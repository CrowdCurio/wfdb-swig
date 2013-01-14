#!/usr/bin/env python
#
# File: example10.py       I. Henry      30 March 2005
#                          last revised: 13 January 2013
#
# Example 10: A QRS Detector
#
# This program reads a single ECG signal, attempts to detect QRS
# complexes, and records their locations in an annotation file. The
# detector algorithm is based on a Pascal program written by
# W.A.H. Engelse and C. Zeelenberg, “A single scan algorithm for
# QRS-detection and feature extraction”, Computers in Cardiology
# 6:37-42 (1979).
#
# This is a Python translation of example10.c from the WFDB
# Programmer's Guide
# 						   
# http://www.physionet.org/physiotools/wpg/wpg_55.htm#Example-10
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

    time = maxslope = nslope = scmin = 0
    a = wfdb.WFDB_Anninfo()
    annot = wfdb.WFDB_Annotation()

    if len(argv) < 2:
        print "usage:", argv[0], "record [threshold]"
        sys.exit(1)
    
    a.name = "qrs"
    a.stat = wfdb.WFDB_WRITE

    nsig = wfdb.isigopen(argv[1], None, 0)
    if nsig < 1: sys.exit(2)
    s = wfdb.WFDB_SiginfoArray(nsig)
    v = wfdb.WFDB_SampleArray(nsig)
    if wfdb.wfdbinit(argv[1], a, 1, s, nsig) != nsig: sys.exit(2)
    if wfdb.sampfreq(None) < 240. or wfdb.sampfreq(None) > 260.:
	wfdb.setifreq(250.)
    if len(argv) > 2: scmin = wfdb.muvadu(0, argv[2])
    if scmin < 1: scmin = wfdb.muvadu(0, 1000)
    slopecrit = scmax = 10 * scmin
    ms160 = wfdb.strtim("0.16")
    ms200 = wfdb.strtim("0.2")
    s2 = wfdb.strtim("2")
    annot.subtyp = annot.chan = annot.num = 0
    annot.aux = None
    wfdb.getvec(v.cast())
    t9 = t8 = t7 = t6 = t5 = t4 = t3 = t2 = t1 = v[0]

    while 1:
        t0 = v[0]
        filter = t0 + 4*t1 + 6*t2 + 4*t3 + t4 - t5 - 4*t6 - 6*t7 - 4*t8 - t9
        if time % s2 == 0:
            if nslope == 0:
                slopecrit -= slopecrit >> 4
                if slopecrit < scmin: slopecrit = scmin
            elif nslope >= 5:
                slopecrit += slopecrit >> 4
                if slopecrit > scmax: slopecrit = scmax
        if nslope == 0 and abs(filter) > slopecrit: 
            nslope = 1
            maxtime = ms160
            if filter > 0:
                sign = 1
            else:
                sign = -1
            qtime = time
        if nslope != 0:
            if filter * sign < -slopecrit: 
                sign = -sign
                nslope = nslope + 1
                if nslope > 4:       
                    maxtime = ms200
                else:
                    maxtime = ms160
            elif filter * sign > slopecrit and \
                     abs(filter) > maxslope:
                maxslope = abs(filter)
            if maxtime < 0:
                if 2 <= nslope and nslope <= 4:
                    slopecrit += ((maxslope>>2) - slopecrit) >> 3
                    if slopecrit < scmin:
                        slopecrit = scmin
                    elif slopecrit > scmax:
                        slopecrit = scmax
                    annot.time = wfdb.strtim("i") - (time - qtime) - 4
                    annot.anntyp = wfdb.NORMAL
                    wfdb.putann(0, annot)
                    time = 0
                elif nslope >= 5: 
                    annot.time = wfdb.strtim("i") - (time - qtime) - 4
                    annot.anntyp = wfdb.ARFCT
                    wfdb.putann(0, annot)
                nslope = 0
            maxtime = maxtime - 1
        t9 = t8
        t8 = t7
        t7 = t6
        t6 = t5
        t5 = t4
        t4 = t3
        t3 = t2
        t2 = t1
        t1 = t0
        time = time + 1
        if not wfdb.getvec(v.cast()) > 0: break

    wfdb.wfdbquit()


if __name__ == "__main__":
    main(sys.argv)
