/* Javadoc comments for wfdb functions 
 
   Please see SWIG manual for more info:
   http://www.swig.org/Doc1.3/Java.html#javadoc_comments
 */

%typemap(javaimports) WFDB_Siginfo "
/**
 * javadoc comment here 
 */"

%typemap(javaimports) WFDB_SiginfoArray "
/**
 * javadoc comment here 
 */"

%typemap(javaimports) WFDB_Calinfo "
/**
 * javadoc comment here 
 */"

%typemap(javaimports) WFDB_Anninfo "
/**
 * javadoc comment here 
 */"

%typemap(javaimports) WFDB_AnninfoArray "
/**
 * javadoc comment here 
 */"

%typemap(javaimports) WFDB_Annotation "
/** 
 * javadoc comment here 
 */"

%javamethodmodifiers annopen(char *record, WFDB_Anninfo* aiarray, unsigned int nann) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers isigopen(char *record, WFDB_Siginfo* siarray, int nsig) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers osigopen(char *record, WFDB_Siginfo* siarray, unsigned int nsig) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers osigfopen(WFDB_Siginfo* siarray, unsigned int nsig) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers wfdbinit(char *record, WFDB_Anninfo *aiarray, unsigned int nann, WFDB_Siginfo* siarray, unsigned int nsig) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers getspf(void) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers setgvmode(int mode) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers getvec(WFDB_Sample *vector) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers getframe(WFDB_Sample *vector) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers putvec(WFDB_Sample *vector) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers getann(WFDB_Annotator a, WFDB_Annotation *annot) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers ungetann(WFDB_Annotator a, WFDB_Annotation *annot) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers putann(WFDB_Annotator a, WFDB_Annotation *annot) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers isigsettime(WFDB_Time t) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers isgsettime(WFDB_Group g, WFDB_Time t) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers iannsettime(WFDB_Time t) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers ecgstr(int annotation_code) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers strecg(char *annotation_mnemonic_string) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers setecgstr(int annotation_code, char *annotation_mnemonic_string) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers annstr(int annotation_code) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers strann(char *annotation_mnemonic_string) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers setannstr(int annotation_code, char *annotation_mnemonic_string) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers anndesc(int annotation_code) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers setanndesc(int annotation_code, char *annotation_description) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers iannclose(WFDB_Annotator a) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers oannclose(WFDB_Annotator a) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers timstr(WFDB_Time t) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers mstimstr(WFDB_Time t) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers strtim(char *time_string) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers datstr(WFDB_Date d) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers strdat(char *date_string) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers adumuv(WFDB_Signal s, WFDB_Sample a) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers muvadu(WFDB_Signal s, int microvolts) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers aduphys(WFDB_Signal s, WFDB_Sample a) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers physadu(WFDB_Signal s, double v) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers calopen(char *calibration_filename) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers getcal(char *description, char *units, WFDB_Calinfo *cal) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers putcal(WFDB_Calinfo *cal) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers newcal(char *calibration_filename) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers flushcal(void) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers getinfo(char *record) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers putinfo(char *info) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers newheader(char *record) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers setheader(char *record, WFDB_Siginfo* siarray, unsigned int nsig) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers setmsheader(char *record, char **seg_names, unsigned int nsegments) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers wfdbgetskew(WFDB_Signal s) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers wfdbsetskew(WFDB_Signal s, int skew) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers wfdbgetstart(WFDB_Signal s) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers wfdbsetstart(WFDB_Signal s, long bytes) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers wfdbquit(void) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers sampfreq(char *record) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers setsampfreq(WFDB_Frequency sampling_frequency) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers getcfreq(void) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers setcfreq(WFDB_Frequency counter_frequency) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers getbasecount(void) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers setbasecount(double count) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers setbasetime(char *time_string) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers wfdbquiet(void) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers wfdbverbose(void) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers wfdberror(void) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers setwfdb(char *database_path_string) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers getwfdb(void) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers setibsize(int input_buffer_size) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers setobsize(int output_buffer_size) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers wfdbfile(char *file_type, char *record) "
 /**
  * javadoc comment here 
  */
  public";

%javamethodmodifiers wfdbflush(void) "
 /**
  * javadoc comment here 
  */
  public";
