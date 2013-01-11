#!/bin/sh

if [ -s configure -a configure -nt configure.ac ]
then
    echo 'configure is up-to-date'
else
    aclocal -Im4
    automake
    autoconf
    echo 'configure is up-to-date'
fi
