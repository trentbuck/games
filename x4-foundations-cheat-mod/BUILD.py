#!/usr/bin/python3
from hashlib import md5
from pathlib import Path
from time import time
with (Path('ext_01.dat').open('wb') as dat_fd,
      Path('ext_01.cat').open('w') as cat_fd):
    for xml_path in sorted(Path.cwd().glob('*%*.xml')):
        xml_bytes = xml_path.read_bytes()
        xml_length = len(xml_bytes)
        xml_mtime = int(xml_path.stat().st_mtime)
        xml_md5sum = md5(xml_bytes).hexdigest()
        xml_target_path = xml_path.name.replace("%","/")
        dat_fd.write(xml_bytes)
        cat_fd.write(f'{xml_target_path} {xml_length} {xml_mtime} {xml_md5sum}\n')
