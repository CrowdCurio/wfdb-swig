// File: example5.cs       I. Henry    February 18 2005
//
// C# translation of example5.c from the WFDB Programmer's Guide
//
// Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

using System;
using Wfdb;

public class example5 {
    static void Main(string[] argv) {
	int i, nsig;

	if (argv.Length < 1) {
	    Console.WriteLine("usage: example5 record");
	    // Unlike C programs, Java programs do not have any foolproof way
	    // to discover their own names, so the name is given as a constant
	    // above.  The command needed to run this program within a VM
	    // is platform-dependent and likely to be more complex.
	    Environment.Exit(1);
	}
	nsig = wfdb.isigopen(argv[0], null, 0);
	if (nsig < 1) Environment.Exit(2);
	WFDB_SiginfoArray s = new WFDB_SiginfoArray(nsig);

	if (wfdb.isigopen(argv[0], s.cast(), nsig) != nsig)
	    Environment.Exit(2);
	Console.WriteLine("Record {0}", argv[0]);
	Console.WriteLine("Starting time: {0}", wfdb.timstr(0));
	Console.WriteLine("Sampling frequency: {0} Hz",
			  wfdb.sampfreq(argv[0]));
	Console.WriteLine("{0} signals", nsig);
	for (i = 0; i < nsig; i++) {
	    WFDB_Siginfo s_i_ = s.getitem(i);
	    Console.WriteLine("Group {0}, Signal {1}:", s_i_.group, i);
	    Console.WriteLine(" File: {0}", s_i_.fname);
	    Console.WriteLine(" Description: {0}", s_i_.desc);
	    Console.Write(" Gain: ");
	    if ( s_i_.gain == 0.0 )
		Console.Write("uncalibrated; assume {0}", wfdb.WFDB_DEFGAIN);
	    else Console.Write(s_i_.gain);
	    Console.WriteLine(" adu/{0}",
			      (s_i_.units != null ? s_i_.units : "mV"));
	    Console.WriteLine(" Initial value: {0}", s_i_.initval);
	    Console.WriteLine(" Storage format: {0}", s_i_.fmt);
	    Console.Write(" I/O: ");
	    if (s_i_.bsize == 0) Console.WriteLine("can be unbuffered");
	    else Console.WriteLine("{0}-byte blocks", s_i_.bsize);
	    Console.WriteLine(" ADC resolution: {0} bits", s_i_.adcres);
	    Console.WriteLine(" ADC zero: {0}", s_i_.adczero);
	    if (s_i_.nsamp > 0) {
		Console.WriteLine(" Length: {0} ({1} sample intervals)", 
				  wfdb.timstr(s_i_.nsamp), s_i_.nsamp);
		Console.WriteLine(" Checksum: {0}", s_i_.cksum);
	    }	
	    else Console.WriteLine(" Length undefined");
	}
	wfdb.wfdbquit();
    }
}
