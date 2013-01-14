#!/usr/bin/env python
#
# File: rdann.py       I. Henry      28 March 2005
#                      last revised: 13 January 2013
#
# Minimal WFDB sample reader written in Python, based on rdsamp.c
# 							   
# Copyright (C) 2013 Isaac C. Henry (ihenry42@gmail.org)
# This file is part of wfdb-swig.
#
# wfdb-swig is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wfdb-swig is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with wfdb-swig.  If not, see <http://www.gnu.org/licenses/>.

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
    wfdb.isigopen(record, siarray, nsig)

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
