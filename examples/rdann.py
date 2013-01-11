#!/usr/bin/python
#
# File: rdann.py       I. Henry   March 28 2005
#
# Minimal WFDB annotator reader written in Python, based on rdann.c
# 							   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

import getopt, wfdb, sys

def main(argv):
    record = ''
    annotator = ''

    # parse the arguments
    try:
        opts, args = getopt.getopt(argv, "hr:a:", ["help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == '-r':
            record = arg
        elif opt == '-a':
            annotator = arg

    if len(record) == 0 or len(annotator) == 0:
        usage()
        sys.exit(2)
        
    # set the sampling frequency
    sps = wfdb.sampfreq(record)
    if sps < 0:
        sps = wfdb.WFDB_DEFFREQ
        wfdb.setsampfreq(sps)
            
    # get a new anninfo object
    ai = wfdb.WFDB_Anninfo()
    
    # set ai fields
    ai.name = annotator
    ai.stat = wfdb.WFDB_READ
    
    # open the annotation
    result = wfdb.annopen( record, ai, 1 )
    
    if result < 0:
        usage()
        sys.exit(2)
        
    # get a new annotation object
    annot = wfdb.WFDB_Annotation()
    
    while wfdb.getann(0, annot) == 0:

        # remove first char from aux string, if there is one
        if annot.aux is not None:
            aux = annot.aux[1:]
        else:
            aux = ""
                
        print "%s\t%d\t%s\t%d\t%d\t%d\t%s" % ( \
              wfdb.mstimstr(-annot.time), \
              annot.time, \
              wfdb.annstr(annot.anntyp),
              annot.subtyp,
              annot.chan, \
              annot.num, \
              aux)

    wfdb.wfdbquit()


def usage():
    print "Usage: rdann.py -r record -a annotator"

    
if __name__ == "__main__":
    main(sys.argv[1:])
