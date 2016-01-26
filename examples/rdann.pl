#!/usr/bin/perl
#
# File: rdann.pl       I. Henry   March 29 2005
#
# Minimal WFDB annotator reader written in Perl, based on rdann.c
# 							   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

package wfdb;
use wfdb;

if ( @ARGV < 4 ) {
    usage();
    exit;
} 

# parse the arguments
for ( $i=0; $i<@ARGV; $i++ ) {
    if ( $ARGV[$i] =~ m/\-r/ ) {
	$record = $ARGV[++$i];
    }
    elsif ( $ARGV[$i] =~ m/\-a/ ) {
	$annotator = $ARGV[++$i];
    }
    else {
	usage();
	exit;
    }
}

if ( ! $record || ! $annotator ) {
	usage();
	exit(2);
}

# set the sampling frequency
if ( ($sps = sampfreq($record)) < 0.) {
	setsampfreq($sps = $WFDB_DEFFREQ);
}

# get a new anninfo object
$aiarray = new wfdb::WFDB_AnninfoArray(1);

# set ai fields
$ai = $aiarray->getitem(0);
%$ai = ( name => $annotator,
	 stat => $WFDB_READ );
# this is also equivalent to
# $ai->{name} = $annotator;
# $ai->{stat} = $WFDB_READ;

# put the ai in the array
$aiarray->setitem(0,$ai);

# open the annotations
$result = annopen( $record, $aiarray->cast(), 1 );

if ( $result < 0 ) {
	usage();
	exit(2);
}

# get a new annotation object
$annot = new wfdb::WFDB_Annotation();

while ( getann(0, $annot) == 0 ) {    
    print mstimstr(-$annot->{time}), "\t",
    $annot->{time}, "\t",
    annstr( $annot->{anntyp} ), "\t",
    $annot->{subtyp}, "\t",
    $annot->{chan}, "\t",
    $annot->{num}, "\t",
    substr($annot->{aux}, 1), "\n";
}

wfdbquit();

sub usage {
    print STDERR "Usage: rdann.pl -r record -a annotator\n";
}
