Introduction
============

``rbco.rename`` provides a set of Python scripts to rename files in batch.

Install
=======

1. Install setuptools_.
2. Run:: 

       easy_install rbco.rename

This will install the renaming scripts mentioned in the following section.


Usage
=====

- rendel STR FILES
    
  Deletes the string STR from the names of all files in FILES.
    
- rendeln N FILES

  Deletes the N first characters from the names of all files in FILES.
    
- renlu FILES
    
  Renames all files in FILES performing the following operations:
    - replaces ' ' by '_';
    - replaces ' - ' and '- ' by '-';
    - lowercase the names;
    - remove leading and trailing spaces.
    
- renmp3 FILES
    
  Renames all files in FILES performing the following operations:
    - replaces all accentuated characters by their ASCII counterparts.
    - replaces '_' by ' ';
    - replaces ' - ' and '- ' by '-';
    - titlecase the names;
    - lowcase file extension;
    - remove leading and trailing spaces;
    - replace ' ' by '-' after the track number, if needed;
    - makes track numbers have always 2 digits.

- renid3 FILES

  USAGE: renid3 FILES

  Rename all FILES based on the ID3 tags and the FORMAT. Example of FORMAT:
  '%(tracknumber)s-%(artist)s-%(title)s.mp3'. Other tags can be specified: date, author,
  composer, performer, discnumber, album, etc.

  FORMAT is retrieved from the RBCO_RENAME_ID3_FORMAT environment 
  variable. If there's no such variable then a default format is used.        
    
    
- renpre PREFFIX FILES
    
  Renames all files in FILES adding PREFFIX in the beggining of the file name.
    
- renrep OLDSTR NEWSTR FILES
  
  Renames all files in FILES replacing OLDSTR by NEWSTR.
    
- rensuf SUFFIX FILES
    
  Renames all files in FILES adding SUFFIX in the end of the file name. File 
  extension is preserved.
    
- unhide FILES
    
  Unhides all hidden files in FILES.
  
- renremoveacc FILES
    
  Rename the FILES by replacing all accentuated characters by their ASCII counterparts.


.. References
   ==========
   
.. _setuptools: http://pypi.python.org/pypi/setuptools
