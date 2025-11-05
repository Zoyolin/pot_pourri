import subprocess
import logging

def call_python_version(input):
    out = subprocess.run(
        ["./ps1_shortener.py", input],
        capture_output=True,
        timeout=1
    )
    output = out.stdout.decode()
    logging.info(output)
    return output


def call_cpp_version(input):
    out = subprocess.run(
        ["./ps1_shortener.cpp.run", input],
        capture_output=True,
        timeout=1
    )
    output = out.stdout.decode()
    logging.info(output)
    return output

def routine(input, output):
    cpp_output = call_cpp_version(input)
    assert cpp_output == output

    # python_output = call_python_version(input)
    # assert python_output == output

def test_sequence():
    routine("/usr/bin/dossier/folder/fichier", "/usr/bin/dos/fol/fichier")
    routine("usr/bin/dossier/folder/fichier", "usr/bin/dos/fol/fichier")
    routine("/", "/")
    routine("/icbzozbeoc", "/icbzozbeoc")
    routine("/l,c^pzpoz,zpc", "/l,c^pzpoz,zpc")
    routine("/nojrnecei/", "/nojrnecei/")
    routine(".", "/nojrnecei/")
    routine(".", "/nojrnecei/")