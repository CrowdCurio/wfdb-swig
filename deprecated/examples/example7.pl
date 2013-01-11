#!/usr/bin/perl
#
# File: example7.pl       I. Henry   March 30 2005
#
# Perl translation of example7.c from the WFDB Programmer's Guide
# 							   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

package wfdb;
use wfdb;

$nc = @ARGV - 3;
if ( @ARGV < 3 ) {
    print STDERR "usage: ", $0, " record start duration [ coefficients ...]\n";
    exit(1);
} 
if ($nc < 1) {
    $nc = 1;
    $c = 1.0;
} 
for ($i = 0; $i < $nc; $i++) {
    $c[$i] = $ARGV[$i+3];
}
exit(3) if (($nsig = isigopen($ARGV[0], undef, 0)) < 1);
$s = new wfdb::WFDB_SiginfoArray($nsig);
$v = new wfdb::WFDB_SampleArray($nsig);
exit(3) if (isigopen($ARGV[0], $s->cast(), $nsig) != $nsig);
if (isigsettime(strtim($ARGV[1])) < 0) {
    print strtim($ARGV[1]), "\n";
    exit(4);
}
if (($nsamp = strtim($ARGV[2])) < 1) {
    print STDERR $0, ": inappropriate value for duration\n";
    exit(5);
}
exit(6) if (osigopen("16l", $s->cast(), $nsig) != $nsig);
sample(0, 0);
for ($t = 0; $t < $nsamp && sample_valid(); $t++) {
    for ($j = 0; $j < $nsig; $j++) {
        for ($i = 0, $vv = 0.; $i < $nc; $i++) {
            $vv += $c[$i]*sample($j, $t+$i) if ($c[$i] != 0.);
	}
        $v->setitem($j, int($vv));
    }
    last if (putvec($v->cast()) < 0);    
}
newheader("out");
wfdbquit();
