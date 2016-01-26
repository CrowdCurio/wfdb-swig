#!/usr/bin/perl
#
# File: example4.pl       I. Henry   March 29 2005
#
# WFDB Example 4: Generating an R-R Interval Histogram
#
# see http://physionet.org/physiotools/wpg/wpg_144.htm#SEC144
# 						   
# Copyright (C) 2005 Isaac C. Henry (ihenry@physionet.org)

package wfdb;
use wfdb;

$a = new wfdb::WFDB_Anninfo();
$annot = new wfdb::WFDB_Annotation();
if ( @ARGV < 2 ) {
    print STDERR "usage: ", $0, " annotator record\n";
    exit(1);
} 
$a->{name} = $ARGV[0]; $a->{stat} = $WFDB_READ;
exit(2) if (annopen($ARGV[1], $a, 1) < 0);
exit(3) if (($rrmax = 3*sampfreq($ARGV[1])) <= 0);
$i=0; $rrhist[$i++] = 0 while ($i<=$rrmax);
L: goto L while (getann(0, $annot) == 0 && ! wfdb_isqrs($annot->{anntyp}));
$t = $annot->{time};
while (getann(0, $annot) == 0) {
    if (wfdb_isqrs($annot->{anntyp})) {
	if (($rr = $annot->{time} - $t) > $rrmax) { $rr = $rrmax }
	$rrhist[$rr]++;
	$t = $annot->{time};
    }
}
for ($rr = 1; $rr < $rrmax; $rr++) {
    printf("%4d %s\n", $rrhist[$rr], mstimstr($rr));
}
printf("%4d %s (or longer)\n", $rrhist[$rr], mstimstr($rr));

wfdbquit();
