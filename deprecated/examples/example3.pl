#!/usr/bin/perl
#
# File: example3.pl       I. Henry   March 29 2005
#
# Perl translation of example3.c from the WFDB Programmer's Guide
#						   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

package wfdb;
use wfdb;

$a = new wfdb::WFDB_Anninfo();
$annot = new wfdb::WFDB_Annotation();
if ( @ARGV < 2 ) {
    print STDERR "usage: ", $0, " annotator record\n";
    exit(1);
} 
$a->{name} = $ARGV[0];
$a->{stat} = $WFDB_READ;
sampfreq($ARGV[1]);
exit(2) if (annopen($ARGV[1], $a, 1) < 0);
while (getann(0, $annot) == 0) {
    print timstr(-$annot->{time}), " (",
    $annot->{time}, ") ",
    annstr( $annot->{anntyp} ), " ",
    $annot->{subtyp}, " ",
    $annot->{chan}, " ",
    $annot->{num}, " ",
    substr($annot->{aux}, 1), "\n";
}
wfdbquit();
