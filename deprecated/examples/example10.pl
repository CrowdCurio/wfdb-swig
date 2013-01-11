#!/usr/bin/perl
#
# File: example10.pl       I. Henry   March 29 2005
#
# Perl translation of example10.c from the WFDB Programmer's Guide
# 							   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

package wfdb;
use wfdb;
use integer; # note: force integer arithmetic

$time = $maxslope = $nslope = $scmin = 0;
if ( @ARGV < 1 ) {
    print STDERR "usage: ", $0, " record [threshold]\n";
    exit(1);
} 
$a = new wfdb::WFDB_Anninfo;
$a->{name} = "qrs"; $a->{stat}= $WFDB_WRITE;

exit(2) if (($nsig = isigopen($ARGV[0], undef, 0)) < 1);
$s = new wfdb::WFDB_SiginfoArray($nsig);
$v = new wfdb::WFDB_SampleArray($nsig);
exit(2) if (wfdbinit($ARGV[0], $a, 1, $s->cast(), $nsig) != $nsig);
setifreq(250.) if (sampfreq(undef) < 240. || sampfreq(undef) > 260.);
$scmin = muvadu(0, $ARGV[1]) if (@ARGV > 1);
$scmin = muvadu(0, 1000) if ($scmin < 1);
$slopecrit = $scmax = 10 * $scmin;
$ms160 = strtim("0.16"); $ms200 = strtim("0.2"); $s2 = strtim("2");
$annot = new wfdb::WFDB_Annotation;
$annot->{subtyp} = $annot->{chan} = $annot->{num} = 0; $annot->{aux} = undef;
getvec($v->cast());
$t9 = $t8 = $t7 = $t6 = $t5 = $t4 = $t3 = $t2 = $t1 = $v->getitem(0);

do {
    $filter = ($t0 = $v->getitem(0)) + 4*$t1 + 6*$t2 + 4*$t3 + $t4
             - $t5                   - 4*$t6 - 6*$t7 - 4*$t8 - $t9;
    if ($time % $s2 == 0) {
	if ($nslope == 0) {
	    $slopecrit -= $slopecrit >> 4;
	    $slopecrit = $scmin if ($slopecrit < $scmin);
	}
	elsif ($nslope >= 5) {
	    $slopecrit += $slopecrit >> 4;
	    $slopecrit = $scmax if ($slopecrit > $scmax);
	}
    }
    if ($nslope == 0 && abs($filter) > $slopecrit) {
	$nslope = 1; $maxtime = $ms160;
	$sign = ($filter > 0) ? 1 : -1;
	$qtime = $time;
    }
    if ($nslope != 0) {
	if ($filter * $sign < -$slopecrit) {
	    $sign = -$sign;
	    $maxtime = (++$nslope > 4) ? $ms200 : $ms160;
	}
	elsif ($filter * $sign > $slopecrit &&
	       abs($filter) > $maxslope) {
	    $maxslope = abs($filter);
	}
	if ($maxtime-- < 0) {
	    if (2 <= $nslope && $nslope <= 4) {
		$slopecrit += (($maxslope >> 2) - $slopecrit)  >> 3;
		if ($slopecrit < $scmin) {$slopecrit = $scmin}
		elsif ($slopecrit > $scmax) {$slopecrit = $scmax}
		$annot->{time} = strtim("i") - ($time - $qtime) - 4;
		$annot->{anntyp} = $NORMAL; putann(0, $annot);
		$time = 0;
	    }
	    elsif ($nslope >= 5) {
		$annot->{time} = strtim("i") - ($time - $qtime) - 4;
		$annot->{anntyp} = $ARFCT; putann(0, annot);
	    }
	    $nslope = 0;
	}
    }
    $t9 = $t8; $t8 = $t7; $t7 = $t6; $t6 = $t5; $t5 = $t4;
    $t4 = $t3; $t3 = $t2; $t2 = $t1; $t1 = $t0; $time++;
} while (getvec($v->cast()) > 0);


wfdbquit();
