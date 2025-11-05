#!/usr/bin/python3

"""shortens the prompt path."""
import os
import sys

def auto_install():
    install_prefix = "/usr/bin/"  # must be in the PATH
    file_name = os.path.basename(__file__)
    if not os.path.isfile(install_prefix + file_name):
        from subprocess import call

        # create link to location accessible from path (asks for root priviledges)
        call(["sudo", "ln", "-fs", os.path.realpath(__file__), install_prefix])
        # replace \w in the PS1 composition by a call to this script
        call(
            [
                "sed",
                "-i",
                f"/PS1=/ {{s/\\\\w/`{file_name}`/}}",
                f"{os.path.expanduser('~')}/.bashrc",
            ]
        )

def shorten():
    """
    TODO: consider multiple users on 1 machine
    """
    NB_DIGITS = 3

    if len(sys.argv) == 1:
        print(f"Usage: {os.path.basename(__file__)} <path>" )
    if len(sys.argv) != 2:
        exit(os.EX_USAGE)
    
    # use that to run on current path.
    # pwd = os.getcwd().replace(os.path.expanduser("~"), "/~")
    pwd=sys.argv[1]

    ps1 = pwd.split(os.sep)[1:]
    ps1[1:-1] = [elem[:NB_DIGITS] for elem in ps1[1:-1]]
    ps1 = os.path.join(*ps1)
    if ps1[0] != "~":
        ps1 = "/" + ps1
    print(ps1, end="")

if __name__ == "__main__":
    # auto_install()
    shorten()