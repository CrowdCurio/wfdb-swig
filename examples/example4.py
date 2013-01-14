#!/usr/bin/env python
#
# File: example4.py       I. Henry      30 March 2005
#                         last revised: 13 January 2013
#
# WFDB Example 4: Generating an R-R Interval Histogram
#
# This program reads an annotation file, determines the intervals
# between beat annotations (assumed to be the R-R intervals), and
# accumulates a histogram of them.
#
# This is a Python translation of example1.c from the WFDB 
# Programmer's Guide.
#
# http://www.physionet.org/physiotools/wpg/wpg_49.htm#Example-4
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
    a = wfdb.WFDB_Anninfo()
    annot = wfdb.WFDB_Annotation()
    if len(argv) < 3:
        print "usage:", argv[0], "annotator record"
        sys.exit(1)
    a.name = argv[1]
    a.stat = wfdb.WFDB_READ    
    if wfdb.annopen(argv[2], a, 1) < 0: sys.exit(2)
    rrmax = 3 * wfdb.sampfreq(argv[2])
    if rrmax <= 0: sys.exit(3)
    rrhist = [0] * int(rrmax+1)
    while 1:
        if not (wfdb.getann(0,annot) == 0 and not wfdb.wfdb_isqrs(annot.anntyp)): break
    t = annot.time
    while wfdb.getann(0, annot) == 0:
        if wfdb.wfdb_isqrs(annot.anntyp):
            rr = annot.time - t
            if rr > rrmax: rr = rrmax
            rrhist[rr] += 1
            t = annot.time
    for rr in range(1, int(rrmax)):
        print '%(rr)4d %(time)s' % {'rr': rrhist[rr], 'time': wfdb.mstimstr(rr)}
    rr += 1
    print '%(rr)4d %(time)s (or longer)' % {'rr': rrhist[rr], 'time': wfdb.mstimstr(rr)}
    wfdb.wfdbquit()

if __name__ == "__main__":
    main(sys.argv)
