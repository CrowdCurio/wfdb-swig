// File: example9.cs       I. Henry    February 18 2005
//
// C# translation of example9.c from the WFDB Programmer's Guide
//
// Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

using System;
using Wfdb;

public class example9 {
    static void Main(string[] argv) {
	int btype, i, j, nbeats = 0, nsig, hwindow, window, stoptime = 0;
	WFDB_Anninfo a = new WFDB_Anninfo();
	WFDB_Annotation annot = new WFDB_Annotation();
		
	if (argv.Length < 2) {
	    Console.WriteLine(
		       "usage: example9 annotator record [beat-type from to]");
	    // Unlike C programs, C# programs do not have any foolproof way
	    // to discover their own names, so the name is given as a constant
	    // above.  The command needed to run this program within a VM
	    // is platform-dependent and likely to be more complex.
	    Environment.Exit(1);
	}
	a.name = argv[0]; a.stat = wfdb.WFDB_READ;
	if ((nsig = wfdb.isigopen(argv[1], null, 0)) < 1) Environment.Exit(2);
	WFDB_SiginfoArray s = new WFDB_SiginfoArray(nsig);
	WFDB_SampleArray v = new WFDB_SampleArray(nsig);
	WFDB_SampleArray vb = new WFDB_SampleArray(nsig);
	if (wfdb.wfdbinit(argv[1], a, 1, s.cast(), (uint)nsig) != nsig)
	    Environment.Exit(3);
	hwindow = wfdb.strtim(".05"); window = 2*hwindow + 1;
	long[,] sum = new long[nsig,window];
	btype = (argv.Length > 2) ? wfdb.strann(argv[2]) : wfdb.NORMAL;
	if (argv.Length > 3) wfdb.iannsettime(wfdb.strtim(argv[3]));
	WFDB_Siginfo s_0_ = s.getitem(0);
	if (argv.Length > 4) {
	    if ((stoptime = wfdb.strtim(argv[4])) < 0)
		stoptime = -stoptime;
	    if (s_0_.nsamp > 0 && stoptime > s_0_.nsamp)
		stoptime = s_0_.nsamp;
	}
	else stoptime = s_0_.nsamp;
	if (stoptime > 0) stoptime -= hwindow;
	while (wfdb.getann(0, annot) == 0 && annot.time < hwindow)
			;
	do {
	    if (annot.anntyp != btype) continue;
	    wfdb.isigsettime(annot.time - hwindow - 1);
	    wfdb.getvec(vb.cast());
	    for (j = 0; j < window && wfdb.getvec(v.cast()) > 0; j++)
		for (i = 0; i < nsig; i++)
		    sum[i,j] += v.getitem(i) - vb.getitem(i);
	    nbeats++;
	} while (wfdb.getann(0, annot) == 0 &&
		 (stoptime == 0L || annot.time < stoptime));
	if (nbeats < 1) {
	    Console.WriteLine("example9: no `" + wfdb.annstr(btype) +
			      "' beats found");
	    Environment.Exit(4);
	}
	Console.WriteLine("Average of {0} `{1}' beats:", nbeats,
			  wfdb.annstr(btype));
	for (j = 0; j < window; j++)
	    for (i = 0; i < nsig; i++)
		Console.Write( "{0:G6}{1}", (double)sum[i,j]/nbeats,
			       ((i < nsig-1) ? "\t" : "\n"));
	wfdb.wfdbquit();
    }
}
