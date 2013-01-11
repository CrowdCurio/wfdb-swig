#!/usr/bin/perl
#
# File: example9.pl       I. Henry   March 30 2005
#
# Perl translation of example9.c from the WFDB Programmer's Guide
# 							   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

package wfdb;
use wfdb;

$nbeats = 0;
$stoptime = 0;
$a = new wfdb::WFDB_Anninfo();
$annot = new wfdb::WFDB_Annotation();

if (@ARGV < 2) {
    print STDERR "usage: ", $0, " annotator record [beat-type from to]\n";
    exit(1);
}
$a->{name} = $ARGV[0]; $a->{stat} = $WFDB_READ;
exit(2) if (($nsig = isigopen($ARGV[1], undef, 0)) < 1);
$s = new wfdb::WFDB_SiginfoArray($nsig);
$v = new wfdb::WFDB_SampleArray($nsig);
$vb = new wfdb::WFDB_SampleArray($nsig);
exit(3) if (wfdbinit($ARGV[1], $a, 1, $s->cast(), $nsig) != $nsig);
$hwindow = strtim(".05"); $window = 2*$hwindow + 1;
$s_0_ = $s->getitem(0);
# how do i init matrix ?!?! not really necessary?
# @sum = [[0] x $window] x $nsig;
$btype = (@ARGV > 2) ? strann($ARGV[2]) : $NORMAL;
iannsettime(strtim($ARGV[3])) if (@ARGV > 3);
if (@ARGV > 4) {
    if (($stoptime = strtim($ARGV[4])) < 0) {
	$stoptime = -$stoptime;
    }
    if ($s_0_->{nsamp} > 0 && $stoptime > $s_0_->{nsamp}) {
	$stoptime = $s_0_->{nsamp};
    }
} else { 
    $stoptime = $s_0_->{nsamp}; 
}
$stoptime -= $hwindow if ($stoptime > 0);
L: goto L while (getann(0, $annot) == 0 && $annot->{time} < $hwindow);
do {
    if ($annot->{anntyp} == $btype) {
	isigsettime($annot->{time} - $hwindow - 1);
	getvec($vb->cast());
	for ($j = 0; $j < $window && getvec($v->cast()) > 0; $j++) {
	    for ($i = 0; $i < $nsig; $i++) {
		$sum[$i][$j] += $v->getitem($i) - $vb->getitem($i);
	    }
	}
	$nbeats++;
    }
} while (getann(0, $annot) == 0 &&
	 (stoptime == 0 || $annot->{time} < $stoptime));
if ($nbeats < 1) {
    print STDERR $0, ": no `", annstr($btype), "' beats found\n";
    exit(4);
}
print "Average of ", $nbeats, " `", annstr($btype), "' beats:\n";
for ($j = 0; $j < $window; $j++) {
    for ($i = 0; $i < $nsig; $i++) {
	printf("%g%s", $sum[$i][$j]/$nbeats, (($i == $nsig-1) ? "\n" : "\t"));
    }
}

wfdbquit();
