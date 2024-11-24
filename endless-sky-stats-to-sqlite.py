#!/usr/bin/python3
import sqlite3
import subprocess
import tempfile
import pathlib

db_path = pathlib.Path('endless-sky.db').resolve()

if False:

    def import_table(table_name, *args):
        with tempfile.TemporaryDirectory() as td_str:
            td = pathlib.Path(td_str)
            csv_path = td / f'{table_name}.csv'
            csv_path.write_bytes(subprocess.check_output(['endless-sky', *args]).replace(b'\n', b'\r\n'))
            subprocess.check_call(
                ['sqlite3', '-csv', '-header', db_path, f".import '{table_name}.csv' {table_name}"],
                cwd=td)

else:

    # Try forcing everything to be an integer column affinity, so
    # sqlite will try to interpret everythign as integers, then reals, then text.
    def import_table(table_name, *args):
        with tempfile.TemporaryDirectory() as td_str:
            td = pathlib.Path(td_str)
            csv_path = td / f'{table_name}.csv'
            csv_str = subprocess.check_output(['endless-sky', *args], text=True).replace('\n', '\r\n')
            csv_path.write_text(csv_str)
            columns_str, _, _ = csv_str.partition('\r\n')
            columns_str = ','.join(
                f'{c} I' if c.startswith('"') else f'"{c}" I'  # yuk
                for c in columns_str.split(','))
            subprocess.check_call(
                ['sqlite3', '-csv', '-header', db_path, f"CREATE TABLE {table_name} ({columns_str})", f".import --skip 1 {table_name}.csv {table_name}"],
                cwd=td)

import_table('ships', '--ships')
import_table('ships_loaded', '--ships', '--loaded')
import_table('ships_loaded_variants', '--ships', '--loaded', '--variants')
import_table('weapons', '--weapons')
import_table('engines', '--engines')
import_table('power', '--power')
import_table('outfits_all', '--outfits', '--all')

# This one won't work, because it's "X, Y1, Y2, Y2" and sqlite3 expects "X, Y1", "X, Y2", "X, Y3".
# import_table('ships_sales', '--ships', '--sales')
# import_table('sales_ships', '--sales', '--ships')
# import_table('ships_sales', '--outfits', '--sales')
# import_table('sales_outfits', '--sales', '--outfits')

# These two are pretty awful because everything is packed into a single column AND it's not json.
# Also has unescaped double quotes, which breaks sqlite3's RFC-strict CSV parsing.
# import_table('planets', '--planets', '--attributes')
# import_table('systems', '--systems', '--attributes')

# FIXME: If I use "-csv -headers" and don't pre-define the table, it
#        (sometimes?) intuits the column/cell datatype as text, and sorting is fucked up.
#        But if I pre-define the table with column affinities,
#        it ignores -header and inserts the first column as a normal row.
