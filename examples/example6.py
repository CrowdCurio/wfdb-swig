#!/usr/bin/python
#
# File: example6.py       I. Henry   March 30 2005
#
# Python translation of example6.c from the WFDB Programmer's Guide
# 						   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

import wfdb, sys

def main(argv):
    nsamp = 1000
    if len(argv) < 2:
        print "usage:", argv[0], "record"
        sys.exit(1)
    nsig = wfdb.isigopen(argv[1], None, 0)
    if nsig <= 0: sys.exit(2)
    s = wfdb.WFDB_SiginfoArray(nsig)
    vin = wfdb.WFDB_SampleArray(nsig)
    vout = wfdb.WFDB_SampleArray(nsig)
    if wfdb.isigopen(argv[1], s.cast(), nsig) != nsig: sys.exit(2)
    if wfdb.osigopen("8l", s.cast(), nsig) <= 0: sys.exit(3)
    while nsamp > 0 and wfdb.getvec(vin.cast()) > 0:
        nsamp -= 1
        for i in range(0, nsig): vout[i] -= vin[i]
        if wfdb.putvec(vout.cast()) < 0: break
        for i in range(0, nsig): vout[i] = vin[i]
    wfdb.newheader("dif")
    wfdb.wfdbquit()

if __name__ == "__main__":
    main(sys.argv)
