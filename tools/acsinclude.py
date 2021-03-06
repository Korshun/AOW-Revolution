#!/usr/bin/python3
 
import os
import sys
import re
 
ignored = { 'zcommon.acs' }
included = set()
includepath = []
 
def main(input, output, include_path=[]):
    global out
    global includepath
    
    includepath = [os.path.dirname(input)] + include_path
 
    with open(output, 'w') as o:
        out = o
        include_file(os.path.basename(input))
 
def include_file(filename):
    if filename in ignored:
        return
   
    if filename in included:
        print('ERROR: {} included twice'.format(filename))
        sys.exit(1)
    included.add(filename)
 
    text = readfile(resolve_include(filename))
    offset = 0
    for match in re.finditer(r'#include "(.*?)"', text):
        out.write(text[offset:match.start()])
        offset = match.end()
        include_file(match.group(1))
 
    out.write(text[offset:])
 
def resolve_include(filename):
    for dir in includepath:
        filepath = os.path.join(dir, filename)
        if os.path.isfile(filepath):
            return filepath
 
    print('ERROR: {} not found in include path'.format(filename))
    sys.exit(1)
 
def readfile(filename, mode='r'):
    with open(filename, mode) as f:
        return f.read()
 
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: acsinclude <input> <output> [include directories]')
        sys.exit(2)
        
    main(sys.argv[1], sys.argv[2], sys.argv[3:])