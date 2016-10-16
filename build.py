#!/usr/bin/python3

import sys
import os
from subprocess import call

python = sys.executable

def error(text):
    print(text, file=sys.stderr)
    input('Press Enter to continue...')
    sys.exit(1)

def exe(name):
    if sys.platform == 'win32':
        name += '.exe'
    return name

try:    
	if call([python, 'tools/aowbuild.py']) != 0:
		error('AOWBUILD FAILED')
	if call([exe('bcc/bcc'), 'aow/src/aow.acs', 'aow/acs/aow.o']) != 0:
		error('BCC FAILED')
	if call([python, 'tools/acsinclude.py', 'aow/src/aow.acs', 'aow/src/aowmap.acs']) != 0:
		error("ACSINCLUDE FAILED")
	if call([python, 'tools/sndinfogen.py', 'aow']) != 0:
		error("SNDINFOGEN FAILED")
except Exception as e:
	error(e)
		
print("Success")
