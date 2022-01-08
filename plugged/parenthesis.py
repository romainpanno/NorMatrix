from source.file_parser import CFileParse
from source.file_parser import TypeLine
import re

def check(file: CFileParse) -> (int, int):
    nb_error = 0
    for i in range(len(file.sub_parsedline)):
        line = file.sub_parsedline[i]
        if line[0] != TypeLine.COMMENT:
            ll = re.sub("\/\/.*", '', line[1])
            try:
                ll.index('){')
                print(f"{file.basename}:{i + 1}: need a space between '){{'")
                nb_error += 1
            except: pass
    return (nb_error, 1)
