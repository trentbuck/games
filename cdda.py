#!/usr/bin/python3
import subprocess
import pathlib

# This repo is HUGE.  Just download the current commit.
# Do not bother downloading all the commit history between updates.
root = pathlib.Path('~/Desktop/Cataclysm-DDA/').expanduser().resolve()
subprocess.check_call(['git', '-C', root, 'fetch', '--depth=1'])
subprocess.check_call(['git', '-C', root, 'checkout', 'origin/master'])
# https://github.com/CleverRaven/Cataclysm-DDA/blob/master/doc/COMPILING/COMPILING.md#linux-native-sdl-builds
# sudo apt install libsdl2-dev libsdl2-ttf-dev libsdl2-image-dev libsdl2-mixer-dev libfreetype6-dev build-essential
subprocess.check_call(['nice', 'make', '-C', root, 'TILES=1', 'SOUND=1', 'RELEASE=1', 'USE_HOME_DIR=1', 'TESTS=0'])
subprocess.check_call(root / 'cataclysm-launcher')
