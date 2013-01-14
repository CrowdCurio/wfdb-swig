#!/usr/bin/env python
#
# File: rdann.py       I. Henry      28 March 2005
#                      last revised: 13 January 2013
# 
# Minimal WFDB annotator reader written in Python, based on rdann.c
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
