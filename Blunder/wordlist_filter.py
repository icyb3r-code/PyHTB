#!/usr/bin/env python3
import sys
import os


if len(sys.argv) < 2:
    print ("Usage: <{}>  < wordlist> ".format(sys.argv[0]))
    sys.exit(1)

wordlist = 'wordlist'

filename = sys.argv[1]
if not os.path.exists(filename):
    print ("File Not Exist!")

with open (filename,'r') as f:
    with open(wordlist,'w') as w:
        for line in f:
            line = line.strip()
            if len(line) > 7:
                w.write(line+"\n")


        w.close()
    f.close()


