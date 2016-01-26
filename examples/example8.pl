#!/usr/bin/perl
#
# File: example8.pl       I. Henry   March 30 2005
#
# Perl translation of example8.c from the WFDB Programmer's Guide
# 							   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

package wfdb;
use wfdb;

do {
    print "Choose a record name [up to 6 characters]: ";
    $record = <STDIN>; chomp($record);
} while (newheader($record) < 0);
do {
    print "Number of signals to be recorded [>0]: ";
    $nsig = <STDIN>; chomp($nsig);
} while ($nsig < 1);
$s = new wfdb::WFDB_SiginfoArray($nsig);
$v = new wfdb::WFDB_SampleArray($nsig);
do {
    print "Sampling frequency [Hz per signal, > 0]: ";
    $freq = <STDIN>; chomp($freq);
} while (setsampfreq($freq) < 0);
do {
    print "Length of record (H:M:S): ";
    $answer = <STDIN>; chomp($answer);
} while (($nsamp = strtim($answer)) < 1);
print "Directory for signal files [up to 30 characters]: ";
$directory = <STDIN>; chomp($directory);
print "Save signals in difference format? [y/n]: ";
$answer = <STDIN>; chomp($answer);
$s_0_ = $s->getitem(0);
$s_0_->{fmt} = ($answer[0] == 'y') ? 8 : 16;
$s->setitem(0,$s_0_);
print "Save all signals in one file? [y/n]: ";
$answer = <STDIN>; chomp($answer);
if ($answer[0] == 'y') {
    $filename[0] = $directory + "/d." + $record;
    for ($i = 0; $i < $nsig; $i++) {
	$s_i_ = $s->getitem($i);
	$s_i_->{fname} = $filename[0];
	$s_i_->{group} = 0;
	$s->setitem($i, $s_i_);
    }
} else {
    for ($i = 0; $i < $nsig; $i++) {
	$filename[$i] = $directory + "/d" + $i + "." + $record;
	$s_i_ = $s->getitem($i);
	$s_i_->{fname} = $filename[$i];
	$s_i_->{group} = $i;
	$s->setitem($i, $s_i_);
    }
}
for ($i = 0; $i < $nsig; $i++) {
    $s_i_ = $s->getitem($i);
    $s_i_->{fmt} = $s_0_->{fmt}; $s_i_->{bsize} = 0;
    printf "Signal ", $i, " description [up to 30 characters]: ";
    $description[$i] = <STDIN>; chomp($description[$i]);
    $s_i_->desc = $description[$i];
    print "Signal ", $i, " units [up to 20 characters]: ";
    $units[$i] = <STDIN>; chomp($units[$i]);
    $s_i_->{units} = $units[$i][0] ? $units[$i] : "mV";
    do {
	print " Signal ", $i, " gain [adu/", $s_i_->{units}, "]: ";
	$s_i_->{gain} = <STDIN>; chomp($s_i_->{gain});
    } while ($s_i_->{gain} < 0.);
    do {
	print " Signal ", $i, " ADC resolution in bits [8-16]: ";
	$s_i_->{adcres} = <STDIN>; chomp($s_i_->{adcres});
    } while ($s_i_->{adcres} < 8 || $s_i_->{adcres} > 16);
    print " Signal ", $i, " ADC zero level [adu]: ";
    $s_i_->{adczero} = <STDIN>; chomp($s_i_->{adczero});
    $s->setitem($i, $s_i_);
}
exit(1) if (osigfopen($s->cast(), $nsig) < $nsig);
print "To begin sampling, press RETURN;  to specify a\n";
print " start time other than the current time, enter\n";
print " it in H:M:S format before pressing RETURN: ";
$answer = <STDIN>; chomp($answer);
setbasetime($answer);
adinit();
for ($t = 0; $t < $nsamp; $t++) {
    for ($i = 0; $i < $nsig; $i++) {
	$v->setitem($i, adget($i));
    }
    last if (putvec($v->cast()) < 0);
}
adquit();
newheader($record);
wfdbquit();


sub adinit() { print timstr(0), "\n"; }

sub adget($i)
{
    return ($i);
}

sub adquit() { ; }


