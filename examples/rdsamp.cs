// File: rdsamp.cs       I. Henry    February 16 2005
//
// Minimal WFDB sample reader written C#, based on rdsamp.c
//
// Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

using System;
using Wfdb;

public class rdsamp {
    static void Main(string[] argv) {
	string record = null;

	if (argv.Length < 2) {
	    usage();
	    Environment.Exit(2);
	}

	for (int i = 0; i < argv.Length; i++) {
	    if (argv[i] == "-r") {
		record = argv[++i];
	    } else {
		usage();
	    }
	}

	if (record == null) {
	    usage();
	    Environment.Exit(2);
	}

	int nsig, n=0;    
	nsig = wfdb.isigopen(record, null, 0);
	    
	if (nsig <= 0) {
	    usage();
	    Environment.Exit(2);
	}

	WFDB_SiginfoArray siarray = new WFDB_SiginfoArray(nsig);
	
	wfdb.isigopen(record, siarray.cast(), nsig);
	WFDB_SampleArray v = new WFDB_SampleArray(nsig);		

	while (wfdb.getvec(v.cast()) > 0) {
	    Console.Write(n);
	    for (int i=0; i < nsig; i++) {
		Console.Write("\t" + v.getitem(i));
	    }
	    Console.WriteLine();
	    n++;
	}
	
	wfdb.wfdbquit();
    }
    
    static void usage() {
	Console.WriteLine("Usage: rdsamp.exe -r record");
    }
}
