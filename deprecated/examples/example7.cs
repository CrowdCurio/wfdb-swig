// File: example7.cs         I. Henry    February 18 2005
//
// C# translation of example7.c from the WFDB Programmer's Guide
//
// Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

using System;
using Wfdb;

public class example7 {
    static void Main(string[] argv) {
	double[] c; double vv;
	int i, j, nc = argv.Length - 4, nsig, nsamp, t;
		
	if (argv.Length < 3) {
	    Console.WriteLine(
		 "usage: example7 record start duration [ coefficients ... ]");
	    // Unlike C programs, C# programs do not have any foolproof way
	    // to discover their own names, so the name is given as a constant
	    // above.  The command needed to run this program within a VM
	    // is platform-dependent and likely to be more complex.
	    Environment.Exit(1);
	}
	if (nc < 1) {
	    nc = 1;
	    c = new double[1];
	    c[0] = 1.0;
	}
	else {
	    c = new double[nc];
	}
	for (i = 0; i < nc; i++)
	    c[i] = Double.Parse(argv[i+3]);
	if ((nsig = wfdb.isigopen(argv[0], null, 0)) < 1)
	    Environment.Exit(3);
	WFDB_SiginfoArray s = new WFDB_SiginfoArray(nsig);
	WFDB_SampleArray v = new WFDB_SampleArray(nsig);
	if (wfdb.isigopen(argv[0], s.cast(), nsig) != nsig)
	    Environment.Exit(3);
	if (wfdb.isigsettime(wfdb.strtim(argv[1])) < 0)
	    Environment.Exit(4);
	if ((nsamp = wfdb.strtim(argv[2])) < 1) {
	    Console.WriteLine("example7: inappropriate value for duration");
	    Environment.Exit(5);
	}
	if (wfdb.osigopen("16l", s.cast(), (uint)nsig) != nsig)
	    Environment.Exit(6);
		
	wfdb.sample(0, 0);
	for (t = 0; t < nsamp && wfdb.sample_valid() == 1; t++) {
	    for (j = 0; j < nsig; j++) {
		for (i = 0, vv = 0.0; i < nc; i++)
		    if (c[i] != 0.0) vv += c[i]*wfdb.sample((uint)j, t+i);
		v.setitem(j, (int)vv);
	    }
	    if (wfdb.putvec(v.cast()) < 0) break;
	}
		
	wfdb.newheader("out");
	wfdb.wfdbquit();
    }
}
