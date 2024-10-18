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
# FIXME: 01:36 <NetSysFire> yeah i think you want USE_XDG_DIR=1 instead of USE_HOME_DIR=1
#        https://gitlab.archlinux.org/archlinux/packaging/packages/cataclysm-dda/-/blob/main/PKGBUILD?ref_type=heads#L74
#        I also added LTO=1 but haven't tested it yet.
subprocess.check_call(['nice', 'make', '-C', root, 'TILES=1', 'SOUND=1', 'RELEASE=1', 'USE_HOME_DIR=1', 'TESTS=0', 'LTO=1'])
subprocess.check_call(root / 'cataclysm-launcher')
