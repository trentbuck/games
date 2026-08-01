#!/usr/bin/python3
from hashlib import md5
from pathlib import Path
from time import time
fuck_date = int(time())
fuck_paths = {
    # Can't increase Hydra Royal's cargo & weapon hardpoints without also affecting Hydra's.
    # And the AI has regular Hydras.
    # 'assets/units/size_m/macros/ship_bor_m_corvette_02_a_macro.xml',
    # 'assets/units/size_m/ship_bor_m_corvette_02.xml',

    'extensions/ego_dlc_timelines/assets/props/storagemodules/macros/storage_ter_s_xperimental_01_a_macro.xml',
    'extensions/ego_dlc_timelines/assets/props/surfaceelements/macros/shield_ter_s_xperimental_01_mk1_story_macro.xml',
    'extensions/ego_dlc_timelines/assets/props/surfaceelements/macros/shield_ter_s_xperimental_01_mk5_macro.xml',
    'extensions/ego_dlc_timelines/assets/props/surfaceelements/macros/shield_ter_s_xperimental_01_mk5_video_macro.xml',
    'extensions/ego_dlc_timelines/assets/props/surfaceelements/shield_ter_s_xperimental_01.xml',
    'extensions/ego_dlc_timelines/assets/props/surfaceelements/shield_ter_s_xperimental_01_mk5_video.xml',
    'extensions/ego_dlc_timelines/assets/units/size_s/macros/ship_ter_s_xperimental_01_a_macro.xml',
    'extensions/ego_dlc_timelines/assets/units/size_s/macros/ship_ter_s_xperimental_01_a_story_macro.xml',
    'extensions/ego_dlc_timelines/assets/units/size_s/ship_ter_s_xperimental_01.xml',
    'extensions/ego_dlc_timelines/assets/props/engines/macros/engine_ter_s_virtual_01_mk1_macro.xml',
    'extensions/ego_dlc_timelines/assets/props/surfaceelements/macros/shield_ter_s_virtual_01_mk1_macro.xml',
    'extensions/ego_dlc_timelines/assets/units/size_s/macros/ship_ter_s_fighter_04_a_macro.xml',
    'extensions/ego_dlc_timelines/assets/units/size_s/macros/ship_ter_s_fighter_04_b_macro.xml',


}
fuck_bytes = Path('ext_01.xml').read_bytes()
fuck_len = len(fuck_bytes)
fuck_sum = md5(fuck_bytes).hexdigest()
Path('ext_01.dat').write_bytes(len(fuck_paths) * fuck_bytes)
Path('ext_01.cat').write_text('\n'.join(
    f'{fuck_path} {fuck_len} {fuck_date} {fuck_sum}'
    for fuck_path in sorted(fuck_paths)))
