#!/usr/bin/python
#
# File: example7.py       I. Henry   March 31 2005
#
# Python translation of example7.c from the WFDB Programmer's Guide
# 						   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

import wfdb, sys

def main(argv):
    nc = len(argv) - 4

    if len(argv) < 4:
        print "usage:",  argv[0], "record start duration [ coefficients ... ]"
        sys.exit(1)
    if nc < 1: nc = 1
    c = [0.] * nc
    for i in range(0, nc):
        c[i] = float(argv[i+4])
    nsig = wfdb.isigopen(argv[1], None, 0)
    if nsig < 1: sys.exit(3)
    s = wfdb.WFDB_SiginfoArray(nsig)
    v = wfdb.WFDB_SampleArray(nsig)
    if wfdb.isigopen(argv[1], s.cast(), nsig) != nsig: sys.exit(3)
    if wfdb.isigsettime(wfdb.strtim(argv[2])) < 0: sys.exit(4)
    nsamp = wfdb.strtim(argv[3])
    if nsamp < 1:
        print argv[0]+ ": inappropriate value for duration"
        sys.exit(5)
    if wfdb.osigopen("16l", s.cast(), nsig) != nsig: sys.exit(6)
    wfdb.sample(0, 0)
    for t in range(0, nsamp):
        if not wfdb.sample_valid(): break
        for j in range(0, nsig):
            vv = 0
            for i in range(0, nc):
                if c[i] != 0.: vv += c[i] * wfdb.sample(j, t+i)
            v[j] = int(vv)
        if wfdb.putvec(v.cast()) < 0: break
    wfdb.newheader("out")
    wfdb.wfdbquit()

if __name__ == "__main__":
    main(sys.argv)
