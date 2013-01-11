// File: example4.cs       I. Henry    February 18 2005
//
// C# translation of example4.c from the WFDB Programmer's Guide
//
// Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

using System;
using Wfdb;

public class example4 {
    static void Main(string[] argv) {
	int rr, rrmax, t;
	WFDB_Anninfo a = new WFDB_Anninfo();
	WFDB_Annotation annot = new WFDB_Annotation();
		
	if (argv.Length < 2) {
	    Console.WriteLine("usage: example4 annotator record\n");
	    // Unlike C programs, C# programs do not have any foolproof way
	    // to discover their own names, so the name is given as a constant
	    // above.  The command needed to run this program within a VM
	    // is platform-dependent and likely to be more complex.
	    Environment.Exit(1);
	}
	a.name = argv[0]; a.stat = wfdb.WFDB_READ;
	if (wfdb.annopen(argv[1], a, 1) < 0) Environment.Exit(2);
	if ((rrmax = (int)(3*wfdb.sampfreq(argv[1]))) <= 0)
	    Environment.Exit(3);
	int[] rrhist = new int[rrmax+1];
	while (wfdb.getann(0, annot) == 0 &&
	       wfdb.wfdb_isqrs(annot.anntyp) == 0)
	        // Note that C# cannot cast an int (such as that returned by
		// isqrs) to a boolean, so omitting the comparison to 0, as in
		// other translations of this code, does not work in this case.
	    ;
	t = annot.time;
	while (wfdb.getann(0, annot) == 0)
	    if (wfdb.wfdb_isqrs(annot.anntyp) != 0) {
		if ((rr = annot.time - t) > rrmax) rr = rrmax;
		rrhist[rr]++;
		t = annot.time;
	    }
	for (rr = 1; rr < rrmax; rr++)
	    Console.WriteLine("{0,4} {1}", rrhist[rr], wfdb.mstimstr(rr));
	Console.WriteLine("{0,4} {1} (or longer)",
			  rrhist[rr], wfdb.mstimstr(rr));
	wfdb.wfdbquit();
    }
}
