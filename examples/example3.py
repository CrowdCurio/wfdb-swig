#!/usr/bin/python
#
# File: example3.py       I. Henry   March 30 2005
#
# Python translation of example2.c from the WFDB Programmer's Guide
# 							   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

import wfdb, sys

def main(argv):
    a = wfdb.WFDB_Anninfo()
    annot = wfdb.WFDB_Annotation()
    if len(argv) < 3:
        print "usage:", argv[0], "annotator record"
        sys.exit(1)
    a.name = argv[1]
    a.stat = wfdb.WFDB_READ
    wfdb.sampfreq(argv[2])
    if wfdb.annopen(argv[2], a, 1) < 0: sys.exit(2)
    while wfdb.getann(0, annot) == 0:
        if annot.aux is not None:
            aux = annot.aux[1:]
        else:
            aux = ""
        print wfdb.timstr(-annot.time), \
              "(" + str(annot.time)+ ")", \
              wfdb.annstr(annot.anntyp), \
              annot.subtyp, \
              annot.chan, \
              annot.num, \
              aux
    wfdb.wfdbquit()

if __name__ == "__main__":
    main(sys.argv)
