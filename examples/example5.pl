#!/usr/bin/perl
#
# File: example5.pl       I. Henry   March 30 2005
#
# Perl translation of example5.c from the WFDB Programmer's Guide
#						   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

package wfdb;
use wfdb;

if ( @ARGV < 1 ) {
    print STDERR "usage: ", $0, " record\n";
    exit(1);
} 

exit(2) if (($nsig = isigopen($ARGV[0], undef, 0)) < 1);
$s = new wfdb::WFDB_SiginfoArray($nsig);
exit(2) if (isigopen($ARGV[0], $s->cast(), $nsig) != $nsig);
print "Record ", $ARGV[0], "\n";
print "Starting time: ", timstr(0), "\n";
print "Sampling frequency: ", sampfreq($ARGV[0]), " Hz\n";
print $nsig, " signals\n";
for ($i = 0; $i < $nsig; $i++) {
    $s_i_ = $s->getitem($i);
    print "Group ", $s_i_->{group}, ", Signal ", $i, ":\n";
    print " File: ", $s_i_->{fname}, "\n";
    print " Description: ", $s_i_->{desc}, "\n";
    print " Gain: ";
    if ($s_i_->{gain} == 0.) {
        print "uncalibrated; assume ", $WFDB_DEFGAIN;
    } else {
	printf $s_i_->{gain};
    }
    print " adu/", $s_i_->{units} ? $s_i_->{units} : "mV", "\n";
    print " Initial value: ", $s_i_->{initval}, "\n";
    print " Storage format: ", $s_i_->{fmt}, "\n";
    print " I/O: ";
    if ($s_i_->{bsize} == 0) { 
	print "can be unbuffered\n";
    } else { 
	print  $s_i_->{bsize}, "-byte blocks\n"; 
    }
    print " ADC resolution: ", $s_i_->{adcres}, " bits\n";
    print " ADC zero: ", $s_i_->{adczero}, "\n";
    if ($s_i_->{nsamp} > 0) {
        print " Length: ", timstr($s_i_->{nsamp}), 
	      " (", $s_i_->{nsamp}, " sample intervals)\n";
        print " Checksum: ", $s_i_->{cksum}, "\n";
    } else { 
	print " Length undefined\n";
    }
}

wfdbquit();
