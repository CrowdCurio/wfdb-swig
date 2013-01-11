// file: psamples.java		G. Moody	11 March 2006 	
//
// Java translation of psamples.c from the WFDB Programmer's Guide

import wfdb.*;

public class psamples {

    public static void main(String argv[]) {
        WFDB_SiginfoArray siarray = new WFDB_SiginfoArray(2);
        if (wfdb.isigopen ("100s", siarray.cast(), 2) < 2)
            System.exit(1);
        WFDB_SampleArray v = new WFDB_SampleArray(2);
        for (int i = 0; i < 10; i++) {
            if (wfdb.getvec(v.cast()) < 0)
                break;
            System.out.println("\t" + v.getitem(0) + "\t" + v.getitem(1));
        }
    }
}
