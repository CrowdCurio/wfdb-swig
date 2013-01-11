#!/usr/bin/python
#
# File: example4.py       I. Henry   March 30 2005
#
# WFDB Example 4: Generating an R-R Interval Histogram
#
# see http://physionet.org/physiotools/wpg/wpg_144.htm#SEC144
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
