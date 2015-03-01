__author__ = 'Benco'

def CerrError(num,lineNo,lexeme):
    if num==1:
        raise Exception(lineNo,"Wrong Masked",lexeme)
    elif num==2:
        raise Exception(lineNo,"Not Want Masked",lexeme)
    elif num==3:
        raise Exception(lineNo,"No Match Masked",lexeme)