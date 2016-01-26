// File: example10.cs       I. Henry          February 18 2005
//			    Last revised:	6 April 2006
// C# translation of example10.c from the WFDB Programmer's Guide
//
// Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

using System;
using Wfdb;

public class example10 {
	
    static void Main(string[] argv) {
	int filter, time=0, slopecrit, sign=1, maxslope=0, nsig, nslope=0,
	    qtime=0, maxtime=0, t0, t1, t2, t3, t4, t5, t6, t7, t8, t9,
	    ms160, ms200, s2, scmax, scmin = 0;
	WFDB_Anninfo a = new WFDB_Anninfo();
	WFDB_Annotation annot = new WFDB_Annotation();

	if (argv.Length < 1) {
	    Console.WriteLine("usage: example10 record [threshold]");
	    // Unlike C programs, C# programs do not have any foolproof way
	    // to discover their own names, so the name is given as a constant
	    // above.  The command needed to run this program within a VM
	    // is platform-dependent and likely to be more complex.
	    Environment.Exit(1);
	}
	a.name = "qrs"; a.stat = wfdb.WFDB_WRITE;
		
	if ((nsig = wfdb.isigopen(argv[0], null, 0)) < 1)
	    Environment.Exit(2);
	WFDB_SiginfoArray s = new WFDB_SiginfoArray(nsig);
	WFDB_SampleArray v = new WFDB_SampleArray(nsig);
	if (wfdb.wfdbinit(argv[0], a, 1, s.cast(), (uint)nsig) != nsig)
	    Environment.Exit(2);
	if (wfdb.sampfreq(null) < 240.0 || wfdb.sampfreq(null) > 260.0)
	    wfdb.setifreq(250.0);
	if (argv.Length > 1) scmin = wfdb.muvadu(0, Int16.Parse(argv[1]));
	if (scmin < 1) scmin = wfdb.muvadu(0, 1000);
	slopecrit = scmax = 10 * scmin;
	ms160 = wfdb.strtim("0.16"); ms200 = wfdb.strtim("0.2");
	s2 = wfdb.strtim("2");
	annot.subtyp = 0; annot.chan = 0; annot.num = 0; annot.aux = null;
	wfdb.getvec(v.cast());
	t9 = t8 = t7 = t6 = t5 = t4 = t3 = t2 = t1 = v.getitem(0);
		
	do {
	    filter = (t0 = v.getitem(0)) + 4*t1 + 6*t2 + 4*t3 + t4
		            - t5         - 4*t6 - 6*t7 - 4*t8 - t9;
	    if (time % s2 == 0) {
		if (nslope == 0) {
		    slopecrit -= slopecrit >> 4;
		    if (slopecrit < scmin) slopecrit = scmin;
		}
		else if (nslope >= 5) {
		    slopecrit += slopecrit >> 4;
		    if (slopecrit > scmax) slopecrit = scmax;
		}
	    }
	    if (nslope == 0 && Math.Abs(filter) > slopecrit) {
		nslope = 1; maxtime = ms160;
		sign = (filter > 0) ? 1 : -1;
		qtime = time;
	    }
	    if (nslope != 0) {
		if (filter * sign < -slopecrit) {
		    sign = -sign;
		    maxtime = (++nslope > 4) ? ms200 : ms160;
		}
		else if (filter * sign > slopecrit &&
			 Math.Abs(filter) > maxslope)
		    maxslope = Math.Abs(filter);
		if (maxtime-- < 0) {
		    if (2 <= nslope && nslope <= 4) {
			slopecrit += ((maxslope>>2) - slopecrit) >> 3;
			if (slopecrit < scmin) slopecrit = scmin;
			else if (slopecrit > scmax) slopecrit = scmax;
			annot.time = wfdb.strtim("i") - (time - qtime) - 4;
			annot.anntyp = wfdb.NORMAL; wfdb.putann(0, annot);
			time = 0;
		    }
		    else if (nslope >= 5) {
			annot.time = wfdb.strtim("i") - (time - qtime) - 4;
			annot.anntyp = wfdb.ARFCT; wfdb.putann(0, annot);
		    }
		    nslope = 0;
		}
	    }
	    t9 = t8; t8 = t7; t7 = t6; t6 = t5; t5 = t4;
	    t4 = t3; t3 = t2; t2 = t1; t1 = t0; time++;
	} while (wfdb.getvec(v.cast()) > 0);

	wfdb.wfdbquit();		
    }
}
