#!/usr/bin/python3
# Extract /macros/macro[name="ship_..."]/properties/jerk and ./physics stats for all ships, save into a sqlite database.
from pathlib import Path
from pprint import pprint
from sqlite3 import connect
from lxml.etree import fromstring
root = Path('/mnt/c/Program Files (x86)/Steam/steamapps/common/X4 Foundations')
with connect('ships.db') as conn:
    conn.execute('DROP TABLE IF EXISTS ship')
    conn.execute("""
    CREATE TABLE ship 
    ( name TEXT NOT NULL
    , class TEXT NOT NULL
    , mass REAL
    , crew INTEGER
    , physics_inertia_pitch REAL
    , physics_inertia_yaw REAL
    , physics_inertia_roll REAL
    , physics_drag_forward REAL
    , physics_drag_reverse REAL
    , physics_drag_horizontal REAL
    , physics_drag_vertical REAL
    , physics_drag_pitch REAL
    , physics_drag_yaw REAL
    , physics_drag_roll REAL
    , physics_accfactors_forward REAL
    , physics_accfactors_reverse REAL
    , physics_accfactors_horizontal REAL
    , physics_accfactors_vertical REAL
    , jerk_forward_accel REAL
    , jerk_forward_decel REAL
    , jerk_forward_ratio REAL
    , jerk_forward_boost_accel REAL
    , jerk_forward_boost_decel REAL
    , jerk_forward_boost_ratio REAL
    , jerk_forward_travel_accel REAL
    , jerk_forward_travel_decel REAL
    , jerk_forward_travel_ratio REAL
    , jerk_strafe_value REAL
    , jerk_angular_value REAL
    )
    """)

    view_cols = [
        f"json_array(min({c}), cast(round(avg({c})) as int), max({c})) as {c}"
        for c in [
                'mass',
                'crew',
                'physics_inertia_pitch',
                'physics_inertia_yaw',
                'physics_inertia_roll',
                'physics_drag_forward',
                'physics_drag_reverse',
                'physics_drag_horizontal',
                'physics_drag_vertical',
                'physics_drag_pitch',
                'physics_drag_yaw',
                'physics_drag_roll',
                'physics_accfactors_forward',
                'physics_accfactors_reverse',
                'physics_accfactors_horizontal',
                'physics_accfactors_vertical',
                'jerk_forward_accel',
                'jerk_forward_decel',
                'jerk_forward_ratio',
                'jerk_forward_boost_accel',
                'jerk_forward_boost_decel',
                'jerk_forward_boost_ratio',
                'jerk_forward_travel_accel',
                'jerk_forward_travel_decel',
                'jerk_forward_travel_ratio',
                'jerk_strafe_value',
                'jerk_angular_value',
                ]]
    conn.execute(f"CREATE VIEW ship_spread_by_class AS SELECT class, {','.join(view_cols)} from ship group by class order by max(mass)")
    for cat_path in root.glob('**/**.cat'):
        total_offset = 0
        if cat_path.name.endswith('_sig.cat'):
            continue
        prefix = cat_path.parent.relative_to(root)
        with cat_path.with_suffix('.dat').open('rb') as dat_handle:
            for cat_entry in cat_path.read_text().splitlines():
                # NOTE: some path names have spaces in them, sigh, so split from the back.
                asset_path, asset_bytes, asset_mtime, asset_md5sum = cat_entry.rsplit(None, 3)
                asset_bytes = int(asset_bytes)
                total_offset += asset_bytes
                if not asset_path.lower().endswith('.xml'):
                    dat_handle.seek(total_offset)
                    continue
                obj = fromstring(dat_handle.read(asset_bytes))
                for macro_obj in obj.xpath("/macros/macro[starts-with(@name, 'ship')]/properties/physics/../.."):
                    row = {
                        'name': macro_obj.get('name'),
                        'class': macro_obj.get('class'),
                        'mass': (macro_obj.xpath('./properties/physics/@mass') or [None])[0],
                        'crew': (macro_obj.xpath('./properties/people/@capacity') or [None])[0],

                        }
                    for obj in macro_obj.xpath('./properties/physics/*'):
                        for key, value in obj.items():
                            row[f'physics_{obj.tag}_{key}'] = value
                    for obj in macro_obj.xpath('./properties/jerk/*'):
                        for key, value in obj.items():
                            row[f'jerk_{obj.tag}_{key}'] = value
                    # pprint(row)
                    query = f"""INSERT INTO ship ({','.join(row.keys())}) VALUES ({','.join('?' for _ in row.keys())})"""
                    # pprint(query)
                    # pprint(row.values())
                    conn.execute(query, tuple(row.values()))
    # conn.commit()
    # for line in conn.iterdump():
    #     print(line)
