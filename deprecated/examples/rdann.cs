// File: rdann.cs       I. Henry    February 18 2005
//
// Minimal WFDB annotator reader written in C#, based on rdann.c
//
// Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

using System;
using Wfdb;

public class rdann {

    static void Main(string[] argv) {
	int stat;
	String record = null, annotator = null;
	
	if (argv.Length < 4) {
	    usage();
	    Environment.Exit(2);
	}
		
	for (int i = 0; i < argv.Length; i++) {
	    if (argv[i] == "-r") {
		record = argv[++i];
	    } else if (argv[i] == "-a") {
		annotator = argv[++i];
	    } else {
		usage();
	    }
	}
	
	if (record == null || annotator == null) {
	    usage();
	    Environment.Exit(2);
	}
	
	WFDB_AnninfoArray aiarray = new WFDB_AnninfoArray(1);
	WFDB_Anninfo ai = new WFDB_Anninfo();
	WFDB_Annotation annot = new WFDB_Annotation();
	
	ai.name = annotator;
	ai.stat = wfdb.WFDB_READ;
	aiarray.setitem(0,ai);
	
	stat = wfdb.annopen(record, aiarray.cast(), 1);
	if (stat < 0) {
	    usage();
	    Environment.Exit(2);
	}
	
	while (wfdb.getann(0, annot) == 0 ) {
	    Console.WriteLine(wfdb.mstimstr(-annot.time) + "\t" +
			      annot.time + "\t" + 
			      wfdb.annstr(annot.anntyp) + "\t" + 
			      annot.subtyp + "\t" + 
			      annot.chan + "\t" + 
			      annot.num + "\t" +
			      // print the aux string, excluding the first
			      // char, which is the length of the string
			      (annot.aux == null ? "" : 
			       annot.aux.Substring(1)));
	}

	wfdb.wfdbquit();
    }
    
    static void usage() {
	Console.WriteLine("Usage: rdann -r record -a annotator");
    }
}
