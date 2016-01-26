// File: example1.cs       I. Henry    March 30 2005
//
// C# translation of example1.c from the WFDB Programmer's Guide
//
// Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

using System;
using Wfdb;

public class example1 {
	
    static void Main(string[] argv) {
		
	WFDB_AnninfoArray an = new WFDB_AnninfoArray(2);
	string record = null, iann = null, oann = null;
	WFDB_Annotation annot =  new WFDB_Annotation();

	Console.Write("Type record name: ");
	record = Console.ReadLine();
	Console.Write("Type input annotator name: ");
	iann = Console.ReadLine();
	Console.Write("Type output annotator name: ");
	oann = Console.ReadLine();
	
	WFDB_Anninfo a = an.getitem(0);
	a.name = iann; a.stat =wfdb.WFDB_READ;
	an.setitem(0,a);
	a = an.getitem(1);
	a.name = oann; a.stat = wfdb.WFDB_WRITE;
	an.setitem(1,a);
	
	if ( wfdb.annopen(record, an.cast(), 2) < 0 ) Environment.Exit(1);
	while ( wfdb.getann(0, annot) == 0) {
	    if ( wfdb.wfdb_isqrs(annot.anntyp) != 0 ) {
		// Note that C# cannot cast an int (such as that returned by
		// isqrs) to a boolean, so omitting the comparison to 0, as in
		// other translations of this code, does not work in this case.
		annot.anntyp = wfdb.NORMAL;
		if ( wfdb.putann(0, annot) < 0) break;
	    }
	}

	wfdb.wfdbquit();
    }
}
