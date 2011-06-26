#coding=utf8
"""File renaming utilities."""
import os
import urllib
import re
from unidecode import unidecode

DEFAULT_ID3_FORMAT = '%(tracknumber)s-%(title)s.mp3'

def rename_files(paths, new_name_func):
    """
    Take a sequence of `paths` and rename the files. `new_name_func` is a function that takes a 
    filename (without the directory) and return the new name.
    """
    for f in paths:      
        (filedir, filename) = os.path.split(f)        
        os.chdir(filedir)
        os.rename(
            f, 
            os.path.join(filedir, new_name_func(filename))
        )
             
            
def rename_prefix(files, s):
    """Renames all files in files prefixing then with the string s.
    
    Arguments:
    files -- a sequence of path strings.
    s -- an string.
    """
    rename_files(files, lambda f: s + f)
        
def rename_suffix(files, s, preserveExtension = True):
    """Renames all files in files suffixing then with the string s.
    
    Arguments:
    files -- a sequence of path strings.
    s -- an string.
    preserveExtension -- preserve file extension ?
    """
    def get_new_name(f):
        if preserveExtension:
            extension = getExtension(f)
            newName = removeExtension(f) + s
            if len(extension) > 0:
                newName += "." + extension            
        else:
            newName = f + s      
        
        return newName  
    
    rename_files(files, get_new_name)   
        
def rename_replace(files, old, new):
    """
    Renames all files in files replacing the string old by new.
    
    Arguments:
    files -- a sequence of path strings.
    old -- an string.
    new -- an string.
    """
    rename_files(files, lambda f: f.replace(old, new)) 

def rename_delete_first_chars(files, n):
    """
    Renames all files in files deleting the n first chars.
    
    Arguments:
    files -- a sequence of path strings.
    n -- the number of chars to delete.
    """
    rename_files(files, lambda f: f[n:])

def rename_remove_accentuation(files):
    """
    Renames all `files` replacing all accentuated characters by their ASCII counterparts.
    Eg.: "É Fácil.mp3" -> "E Facil.mp3"
    
    Arguments:
    files -- a sequence of path strings.
    """
    rename_files(files, lambda f: remove_accentuation(f))

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
    def get_new_name(f):
        extension = getExtension(f)
        newName = removeExtension(f)        
        
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
        
        return newName    
     
    rename_files(files, get_new_name)

def rename_id3(files, format=None):
    """
    Rename all `files` based on the ID3 tags and the given `format`. Example of format:
    '%(tracknumber)s-%(artist)s-%(title)s.mp3'. Other tags can be specified: date, author,
    composer, performer, discnumber, album, etc.
    
    If format is not given then it is retrieved from the RBCO_RENAME_ID3_FORMAT environment 
    variable. If there's no such variable then a default format is used.    
    """
    format = format or os.environ.get('RBCO_RENAME_ID3_FORMAT', DEFAULT_ID3_FORMAT)
    return rename_files(files, lambda f: format % EasyID3(f))


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

    return filename

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
    """Replace ' ' by '-' after the track number, if needed."""
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
        
        

