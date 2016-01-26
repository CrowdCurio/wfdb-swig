// File: example3.cs       I. Henry    February 18 2005
//
// C# translation of example3.c from the WFDB Programmer's Guide
// 
//
// Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

using System;
using Wfdb;

public class example3 {
    static void Main(string[] argv) {
	WFDB_Anninfo a = new WFDB_Anninfo();
	WFDB_Annotation annot = new WFDB_Annotation();
		
	if (argv.Length < 2) {
	    Console.WriteLine( "usage: example3 annotator record");
	    // Unlike C programs, C# programs do not have any foolproof way
	    // to discover their own names, so the name is given as a constant
	    // above.  The command needed to run this program within a VM
	    // is platform-dependent and likely to be more complex.
	    Environment.Exit(1);
	}
	a.name = argv[0]; a.stat = wfdb.WFDB_READ;
	wfdb.sampfreq(argv[1]);
	if (wfdb.annopen(argv[1], a, 1) < 0) Environment.Exit(2); 
	while (wfdb.getann(0, annot) == 0)
	    Console.WriteLine(wfdb.timstr(-annot.time) + 
			      " (" + annot.time + ") " +
			      wfdb.annstr(annot.anntyp) + " "+
			      annot.subtyp + " " +
			      annot.chan + " " + 
			      annot.num + " " +
			      (annot.aux == null ? "" :
			       annot.aux.Substring(1)));		
	wfdb.wfdbquit();
    }
}
