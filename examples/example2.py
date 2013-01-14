#!/usr/bin/env python
#
# File: example2.py       I. Henry      30 March 2005
#                         last revised: 13 January 2013
#
# Example 2: An Annotation Translator
#
# This program translates the ‘atr’ annotations for the record named
# in its argument into an AHA-format annotation file with the
# annotator name ‘aha’
#
# This is a Python translation of example2.c from the WFDB
# Programmer's Guide
#
# http://www.physionet.org/physiotools/wpg/wpg_47.htm#Example-2
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
    # First get a wrapper object to C array of Anninfo structures.
    an = wfdb.WFDB_AnninfoArray(2)
    # In early versions of the wrapper this would have also allocated
    # the WFDB_Anninfo C-structures in the array.  As of SWIG v2.0.8
    # it appears that only the array is allocated, not the Anninfo
    # structures within.


    # Get a wrapper object for an annotation structure 
    annot = wfdb.WFDB_Annotation()

    # Check to see if there is command line argument
    if len(argv) < 2:
        # no command line argument, so print usage and exit
        print "usage:", argv[0], "record"
        sys.exit(1)

    record = argv[1] # the record name is the first argument

    # Now we're going to setup the Anninfo structures so we can call
    # annopen later

    # First get a new Anninfo structure.
    a = wfdb.WFDB_Anninfo()   # LINE_B
    # In the early version this line was:
    #   a = an[0]
    # because calling wfdb.AnninfoArray(2), previously allocated
    # each Anninfo info the the array as well. Now we need to explicitly
    # allocate a new Anninfo struct instead of getting one from the 
    # AnninfoArray "an"

    # now assign the values of a
    a.name = "atr"
    a.stat = wfdb.WFDB_READ

    # finally assign the anninfo struct, "a", to its place in the
    # array "an"
    an[0] = a

    # repeat for output annotation
    a = wfdb.WFDB_Anninfo()
    a.name = "aha"
    a.stat = wfdb.WFDB_AHA_WRITE
    an[1] = a

    # We call annopen with the record name, given on the command line,
    # and the AnninfoArray, "an", we just setup.  
    if wfdb.annopen(record, an, 2) < 0: sys.exit(2)
    # note that in previous versions, it was necessary to use 'an.cast()',
    # rather then simply 'an', when passing an AnninfoArray to a wfdb
    # functoin.  Now the wrappers no longer require the 'cast()' in most
    # cases.

    # now iterate until all annotations have been ready
    while 1:
        # read an annotation from the input annotator and put it into
        # the output, AHA formatted, annotator
        if not (wfdb.getann(0, annot) == 0 and wfdb.putann(0,annot) == 0):
            break
    wfdb.wfdbquit()
    
if __name__ == "__main__":
    main(sys.argv)
