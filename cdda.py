#!/usr/bin/python3
import subprocess
import pathlib

# This repo is HUGE.  Just download the current commit.
# Do not bother downloading all the commit history between updates.
root = pathlib.Path('~/Desktop/Cataclysm-DDA/').expanduser().resolve()
# FIXME: track "0.H-branch" (not "master")?
#        git fetch --depth 1 origin 0.H-branch:refs/remotes/origin/0.H-branch
#        git remote set-branches origin 0.H-branch
#        git remote set-head --delete origin
#        git remote prune origin
subprocess.check_call(['git', '-C', root, 'fetch', '--depth=1'])
subprocess.check_call(['git', '-C', root, 'checkout', 'origin/0.H-branch'])
# To free up some space in .git again...
#     git tag -d cdda-experimental-2021-07-03-0512 cdda-experimental-2023-02-14-0634 cdda-experimental-2023-03-01-2354 ...
#     git reflog expire --expire=all --all
#     git gc --prune=now
# To manually add a single tag of a released version...
#     git fetch --depth 1 origin 0.F:refs/remotes/origin/0.F
# https://github.com/CleverRaven/Cataclysm-DDA/blob/master/doc/COMPILING/COMPILING.md#linux-native-sdl-builds
# sudo apt install libsdl2-dev libsdl2-ttf-dev libsdl2-image-dev libsdl2-mixer-dev libfreetype6-dev build-essential
# FIXME: 01:36 <NetSysFire> yeah i think you want USE_XDG_DIR=1 instead of USE_HOME_DIR=1
#        https://gitlab.archlinux.org/archlinux/packaging/packages/cataclysm-dda/-/blob/main/PKGBUILD?ref_type=heads#L74
#        I also added LTO=1 but haven't tested it yet.
subprocess.check_call(['nice', 'make', '-C', root, 'TILES=1', 'SOUND=1', 'RELEASE=1', 'USE_XDG_DIR=1', # 'USE_HOME_DIR=1',
                       'TESTS=0', 'LTO=1'])
subprocess.check_call(root / 'cataclysm-launcher')
