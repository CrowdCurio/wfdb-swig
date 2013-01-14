#!/usr/bin/env python
#
# File: example1.py       I. Henry      30 March 2005
#                         last revised: 13 January 2013
#
# Example 1: An Annotation Filter
#
# The following program copies an annotation file, changing all QRS
# annotations to NORMAL and deleting all non-QRS annotations.
#
# This is a Python translation of example1.c from the WFDB
# Programmer's Guide.
#
# http://www.physionet.org/physiotools/wpg/wpg_46.htm#Example-1
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
    an = wfdb.WFDB_AnninfoArray(2)
    annot = wfdb.WFDB_Annotation()
    record = raw_input ("Type record name: ")
    iann = raw_input("Type input annotator name: ")
    oann = raw_input("Type output annotator name: ")
    a = wfdb.WFDB_Anninfo()
    a.name = iann
    a.stat = wfdb.WFDB_READ
    an[0] = a

    a = wfdb.WFDB_Anninfo()
    a.name = oann
    a.stat = wfdb.WFDB_WRITE
    an[1] = a
    if wfdb.annopen(record, an, 2) < 0: sys.exit(1)
    while wfdb.getann(0, annot) == 0:
        if wfdb.wfdb_isqrs(annot.anntyp):
            annot.anntyp = wfdb.NORMAL
            if wfdb.putann(0, annot) < 0: break
    wfdb.wfdbquit()

if __name__ == "__main__":
    main(sys.argv[1:])
