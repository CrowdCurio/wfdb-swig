#!/usr/bin/env python
#
# File: example9.py       I. Henry      30 March 2005
#                         last revised: 13 January 2013
#
# Example 9: A Signal Averager
#
# The following program is considerably more complex than the previous
# examples in this chapter. It reads an annotation file (for which the
# annotator name is specified in its first argument, and the record
# name in the second argument) and selects beats of a specified type
# to be averaged. The program selects segments of the signals that are
# within 50 milliseconds of the time of the specified beat
# annotations, subtracts a baseline estimate from each sample, and
# calculates an average waveform (by default, the average normal QRS
# complex).
#
# This is Python translation of example9.c from the WFDB Programmer's
# Guide
#
# http://www.physionet.org/physiotools/wpg/wpg_54.htm#Example-9
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
    nbeats = stoptime = 0
    a = wfdb.WFDB_Anninfo()
    annot = wfdb.WFDB_Annotation()

    if len(argv) < 3:
        print "usage:", argv[0], "annotator record [beat-type from to]",
        sys.exit(1)    
    a.name = argv[1]
    a.stat = wfdb.WFDB_READ
    nsig = wfdb.isigopen(argv[2], None, 0)
    if nsig < 1: sys.exit(2)
    s = wfdb.WFDB_SiginfoArray(nsig)
    v = wfdb.WFDB_SampleArray(nsig)
    vb = wfdb.WFDB_SampleArray(nsig)
    sum = [None] * nsig
    if wfdb.wfdbinit(argv[2], a, 1, s.cast(), nsig) != nsig: sys.exit(3)
    hwindow = wfdb.strtim(".05")
    window = 2*hwindow + 1
    for i in range(nsig):
        sum[i] = [0] * window
    if len(argv) > 3:
        btype = wfdb.strann(argv[3])
    else:
        btype = wfdb.NORMAL
    if len(argv) > 4: wfdb.iannsettime(wfdb.strtim(argv[4]))
    if len(argv) > 5:
        stoptime = wdfb.strtim(argv[5])
        if stoptime < 0:
            stoptime = -stoptime
        if s[0].nsamp > 0 and stoptime > s[0].nsamp:
            stoptime = s[0].nsamp    
    else:
        stoptime = s[0].nsamp
    if stoptime > 0: stoptime -= hwindow

    while 1:
        if not (wfdb.getann(0, annot) == 0 and annot.time < hwindow): break 
    while 1:        
        if annot.anntyp == btype:
            wfdb.isigsettime(annot.time - hwindow - 1)
            wfdb.getvec(vb.cast())
            j=0
            while j < window and wfdb.getvec(v.cast()) > 0:
                for i in range(nsig):
                    sum[i][j] += v[i] - vb[i]
                j += 1
            nbeats += 1
        if not (wfdb.getann(0, annot) == 0 and \
           (stoptime == 0L or annot.time < stoptime)): break
    
    if nbeats < 1:
        print argv[0] + ": no `" + wfdb.annstr(btype) + "' beats found"
        sys.exit(4)

    print "Average of", nbeats, "`" + wfdb.annstr(btype) + "' beats:"
    for j in range(window):
        for i in range(nsig):
            print "%(av)g" % {'av': float(sum[i][j])/nbeats},
            sys.stdout.write("") # surpress next space
            if i < nsig-1:
                print "\t",
            else:
                print
    wfdb.wfdbquit()

if __name__ == "__main__":
    main(sys.argv)
