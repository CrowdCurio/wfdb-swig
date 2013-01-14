#!/usr/bin/env python
#
# File: example7.py       I. Henry      31 March 2005
#                         last revised: 13 January 2013
#
# Example 7: A General-Purpose FIR Filter
#
# This program illustrates the use of sample to obtain random access
# to signals, a technique that is particularly useful for implementing
# digital filters. The first argument is the record name, the second
# and third arguments are the start time and the duration of the
# segment to be filtered, and the rest of the arguments are
# finite-impulse-response (FIR) filter coefficients. For example, if
# this program were named 'filter', it might be used by
#	
#  filter 100 5:0 20 .2 .2 .2 .2 .2
#
# which would apply a five-point moving average (rectangular window)
# filter to 20 seconds of record '100', beginning 5 minutes into the
# record. The output of the program is readable as record 'out', for
# which a header file is created in the current directory.
#
# This is a Python translation of example7.c from the WFDB
# Programmer's Guide
#
# http://www.physionet.org/physiotools/wpg/wpg_52.htm#Example-7
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
    v = wfdb.intArray(nsig)
    if wfdb.isigopen(argv[1], s, nsig) != nsig: sys.exit(3)
    if wfdb.isigsettime(wfdb.strtim(argv[2])) < 0: sys.exit(4)
    nsamp = wfdb.strtim(argv[3])
    if nsamp < 1:
        print argv[0]+ ": inappropriate value for duration"
        sys.exit(5)
    if wfdb.osigopen("16l", s, nsig) != nsig: sys.exit(6)
    wfdb.sample(0, 0)
    for t in range(0, nsamp):
        if not wfdb.sample_valid(): break
        for j in range(0, nsig):
            vv = 0
            for i in range(0, nc):
                if c[i] != 0.: vv += c[i] * wfdb.sample(j, t+i)
            v[j] = int(vv)
        if wfdb.putvec(v) < 0: break
    wfdb.newheader("out")
    wfdb.wfdbquit()

if __name__ == "__main__":
    main(sys.argv)
