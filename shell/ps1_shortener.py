#!/usr/bin/python3
import os

# INSTALLATION :
install_prefix = "/usr/bin/"
file_name = os.path.basename(__file__)
if not os.path.isfile(install_prefix + file_name):
    from subprocess import call
    # create link to location accessible from path (asks for root priviledges)
    call(["sudo", "ln", "-fs",os.path.realpath(__file__), install_prefix])
    # replace \w in the PS1 composition by a call to this script
    call(["sed", "-i", f"/PS1=/ {{s/\\\\w/`{file_name}`/}}", f"{os.path.expanduser('~')}/.bashrc"])

ps1 = os.getcwd().replace(os.path.expanduser("~"), "/~").split(os.sep)[1:]
middle = [d[:3] for d in ps1[1:-1]]
if len(ps1) > 1:
    ps1 = os.path.join(ps1[0], *middle, ps1[-1])
else:
    ps1 = ps1[0]
print(ps1)
