#!/usr/bin/env python
#
# File: example3.py       I. Henry      30 March 2005
#                         last revised: 13 January 2013
#
# Example 3: An Annotation Printer
#
# This program prints annotations in readable form. Its first argument
# is an annotator name, and its second argument is a record name.
#
# This is a Python translation of example3.c from the WFDB
# Programmer's Guide
# 
# http://www.physionet.org/physiotools/wpg/wpg_48.htm#Example-3
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
    wfdb.sampfreq(argv[2])
    if wfdb.annopen(argv[2], a, 1) < 0: sys.exit(2)
    while wfdb.getann(0, annot) == 0:
        if annot.aux is not None:
            aux = annot.aux[1:]
        else:
            aux = ""
        print wfdb.timstr(-annot.time), \
              "(" + str(annot.time)+ ")", \
              wfdb.annstr(annot.anntyp), \
              annot.subtyp, \
              annot.chan, \
              annot.num, \
              aux
    wfdb.wfdbquit()

if __name__ == "__main__":
    main(sys.argv)
