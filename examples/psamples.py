#!/usr/bin/python
#
# file: psamples.py		G. Moody	11 March 2006 	
#
# Python translation of psamples.c from the WFDB Programmer's Guide 	

import wfdb, sys

def main(argv):
    siarray = wfdb.WFDB_SiginfoArray(2)
    if wfdb.isigopen("100s", siarray.cast(), 2) < 2: sys.exit(1)
    v = wfdb.WFDB_SampleArray(2)
    for i in range(0,10):
        if wfdb.getvec(v.cast()) < 0: sys.exit(2)
        print "\t%d\t%d" % (v[0], v[1])

if __name__ == "__main__":
    main(sys.argv[1:])
