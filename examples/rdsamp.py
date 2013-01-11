#!/usr/bin/python
#
# File: rdann.py       I. Henry   March 28 2005
#
# Minimal WFDB sample reader written in Python, based on rdsamp.c
# 							   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

import getopt, wfdb, sys

def main(argv):
    record = ''

    # Parse the arguments
    try:
        opts, args = getopt.getopt(argv, "hr:", ["help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == '-r':
            record = arg

    # Read the number of signals in the record
    nsig = wfdb.isigopen(record, None, 0)

    # Exit if the record is not found, or there are no signals
    if nsig < 1:
        usage()
        sys.exit(2)

    siarray = wfdb.WFDB_SiginfoArray(nsig)
    wfdb.isigopen(record, siarray.cast(), nsig)

    n = 0
    v = wfdb.WFDB_SampleArray(nsig)

    # Loop over each sample and print the signal values.
    while wfdb.getvec(v.cast()) > 0:
        print n,
        for i in range(0,nsig):
            print v[i],
        print
        n = n + 1
        
    wfdb.wfdbquit()

def usage():
    print "Usage: rdsamp.py -r record"

if __name__ == "__main__":
    main(sys.argv[1:])
