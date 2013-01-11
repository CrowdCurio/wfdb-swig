#!/usr/bin/perl
#
# File: example6.pl       I. Henry   March 30 2005
#
# Perl translation of example6.c from the WFDB Programmer's Guide
# 						   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

package wfdb;
use wfdb;

$nsamp = 1000;
if ( @ARGV < 1 ) {
    print STDERR "usage: ", $0, " record\n";
    exit(1);
} 
exit(2) if (($nsig = isigopen($ARGV[0], undef, 0)) <= 0);
$s = new wfdb::WFDB_SiginfoArray($nsig);
$vin = new wfdb::WFDB_SampleArray($nsig);
$vout = new wfdb::WFDB_SampleArray($nsig);
exit(2) if (isigopen($ARGV[0], $s->cast(), $nsig) != $nsig);
exit(3) if (osigopen("8l", $s->cast(), $nsig) <= 0);
while ($nsamp-- > 0 && getvec($vin->cast()) > 0) {
    for ($i = 0; $i < $nsig; $i++) {
	$vout->setitem($i, $vout->getitem($i)-$vin->getitem($i));
    }
    last if (putvec($vout->cast()) < 0);
    for ($i = 0; $i < $nsig; $i++) {
	$vout->setitem($i, $vin->getitem($i));
    }    
}
newheader("dif");
wfdbquit();
