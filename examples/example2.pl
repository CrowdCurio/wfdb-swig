#!/usr/bin/perl 
#
# File: example2.pl       I. Henry   March 29 2005
#
# Perl translation of example2.c from the WFDB Programmer's Guide
#				   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

package wfdb;
use wfdb;

$an = new wfdb::WFDB_AnninfoArray(2);
$annot = new wfdb::WFDB_Annotation;
if ( @ARGV < 1 ) {
    print STDERR "usage: ", $0, " record\n";
    exit(1);
}
$a = $an->getitem(0);
$a->{name} = "atr"; $a->{stat} = $WFDB_READ;
$an->setitem(0,$a);
$a = $an->getitem(1);
$a->{name} = "aha"; $a->{stat} = $WFDB_AHA_WRITE; 
$an->setitem(1,$a);
exit(2) if (annopen($ARGV[0], $an->cast(), 2) < 0);
L: goto L while (getann(0, $annot) == 0 && putann(0, $annot) == 0);
wfdbquit();
