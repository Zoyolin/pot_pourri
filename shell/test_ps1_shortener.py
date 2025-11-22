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


def call_c_version(input):
    out = subprocess.run(
        ["./ps1_shortener.c.run", input],
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

def routine(harness, input, output):
    bin_output = harness(input)
    print(f"{input} -> {output} resulted in fact in ", end="")
    # assert bin_output == output
    print(f"{bin_output}")

    # python_output = call_python_version(input)
    # assert python_output == output

def test_sequence():
    callers = [call_cpp_version, call_c_version, call_python_version]
    for caller in callers:
        routine(caller, "/usr/bin/dossier/folder/fichier", "/usr/bin/dos/fol/fichier")
        routine(caller, "usr/bin/dossier/folder/fichier", "usr/bin/dos/fol/fichier")
        routine(caller, "/", "/")
        routine(caller, "/icbzozbeoc", "/icbzozbeoc")
        routine(caller, "/l,c^pzpoz,zpc", "/l,c^pzpoz,zpc")
        routine(caller, "/nojrnecei/", "/nojrnecei/")
        routine(caller, ".", "/nojrnecei/")
        routine(caller, ".", "/nojrnecei/")

if __name__ == "__main__":
    test_sequence()