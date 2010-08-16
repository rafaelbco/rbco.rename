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
        if f[0] == ".":
            os.rename(f, f[1:])

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
    - replaces '_' by ' ';
    - replaces ' - ' and '- ' by '-';
    - titlecase the names;
    - lowcase file extension;
    - remove leading and trailing spaces;
    - replace ' ' by '-' after the track number, if needed;
    - makes track numbers have always 2 digits.
    """
    paths = sys.argv[1:]
        
    for path in paths:
        if not path:
            continue
        
        if path[-1] == os.sep:
            path = path[:-1]
        
        (filedir, filename) = os.path.split(path)
        
        if not filename:
            continue
        
        extension = renaming.getExtension(filename)
        newName = renaming.removeExtension(filename)
            
        newName = newName \
            .replace("_", " ") \
            .replace(" - ", "-") \
            .replace("- ", "-") \
            .title() \
            .strip()
        newName = renaming.fixTrackNumber(newName)
        newName = renaming.fixTitleCase(newName)
        
        if extension:
            newName += "." + extension.lower()        
        
        newPath = os.path.join(filedir, newName)
                           
        os.rename(path, newPath)
        
                
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
                 
