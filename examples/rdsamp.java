// File: rdsamp.java       I. Henry    February 16 2005
//
// Minimal WFDB sample reader written Java, based on rdsamp.c
//
// Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

import wfdb.*;

public class rdsamp {

    public static void main(String argv[]) {

	String record = null;

	if (argv.length < 2) {
	    usage();
	    System.exit(2);
	}

	for (int i = 0; i < argv.length; i++) {
	    if (argv[i].equals("-r")) {
		record = argv[++i];
	    } else {
		usage();
	    }
	}

	if (record == null) {
	    usage();
	    System.exit(2);
	}

	int nsig, n=0;	    
	nsig = wfdb.isigopen(record, null, 0);
	    
	if (nsig <= 0) {
	    usage();
	    System.exit(2);
	}

	WFDB_SiginfoArray siarray = new WFDB_SiginfoArray(nsig);
	
	wfdb.isigopen(record, siarray.cast(), nsig);
	WFDB_SampleArray v = new WFDB_SampleArray(nsig);

	while (wfdb.getvec(v.cast()) > 0) {
	    System.out.print(n);
	    for (int i=0; i < nsig; i++) {
		System.out.print("\t" + v.getitem(i));
	    }
	    System.out.println();
	    n++;
	}
	
	wfdb.wfdbquit();

    }

    public static void usage() {
	System.out.println("Usage: rdsamp -r record");
    }

}
