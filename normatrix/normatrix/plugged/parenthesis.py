try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
except ModuleNotFoundError:
    from normatrix.normatrix.source.file_parser import CFileParse
    from normatrix.normatrix.source.config import TypeLine

import re

def check(context, file: CFileParse) -> (int, int):
    nb_error = 0
    list_ok = ["do", "while", "for", "return", "if"]
    for i in range(len(file.sub_parsedline)):
        line = file.sub_parsedline[i]
        if line[0] != TypeLine.COMMENT:
            ll = re.sub("\/\/.*", '', line[1])
            if '){' in ll:
                print(f"{file.basename}:{i + 1}: need a space between '){{'")
                nb_error += 1
            for e, char in enumerate(ll, start=1):
                if char == '(' and ll[e - 2] == ' ':
                    found = 0
                    for to_check in list_ok:
                        if ll[e - len(to_check) - 2:e] == f"{to_check} (":
                            found = 1
                    if found == 0:
                        print(f"{file.basename}:{i + 1}: no need space when function call")
                        nb_error += 1
    return (nb_error, 1)
