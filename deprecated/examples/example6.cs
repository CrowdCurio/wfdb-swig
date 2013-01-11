// File: example6.cs        I. Henry    February 18 2005
//
// C# translation of example6.c from the WFDB Programmer's Guide
//
// Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

using System;
using Wfdb;

public class example6 {
    static void Main(string[] argv) {
	int i, nsig, nsamp = 1000;

	if (argv.Length < 1) {
	    Console.WriteLine("usage: example6 record");
	    // Unlike C programs, C# programs do not have any foolproof way
	    // to discover their own names, so the name is given as a constant
	    // above.  The command needed to run this program within a VM
	    // is platform-dependent and likely to be more complex.
	    Environment.Exit(1);
	}
	if ((nsig = wfdb.isigopen(argv[0], null, 0)) <= 0) Environment.Exit(2);
	WFDB_SiginfoArray s = new WFDB_SiginfoArray(nsig);
	WFDB_SampleArray vin = new WFDB_SampleArray(nsig);
	WFDB_SampleArray vout = new WFDB_SampleArray(nsig);
	if (wfdb.isigopen(argv[0], s.cast(), nsig) != nsig)
	    Environment.Exit(2);
	if (wfdb.osigopen("8l", s.cast(), (uint)nsig) <= 0)
	    Environment.Exit(3);
	while (nsamp-- > 0 && wfdb.getvec(vin.cast()) > 0) {
	    for (i = 0; i < nsig; i++) {
		vout.setitem(i, vout.getitem(i) - vin.getitem(i));
	    }
	    if (wfdb.putvec(vout.cast()) < 0) break;
	    for (i = 0; i < nsig; i++) {
		vout.setitem(i, vin.getitem(i));
	    }
	}
	wfdb.newheader("dif");
	wfdb.wfdbquit();
    }
}
