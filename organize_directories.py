"""
Sort files in a folder into subfolders

set the Folder path before running the script
"""

import os
from pathlib import Path


FOLDER = Path.home() / "Downloads"
#   FOLDER = Path.home() / "Downloads"          # works on Windows and Ubuntu
#   FOLDER = r"C:\Users\Amir\Desktop\Stuff"     # Windows (keep the r in front)
#   FOLDER = "/home/amir/Documents/stuff"       # Ubuntu

CONFIRM_PHRASE = "lets move"


SUBDIR = {
    "Docs": ['.pdf', '.docx', '.txt', '.rtf'],
    "Audio": ['.mp3', '.wav', '.flac', '.aac'],
    "Video": ['.mp4', '.mkv', '.avi', '.mov'],
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp']   
}

def pickDirectory(value):
    for category, suffixes in SUBDIR.items():
        if value in suffixes:
            return category
    return "Misc"

def uniquePath(path):
    """
    Returns a unique path by appending a number if the path already exists.
    if it already exists, it will append (1), (2), etc. to the filename until it finds a unique name.
    """
    if not path.exists():
        return path
    counter = 1
    while True:
        candidate = path.with_name(f"{path.stem} ({counter}){path.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1
        
def organizeDirectory(folder, dryRun = True):
    """
    dryRun = True: only prints the actions that would be taken
    dryRun = False: actually moves the files into the subfolders
    Returns the number of files moved (or that would be moved).
    """
    folder  = Path(folder).expanduser().resolve()
    if not folder.is_dir():
        raise NotADirectoryError(f"{folder} is not a valid directory")
    
    thisScript = Path(__file__).resolve()
    
    files = [p for p in folder.iterdir() if p.is_file()]
    
    moved = 0
    
    for filePath in files:
        if filePath == thisScript or filePath.name.startswith('.'):
            continue  # doesn't move this script or hidden files
        
        category = pickDirectory(filePath.suffix.lower())
        targetDir = folder / category
        target = uniquePath(targetDir / filePath.name)
        
        print(f"{filePath.name}  ->  {category}/{target.name}")
        
        if not dryRun:
            targetDir.mkdir(exist_ok = True)
            filePath.rename(target)
        moved += 1
        
    verb = "Would move" if dryRun else "Moved"
    print(f"{verb} {moved} files into {folder}")
    return moved
        
        

if __name__ == "__main__":
    
    print("Checking the folder path", FOLDER)
    
    # Always preview first, nothing is moved
    count = organizeDirectory(FOLDER, dryRun = True)
    
    # If user enters the phrase move the items
    if (count > 0):
        answer = input('\nType "Lets move" to move the files, or anything else to cancel: ')
        cleaned = answer.strip().lower().replace("'", "")
        if cleaned == CONFIRM_PHRASE:
            print("Moving files ... ")
            organizeDirectory(FOLDER, dryRun = False)
        else:
            print("Operation cancelled.")