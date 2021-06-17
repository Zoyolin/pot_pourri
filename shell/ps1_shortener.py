#!/usr/bin/python3
import os

# INSTALLATION :
install_prefix = "/usr/bin/"
file_name = os.path.basename(__file__)
if not os.path.isfile(install_prefix + file_name):
    from subprocess import call
    # create link to location accessible from path (asks for root priviledges)
    call(["sudo", "ln", "-fs", __file__, install_prefix])
    # replace \w in the PS1 composition by a call to this script
    call(["sed", "-i", f"s/\\\\w/\$\({file_name}\)/", f"{os.path.expanduser('~')}/.bashrc"])

def path_it(path):
    head, tail = os.path.split(path)
    if head == os.path.abspath(os.sep):
         yield path
    else:
        yield from path_it(head)
        yield tail[0]

pwd = os.getcwd()
ps1 = [d for d in path_it(pwd)]
if len(ps1) > 1 :
    ps1[-1] = os.path.basename(pwd)
print(os.path.join(*ps1))
