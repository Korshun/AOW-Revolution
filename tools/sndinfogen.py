#!/usr/bin/python3
# SNDINFO generator v2
 
import sys
import os
 
def main(pk3root):
    sounds = {}
    randomized = {}
    warning = False
    with open(os.path.join(pk3root, 'sndinfo.sux'), 'w') as sndinfo:
        sndinfo.write('DSEMPTY DSEMPTY\n')
        sndinfo.write('NOSOUND DSEMPTY\n')
    
        for root, dirs, files in os.walk(os.path.join(pk3root, 'sounds'), onerror=raise_error):
            for file in files:
                filepath = os.path.join(root, file)
                lumpname = os.path.splitext(file)[0].upper()
                
                if lumpname in sounds:
                    print('WARNING: conflicting sounds names: {} {}'.format(sounds[lumpname], filepath))
                    warning = True
                    continue
                
                sndinfo.write(lumpname + ' ' + lumpname + '\n')
                sounds[lumpname] = filepath
                
                if lumpname[-1].isdigit():
                    digit = lumpname[-1]
                    lumpname = lumpname[:-1]
                    if lumpname in randomized:
                        randomized[lumpname].append(digit)
                    else:
                        randomized[lumpname] = [digit]
                        
        for lumpname, digits in randomized.items():
            if lumpname in sounds:
                continue
                
            sndinfo.write('$random ' + lumpname + ' { ')
            for digit in digits:
                sndinfo.write(lumpname + digit + ' ')
            sndinfo.write('} \n')
        
    sys.exit(int(warning))
 
def raise_error(x):
    raise x
 
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: sndinfogen <pk3 root>')
        sys.exit(2)
    main(sys.argv[1])
