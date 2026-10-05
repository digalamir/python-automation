import os
from pathlib import Path

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

# print(pickDirectory('.mp3'))  

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(directory)
        if not directoryPath.is_dir():
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))
        
