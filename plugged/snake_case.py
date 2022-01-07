from source.file_parser import CFileParse
from source.file_parser import TypeLine
import os

def check(file: CFileParse) -> (int, int):
    for char in os.path.basename(file.basename):
        if char in [chr(i) for i in range(ord('A'), ord('Z') + 1)]:
            print(f"{file.basename}: only lower case in file name")
            return (1, 0)
    return (0, 0)
