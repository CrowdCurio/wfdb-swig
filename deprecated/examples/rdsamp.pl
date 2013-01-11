#!/usr/bin/perl
#
# File: rdsamp.pl       I. Henry   March 29 2005
#
# Minimal WFDB sample reader written in Perl, based on rdsamp.c
# 							   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)


package wfdb;
use wfdb;

if ( @ARGV < 2 ) {
    usage();
    exit;
} 

# parse the arguments
for ($i=0; $i<@ARGV; $i++ ) {
    if ( $ARGV[$i] =~ m/\-r/ ) {
	$record = $ARGV[++$i];
    }
    else {
	usage();
	exit;
    }
}

if ( ! $record ) {
    usage();
    exit(2);
}

$nsig = isigopen($record, undef, 0);

if ( $nsig < 1 ) {
    usage();
    exit(2);
} 

$siarray = new wfdb::WFDB_SiginfoArray($nsig);
$nsig = isigopen($record, $siarray->cast(), $nsig);

$n = 0;

$v = new wfdb::WFDB_SampleArray($nsig);
while ( getvec($v->cast()) > 0 ) {
    print $n;
    for ($i=0; $i < $nsig; $i++) {
    	print "\t", $v->getitem($i);
    }
    print "\n";
    $n++;
}

wfdbquit();

sub usage {
    print STDERR "Usage: rdsamp.pl -r record\n";
}
