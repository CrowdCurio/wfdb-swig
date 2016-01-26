#!/usr/bin/perl 
#
# File: example1.pl       I. Henry   March 29 2005
#
# Perl translation of example1.c from the WFDB Programmer's Guide
# 
# see http://physionet.org/physiotools/wpg/wpg_141.htm#SEC141
#  							   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

package wfdb;
use wfdb;

$an = new wfdb::WFDB_AnninfoArray(2);
$annot = new wfdb::WFDB_Annotation();
print "Type record name: ";
$record = <STDIN>; chomp($record);
print "Type input annotator name: ";
$iann = <STDIN>; chomp($iann);
print "Type output annotator name: ";
$oann = <STDIN>; chomp($oann);
$a = $an->getitem(0);
$a->{name} = $iann; $a->{stat} = $WFDB_READ;  
$an->setitem(0,$a);
$a = $an->getitem(1);
$a->{name} = $oann; $a->{stat} = $WFDB_WRITE; 
$an->setitem(1,$a);
exit (1) if (annopen($record, $an->cast(), 2) < 0);
while (getann(0, $annot) == 0) {
    if ( wfdb_isqrs($annot->{anntyp}) ) {
	$annot->{anntyp} = $NORMAL;
	last if (putann(0, $annot) < 0);
    }
}
wfdbquit();
