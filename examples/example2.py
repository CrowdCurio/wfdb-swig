#!/usr/bin/python
#
# File: example2.py       I. Henry   March 30 2005
#
# Python translation of example2.c from the WFDB Programmer's Guide
#
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

import wfdb, sys

def main(argv):
    an = wfdb.WFDB_AnninfoArray(2)
    annot = wfdb.WFDB_Annotation()
    if len(argv) < 2:
        print "usage:", argv[0], "record"
        sys.exit(1)
    a = an[0]
    a.name = "atr"
    a.stat = wfdb.WFDB_READ
    an[0] = a
    a = an[1]
    a.name = "aha"
    a.stat = wfdb.WFDB_AHA_WRITE
    an[1] = a
    if wfdb.annopen(argv[1], an.cast(), 2) < 0: sys.exit(2)
    while 1:
        if not (wfdb.getann(0, annot) == 0 and wfdb.putann(0,annot) == 0):
            break
    wfdb.wfdbquit()
    
if __name__ == "__main__":
    main(sys.argv)
