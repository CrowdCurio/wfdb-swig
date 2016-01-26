#!/usr/bin/python
#
# File: example9.py       I. Henry   March 30 2005
#
# Python translation of example9.c from the WFDB Programmer's Guide
# 						   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)


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
