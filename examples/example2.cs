// File: example2.cs       I. Henry    February 18 2005
//
// C# translation of example2.c from the WFDB Programmer's Guide
//
// Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

using System;
using Wfdb;

public class example2 {
    static void Main(string[] argv) {
	WFDB_AnninfoArray an = new WFDB_AnninfoArray(2);
	WFDB_Annotation annot = new WFDB_Annotation();
		
	if (argv.Length < 1) {
	    Console.WriteLine("usage: example2 record");
	    // Unlike C programs, Java programs do not have any foolproof way
	    // to discover their own names, so the name is given as a constant
	    // above.  The command needed to run this program within a VM
	    // is platform-dependent and likely to be more complex.
	    Environment.Exit(1);
	}
	WFDB_Anninfo a = an.getitem(0);
	a.name = "atr"; a.stat = wfdb.WFDB_READ;
	an.setitem(0, a);
	a = an.getitem(1);
	a.name = "aha"; a.stat = wfdb.WFDB_AHA_WRITE;
	an.setitem(1,a);
	if (wfdb.annopen(argv[0], an.cast(), 2) < 0) Environment.Exit(2);
	while (wfdb.getann(0, annot) == 0 && wfdb.putann(0, annot) == 0)
	    ;
	wfdb.wfdbquit();
    }
}
