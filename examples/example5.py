#!/usr/bin/python
#
# File: example5.py       I. Henry   March 30 2005
#
# Python translation of example5.c from the WFDB Programmer's Guide
# 							   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

import wfdb, sys

def main(argv):
    if len(argv) < 2:
        print "usage:", argv[0], "record"
        sys.exit(1)
    nsig = wfdb.isigopen(argv[1], None, 0)
    if nsig < 1: sys.exit(2)
    s = wfdb.WFDB_SiginfoArray(nsig)
    if wfdb.isigopen(argv[1], s.cast(), nsig) != nsig: sys.exit(2)
    print "Record", argv[1]
    print "Starting time:", wfdb.timstr(0)
    print "Sampling frequency: %(sf)g Hz" % {'sf': wfdb.sampfreq(argv[1])}
    print nsig, "signals"
    for i in range(0,nsig):
        print "Group %(g)d, Signal %(s)d:" % {'g': s[i].group, 's': i }
        print " File:", s[i].fname
        print " Description:", s[i].desc
        print " Gain:",
        if s[i].gain == 0.:
            print "uncalibrated; assume", wfdb.WFDB_DEFGAIN,
        else:
            print "%(gain)g" % {'gain': s[i].gain},
        if s[i].units is not None:
            print "adu/" + s[i].units
        else:
            print "adu/mV"
        print " Initial value:", s[i].initval
        print " Storage format:", s[i].fmt
        print " I/O:",
        if s[i].bsize == 0:
            print "can be unbuffered"
        else:
            print str(s[i].bsize) + "-byte blocks"
        print " ADC resolution:", s[i].adcres, "bits"
        print " ADC zero:", s[i].adczero
        if s[i].nsamp > 0:
            print " Length:", wfdb.timstr(s[i].nsamp), \
                  "(" + str(s[i].nsamp) + " sample intervals)"
            print " Checksum:", s[i].cksum
        else:
            print " Length undefined"
    wfdb.wfdbquit()
    
if __name__ == "__main__":
    main(sys.argv)
