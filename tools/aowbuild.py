#!/usr/bin/python3

from glob import glob
import re

def main():
	global decorate
	global acs
	decorate = open('aow/decorate/acsdefines.txt', 'w')
	acs = open('aow/src/scriptnumbers.acs', 'w')
	
	for filename in glob('aow/src/a_*.acs') + ['aow/src/aow.acs']:
		process_acs(filename)
		
def readfile(filename, mode='r'):
	with open(filename, mode) as file:
		return file.read()
		
regex_script = re.compile('script\s+(aow_\w+)')
script_number = 300

regex_define = re.compile('#define\s+(\w+)\s+(\d+)\s')

def process_acs(filename):
	text = readfile(filename)
	for match in regex_script.finditer(text):
		global script_number
		name = match.group(1)
		
		if name.startswith('aow_map_')  or name.startswith('aow_cmd_'):
			continue

		script_number += 1
		acs.write('#define {} {}\n'.format(name, script_number))
		decorate.write('const int {} = {};\n'.format(name, script_number))
		
	for match in regex_define.finditer(text):
		name = match.group(1)
		value = match.group(2)
		decorate.write('const int {} = {};\n'.format(name, value))
	
if __name__ == '__main__':
	main()
