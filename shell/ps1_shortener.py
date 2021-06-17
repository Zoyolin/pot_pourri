#!/usr/bin/python3

import os

# in ~/.bashrc, replace \w by the output of this script   
#    TRIMED_PATH=$(ps1_shortener.py)
#    if [ "$color_prompt" = yes ]; then
#        PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]$TRIMED_PATH\[\033[00m\]\$ '
#    else
#        PS1='${debian_chroot:+($debian_chroot)}\u@\h:$TRIMED_PATH\$ '
#    fi




def path_it(path):
    head, tail = os.path.split(path)
    if head == os.path.abspath(os.sep):
         yield path
    else:
        yield from path_it(head)
        yield tail[0]

pwd = os.getcwd()
ps1 = [d for d in path_it(pwd)]
ps1[-1] = os.path.basename(pwd)
print(os.path.join(*ps1))
