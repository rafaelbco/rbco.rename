#coding=utf8
import os
import sys
import renaming
import os.path
import re

def unhide():
    """
    Usage: unhide FILES
    
    Unhides all hidden files in FILES.
    """
    files = sys.argv

    for f in files:
        renaming.unhide(f)

def rensuf():
    """
    Usage: rensuf SUFFIX FILES
    
    Renames all files in FILES adding SUFFIX in the end of the file name. File 
    extension is preserved.
    """
    s = sys.argv[1]
    files = sys.argv[2:]
    
    renaming.rename_suffix(files, s)            
    
def renrep():
    """
    Usage: renrep OLDSTR NEWSTR FILES
    
    Renames all files in FILES replacing OLDSTR by NEWSTR.
    """
    old = sys.argv[1]
    new = sys.argv[2]
    files = sys.argv[3:]
    
    renaming.rename_replace(files, old, new)
    
        
def renpre():
    """
    Usage: renpre PREFFIX FILES
    
    Renames all files in FILES adding PREFFIX in the beggining of the file name. 
    File extension is preserved.
    """
    s = sys.argv[1]
    files = sys.argv[2:]
    
    renaming.rename_prefix(files, s)        

def renmp3():
    """
    Usage: renmp3 FILES
    
    Renames all files in FILES performing the following operations:
    - replaces all accentuated characters by their ASCII counterparts (Eg.: 
      "É Fácil.mp3" -> "E Facil.mp3").    
    - replaces '_' by ' ';
    - replaces ' - ' and '- ' by '-';
    - titlecase the names;
    - lowcase file extension;
    - remove leading and trailing spaces;
    - replace ' ' by '-' after the track number, if needed;
    - makes track numbers have always 2 digits.
    """
    files = sys.argv[1:]
    renaming.rename_mp3(files)
    
def renid3():
    """    
    USAGE: renid3 FILES
    
    Rename all FILES based on the ID3 tags and the FORMAT. Example of FORMAT:
    '%(tracknumber)s-%(artist)s-%(title)s.mp3'. Other tags can be specified: date, author,
    composer, performer, discnumber, album, etc.
    
    FORMAT is retrieved from the RBCO_RENAME_ID3_FORMAT environment 
    variable. If there's no such variable then a default format is used.        
    """
    files = sys.argv[1:]
    renaming.rename_id3(files)    
                
def renlu():
    """
    Usage: renlu FILES
    
    Renames all files in FILES performing the following operations:
    - replaces ' ' by '_';
    - replaces ' - ' and '- ' by '-';
    - lowercase the names;
    - remove leading and trailing spaces.
    """
    files = sys.argv[1:]
        
    for f in files:
        (filedir, filename) = os.path.split(f)
        if len(filename) <= 0:
            continue
        
        extension = renaming.getExtension(filename)
        newName = renaming.removeExtension(filename)
            
        newName = newName.replace(" ", "_").replace(" - ", "-").\
            replace("- ", "-").lower().strip()

        if len(extension) > 0:
            newName += "." + extension.lower()        
                                    
        os.rename(f, os.path.join(filedir, newName))       
        
def rendel():
    """
    Usage: rendel STR FILES
    
    Deletes the string STR from the names of all files in FILES.
    """
    s = sys.argv[1]
    files = sys.argv[2:]
    
    renaming.rename_replace(files, s, "")
                 
                 
def rendeln():
    """
    Usage: rendeln N FILES
    
    Deletes the N first characters from the names of all files in FILES.
    """
    n = int(sys.argv[1])
    files = sys.argv[2:]
    
    renaming.rename_delete_first_chars(files, n)
    
def renremoveacc():
    """
    Usage: renremoveacc FILES
    
    Rename the FILES by replacing all accentuated characters by their ASCII counterparts.
    Eg.: "É Fácil.mp3" -> "E Facil.mp3"
    """    
    files = sys.argv[1:]
    renaming.rename_remove_accentuation(files)
                 
