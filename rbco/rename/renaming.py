"""File renaming utilities."""
import os
import urllib
import re
from unidecode import unidecode

    
def getExtension(filename):
    """Returns the file extension."""
    parts = filename.split(".")
    if len(parts) > 1:
        return parts[-1]
    else:
        return ""        
        
def removeExtension(filename):
    """Returns filename with the extension removed."""
    parts = filename.split(".")
    if len(parts) > 1:
        return ".".join(parts[:-1])
    else:
        return filename       
        
def rename_prefix(files, s):
    """Renames all files in files prefixing then with the string s.
    
    Arguments:
    files -- a sequence of path strings.
    s -- an string.
    """
    for f in files:      
        (filedir, filename) = os.path.split(f)
        newName = s + filename
        os.rename(f, os.path.join(filedir, newName))
        
def rename_suffix(files, s, preserveExtension = True):
    """Renames all files in files suffixing then with the string s.
    
    Arguments:
    files -- a sequence of path strings.
    s -- an string.
    preserveExtension -- preserve file extension ?
    """
    for f in files:
        (filedir, filename) = os.path.split(f)
            
        if preserveExtension:
            extension = getExtension(filename)
            newName = removeExtension(filename) + s
            if len(extension) > 0:
                newName += "." + extension            
        else:
            newName = filename + s
                                           
        os.rename(f, os.path.join(filedir, newName))        
        
def rename_replace(files, old, new):
    """
    Renames all files in files replacing the string old by new.
    
    Arguments:
    files -- a sequence of path strings.
    old -- an string.
    new -- an string.
    """
    for f in files:
        (filedir, filename) = os.path.split(f)
        newName = filename.replace(old, new)
        os.rename(f, os.path.join(filedir, newName))    

def rename_delete_first_chars(files, n):
    """
    Renames all files in files deleting the n first chars.
    
    Arguments:
    files -- a sequence of path strings.
    n -- the number of chars to delete.
    """
    for f in files:
        (filedir, filename) = os.path.split(f)
        newName = filename[n:]
        os.rename(f, os.path.join(filedir, newName))  

def rename_remove_accentuation(files):
    """
    Renames all `files` replacing all accentuated characters by their ASCII counterparts.
    Eg.: "É Fácil.mp3" -> "E Facil.mp3"
    
    Arguments:
    files -- a sequence of path strings.
    """
    for f in files:
        (filedir, filename) = os.path.split(f)        
        new_name = remove_accentuation(filename)
        os.rename(f, os.path.join(filedir, new_name))

def rename_mp3(files):
    """    
    Renames all `files` in performing the following operations:
    - replaces all accentuated characters by their ASCII counterparts (Eg.: 
      "É Fácil.mp3" -> "E Facil.mp3").
    - replaces '_' by ' ';
    - replaces ' - ' and '- ' by '-';
    - titlecase the names;
    - lowcase file extension;
    - remove leading and trailing spaces;
    - replace ' ' by '-' after the track number, if needed;
    - makes track numbers have always 2 digits.
    
    
    Arguments:
    files -- a sequence of path strings.    
    """        
    for path in files:
        if not path:
            continue
        
        if path[-1] == os.sep:
            path = path[:-1]
        
        (filedir, filename) = os.path.split(path)
        
        if not filename:
            continue
        
        extension = getExtension(filename)
        newName = removeExtension(filename)        
        
        newName = remove_accentuation(newName) \
            .replace("_", " ") \
            .replace(" - ", "-") \
            .replace("- ", "-") \
            .title() \
            .strip()
        newName = fixTrackNumber(newName)
        newName = fixTitleCase(newName)
        
        if extension:
            newName += "." + extension.lower()        
        
        newPath = os.path.join(filedir, newName)
                           
        os.rename(path, newPath)    

def remove_accentuation(s):
    return unidecode(unicode(s, 'utf8'))

def fixTitleCase(fileName):
    """Fix the string.title() issue with the (') character. E.g.: takes "You Don'T Know" and 
    returns "You Don't Know".
    """
    
    fileNameParts = fileName.split("'")
    fixedParts = [fileNameParts[0]]
    
    for part in fileNameParts[1:]:
        if part:
            fixedParts.append(part[0].lower() + part[1:])
        else:
            fixedParts.append(part)
                    
    return "'".join(fixedParts)       
    
def fixTrackNumber(fname):
    """
    Replace ' ' by '-' after the track number, if needed.
    
    """
    TRACK_NUMBER_PATTERN = r'(\d\d?)( |-)'
    
    match = re.match(TRACK_NUMBER_PATTERN, fname)
    if not match:
        return fname
    
    matched = match.group()
    track_number = match.group(1)
    separator = '-'
    
    if len(track_number) == 1:
        track_number = '0' + track_number
        
    return fname.replace(matched, track_number + separator)      
               
def unhide(filename):
    if filename[0].startswith('.'):
        os.rename(filename, filename[1:])
        
        

