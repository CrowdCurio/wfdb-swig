// File: rdann.java       I. Henry    February 18 2005
//
// Minimal WFDB annotator reader written in Java, based on rdann.c
//
// Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

import wfdb.*;

public class rdann {
    
    public static void main(String argv[]) {
	int stat;
	String record = null, annotator = null;
	
	if ( argv.length < 4 ) {
	    usage();
	    System.exit(2);
	}
		
	for (int i = 0; i < argv.length; i++) {
	    if (argv[i].equals("-r")) {
		record = argv[++i];
	    } else if (argv[i].equals("-a")) {
		annotator = argv[++i];
	    } else {
		usage();
	    }
	}
	
	if (record == null || annotator == null) {
	    usage();
	    System.exit(2);
	}
	
	WFDB_AnninfoArray aiarray = new WFDB_AnninfoArray(1);
	WFDB_Annotation annot = new WFDB_Annotation();

	WFDB_Anninfo ai = aiarray.getitem(0);
	ai.setName(annotator);
	ai.setStat(wfdb.WFDB_READ);
	aiarray.setitem(0, ai);
	
	stat = wfdb.annopen(record, aiarray.cast(), 1);
	if (stat < 0) {
	    usage();
	    System.exit(1);
	}
	
	while (wfdb.getann(0, annot) == 0) {	    
	    System.out.println(wfdb.mstimstr(-annot.getTime()) + "\t" +
			       annot.getTime() + "\t" + 
			       wfdb.annstr(annot.getAnntyp()) + "\t" + 
			       annot.getSubtyp() + "\t" + 
			       annot.getChan() + "\t" + 
			       annot.getNum() + "\t" +
			       // print the aux string, excluding the first
			       // char, which is the length of the string
			       (annot.getAux() == null ? "" :
				annot.getAux().substring(1)));
	}
	wfdb.wfdbquit();
    }

    public static void usage() {
	System.out.println("Usage: rdann -r record -a annotator");
    }
}
