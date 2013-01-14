#!/usr/bin/env python
#
# File: example5.py       I. Henry      30 March 2005
#                         last revised: 13 January 2013
#
# WFDB Example 5: Reading Signal Specifications
#
# This program reads the signal specifications of the record named as
# its argument
#
# This is a Python translation of example5.c from the WFDB
# Programmer's Guide
#
# http://www.physionet.org/physiotools/wpg/wpg_50.htm#Example-5
#
# Copyright (C) 2013 Isaac C. Henry (ihenry42@gmail.org)
#
# This file is part of wfdb-swig.
#
# wfdb-swig is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wfdb-swig is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with wfdb-swig.  If not, see <http://www.gnu.org/licenses/>.

import wfdb, sys

def main(argv):
    if len(argv) < 2:
        print "usage:", argv[0], "record"
        sys.exit(1)
    nsig = wfdb.isigopen(argv[1], None, 0)
    if nsig < 1: sys.exit(2)
    s = wfdb.WFDB_SiginfoArray(nsig)
    if wfdb.isigopen(argv[1], s, nsig) != nsig: sys.exit(2)
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
