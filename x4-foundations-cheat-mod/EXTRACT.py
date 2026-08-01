#!/usr/bin/python3
# Convert *.cat + *.dat into *.zip.
# Only include .xml files (not big art assets).
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
root = Path('/mnt/c/Program Files (x86)/Steam/steamapps/common/X4 Foundations')
keywords = {
    'ter_s_xperimental',
    # 'gen_m_yacht',
}
with ZipFile(root / 'TWB-XML.zip', mode='w', compression=ZIP_DEFLATED) as zipfile:
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
                if asset_path.lower().endswith('.xml') and any(keyword in asset_path.lower() for keyword in keywords):
                    zipfile.writestr(str(prefix / asset_path), dat_handle.read(asset_bytes))
                else:
                    dat_handle.seek(total_offset)
