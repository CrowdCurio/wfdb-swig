#!/usr/bin/env python
#
# File: example6.py       I. Henry      30 March 2005
#                         last revised: 13 January 2013
#
# Example 6: A Differentiator
#
# The program below inverts and differentiates the signals read by
# getvec and writes the results with putvec. The output is readable as
# record ‘dif’. A wide variety of simple digital filters can be
# modelled on this example; see section Example 7: A General-Purpose
# FIR Filter, for a more general approach
#
# This a Python translation of example6.c from the WFDB Programmer's
# Guide
#
# http://www.physionet.org/physiotools/wpg/wpg_51.htm#Example-6
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
    nsamp = 1000
    if len(argv) < 2:
        print "usage:", argv[0], "record"
        sys.exit(1)
    nsig = wfdb.isigopen(argv[1], None, 0)
    if nsig <= 0: sys.exit(2)
    s = wfdb.WFDB_SiginfoArray(nsig)
    vin = wfdb.WFDB_SampleArray(nsig)
    vout = wfdb.WFDB_SampleArray(nsig)
    if wfdb.isigopen(argv[1], s, nsig) != nsig: sys.exit(2)
    if wfdb.osigopen("8l", s, nsig) <= 0: sys.exit(3)
    while nsamp > 0 and wfdb.getvec(vin.cast()) > 0:
        nsamp -= 1
        for i in range(0, nsig): vout[i] -= vin[i]
        if wfdb.putvec(vout.cast()) < 0: break
        for i in range(0, nsig): vout[i] = vin[i]
    wfdb.newheader("dif")
    wfdb.wfdbquit()

if __name__ == "__main__":
    main(sys.argv)
