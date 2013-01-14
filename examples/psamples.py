#!/usr/bin/env python
#
# file: psamples.py		G. Moody	11 March 2006 	
#                               last modified:  14 January 2013
#
# Python translation of psamples.c from the WFDB Programmer's Guide 	

import sys
import wfdb

def main(argv):
    siarray = wfdb.WFDB_SiginfoArray(2)
    if wfdb.isigopen("100s", siarray, 2) < 2: sys.exit(1)
    v = wfdb.intArray(2)
    for i in range(0,10):
        if wfdb.getvec(v) < 0: sys.exit(2)
        print "\t%d\t%d" % (v[0], v[1])

if __name__ == "__main__":
    main(sys.argv[1:])
