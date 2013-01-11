// file: psamples.cs		G. Moody	5 April 2006
//
// C# translation of psamples.c from the WFDB Programmer's Guide 	

using System;
using Wfdb;

public class psamples {
    static void Main(string[] argv) {
        WFDB_SiginfoArray siarray = new WFDB_SiginfoArray(2);
        if (wfdb.isigopen("100s", siarray.cast(), 2) < 2)
            Environment.Exit(1);
        WFDB_SampleArray v = new WFDB_SampleArray(2);
        for (int i = 0; i < 10; i++) {
            if (wfdb.getvec(v.cast()) < 0)
                break;
	    Console.WriteLine("\t" + v.getitem(0) + "\t" + v.getitem(1));
        }
    }
}
