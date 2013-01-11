#!/usr/bin/python
#
# File: example1.py       I. Henry   March 30 2005
#
# Python translation of example1.c from the WFDB Programmer's Guide 
# 							   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

import wfdb, sys

def main(argv):
    an = wfdb.WFDB_AnninfoArray(2)
    annot = wfdb.WFDB_Annotation()
    record = raw_input ("Type record name: ")
    iann = raw_input("Type input annotator name: ")
    oann = raw_input("Type output annotator name: ")
    a = an[0]
    a.name = iann
    a.stat = wfdb.WFDB_READ
    an[0] = a
    a = an[1]
    a.name = oann
    a.stat = wfdb.WFDB_WRITE
    an[1] = a
    if wfdb.annopen(record, an.cast(), 2) < 0: sys.exit(1)
    while wfdb.getann(0, annot) == 0:
        if wfdb.wfdb_isqrs(annot.anntyp):
            annot.anntyp = wfdb.NORMAL
            if wfdb.putann(0, annot) < 0: break
    wfdb.wfdbquit()

if __name__ == "__main__":
    main(sys.argv[1:])
