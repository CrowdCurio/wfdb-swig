/* 
File : wfdb.i		I. Henry	October 17 2001
			Last revised:	20 August 2010 (by I. Henry)

SWIG interface file for WFDB
_______________________________________________________________________________
wfdb-bindings: SWIG (www.swig.org) wrappers for the WFDB library. Allows for 
reading and writing annotated waveforms (time series data) from a variety of 
computer languages.
Copyright (C) 2010 Isaac C. Henry

This library is free software; you can redistribute it and/or modify it under
the terms of the GNU Library General Public License as published by the Free
Software Foundation; either version 2 of the License, or (at your option) any
later version.

This library is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Library General Public License for more
details.

You should have received a copy of the GNU Library General Public License along
with this library; if not, write to the Free Software Foundation, Inc., 59
Temple Place - Suite 330, Boston, MA 02111-1307, USA.

You may contact the author by e-mail (ihenry@physionet.org) or postal mail
(MIT Room E25-505A, Cambridge, MA 02139 USA).  For updates to this software,
please visit PhysioNet (http://www.physionet.org/).
_______________________________________________________________________________
*/

%module wfdb
%header %{
#include <wfdb/wfdb.h>
%}

%module(directors="1") wfdb

/* Structure definitions */
typedef struct  {
    char *fname;
    char *desc;
    char *units;
    WFDB_Gain gain;
    WFDB_Sample initval;
    WFDB_Group group;
    int fmt;
    int spf;
    int bsize;
    int adcres;
    int adczero;
    int baseline;
    long nsamp;
    int cksum;
} WFDB_Siginfo;
%ignore WFDB_siginfo;

typedef struct {
    double low;
    double high;
    double scale;
    char *sigtype;
    char *units;
    int caltype;
} WFDB_Calinfo;

%ignore WFDB_calinfo;

typedef struct  {
    char *name;    
    int stat;
} WFDB_Anninfo;
%ignore WFDB_anninfo;


typedef struct {
    WFDB_Time time;
    int anntyp;
    int subtyp;
    int chan;
    int num;
    char *aux;
} WFDB_Annotation;
%feature("director") WFDB_Annotation;
%ignore WFDB_ann;

%include carrays.i

%array_class(int, intArray);
%array_class(WFDB_Sample,    WFDB_SampleArray);
%array_class(WFDB_Siginfo,    WFDB_SiginfoArray);
%array_class(WFDB_Anninfo,    WFDB_AnninfoArray);
%array_class(WFDB_Annotation, WFDB_AnnotationArray);

%include wfdb/ecgcodes.h
%include wfdb/wfdb.h

#ifdef SWIGJAVA
%include wfdb-java/jwfdb.i
#endif

#ifdef SWIGPYTHON
%include wfdb-python/pywfdb.i
#endif

%inline %{

static int _nvsig;

int spy_nvsig() 
{
    return _nvsig;
}

static int _nsamps;

int spy_nsamps()
{
    return _nsamps;
}

FINT getvec2(WFDB_Sample *vector, int nsamples) 
{
    FINT r;
    int i=0,j;
    WFDB_Sample *tmpv;
    
    if ( nsamples < 1 ) nsamples = _nsamps;
    tmpv = (WFDB_Sample *)malloc(_nvsig * sizeof(WFDB_Sample));
  
    r = getvec(tmpv);
    while ( r > 0 && i<nsamples )  {
	for (j=0; j<_nvsig; j++) 
	    *(vector+i*_nvsig+j) = tmpv[j];
	i++;
	r = getvec(tmpv);
    }
    
    free(tmpv);
    
    return r;
}

FINT getvec2p(double *vector, int nsamples) 
{
    FINT r;
    int i=0,j;
    WFDB_Sample *tmpv;
    
    if  ( nsamples < 1 )
	nsamples = _nsamps;
    tmpv = (WFDB_Sample *) malloc( _nvsig * sizeof(WFDB_Sample) );
  
    r = getvec(tmpv);
    while ( r > 0 && i<nsamples )  {
	for (j=0; j<_nvsig; j++) 
	    *(vector+i*_nvsig+j) = aduphys(j,tmpv[j]);
	i++;
	r = getvec(tmpv);
    }
    
    free(tmpv);
    return r;
}

%}

