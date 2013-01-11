#!/usr/bin/perl
#
# file: psamples.pl		G. Moody	11 March 2006 	
#
# Perl translation of psamples.c from the WFDB Programmer's Guide 	

package wfdb;
use wfdb;

$siarray = new wfdb::WFDB_SiginfoArray(2);
if ($nsig = isigopen("100s", $siarray->cast(), 2) < 2) {
    exit(1);
}
$v = new wfdb::WFDB_SampleArray(2);
for ($i=0; $i < 10; $i++) {
    if (getvec($v->cast()) < 0) {
        exit(2);
    }
    print "\t", $v->getitem(0), "\t", $v->getitem(1), "\n";
}
