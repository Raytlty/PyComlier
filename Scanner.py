__author__ = 'Benco'
from math import *
import re
import time


Token_Type={
    "ORIGIN":0,"SCALE":1,"ROT":2,"IS":3,
    "TO":4,"STEP":5,"DRAW":6,"FOR":7,"T":8,
    "SEMICO":9,"L_BRACKET":10,"R_BRACKET":11,"COMMA":12,"PLUS":13,
    "MINUS":14,"MUL":15,"DIV":16,"POWER":17,
    "FUNC":18,"CONST_ID":19,"NONTOKEN":20,"ERRTOKEN":21,
    'FROM':22,'COMMENT':23
}

Token_Tab={
    "PI":[Token_Type["CONST_ID"],"CONST_ID",pi,None],
    "E":[Token_Type["CONST_ID"],"CONST_ID",e,None],
    "T":[Token_Type["T"],"T",0.0,None],
    "SIN":[Token_Type["FUNC"],"FUNC",0.0,sin],
    "COS":[Token_Type["FUNC"],"FUNC",0.0,cos],
    "LN":[Token_Type["FUNC"],'FUNC',0.0,log],
    "EXP":[Token_Type["FUNC"],'FUNC',0.0,exp],
    "SQRT":[Token_Type['FUNC'],'FUNC',0.0,sqrt],
    'ORIGIN':[Token_Type['ORIGIN'],'ORIGIN',0.0,None],
    'SCALE':[Token_Type['SCALE'],'SCALE',0.0,None],
    'ROT':[Token_Type['ROT'],'ROT',0.0,None],
    'IS':[Token_Type['IS'],'IS',0.0,None],
    'FOR':[Token_Type['FOR'],'FOR',0.0,None],
    'FROM':[Token_Type['FROM'],'FROM',0.0,None],
    'TO':[Token_Type['TO'],'TO',0.0,None],
    'STEP':[Token_Type['STEP'],'STEP',0.0,None],
    'DRAW':[Token_Type['DRAW'],'DRAW',0.0,None],
    'NONTOKEN':[Token_Type['NONTOKEN'],'NONTOKEN',0.0,None],
    'ERRTOKEN':[Token_Type['ERRTOKEN'],'ERRTOKEN',0.0,None],
    '/':[Token_Type['DIV'],'DIV',0.0,None],
    '(':[Token_Type['L_BRACKET'],'L_BRACKET',0.0,None],
    ')':[Token_Type["R_BRACKET"],'R_BRACKET',0.0,None],
    '*':[Token_Type['MUL'],'MUL',0.0,None],
    '**':[Token_Type['POWER'],'POWER',0.0,None],
    '+':[Token_Type['PLUS'],'PLUS',0.0,None],
    '-':[Token_Type['MINUS'],'MINUS',0.0,None],
    ',':[Token_Type['COMMA'],'COMMA',0.0,None],
    ';':[Token_Type['SEMICO'],'SEMICO',0.0,None],
    '//':[Token_Type['COMMENT'],'COMMENT',0.0,None],
    '--':[Token_Type['COMMENT'],'COMMENT',0.0,None]
    #'COMMENT':[Token_Type['COMMENT'],'COMMENT',0.0,None],
    #'POWER':[Token_Type['POWER'],'POWER',0.0,None]
}
'''
def GetTokenList(line,No):
    items=All.findall(str(line))
    lists=[]
    for item in items:
        token=Token(lineNo=No)
        #print(item,end=' ')
        token.GetToken(item)
        lists.append(token)
    token=Token()
    lists.append(token)
    return lists
'''
class Scanner:
    def __init__(self,filename=None,lineNo=1):
        self.re=re.compile(r'(\d+\.\d+[eE][-+]?\d+|\d+\.\d*|[0-9]\d*|0[0-7]+|0x[0-9a-fA-F]+|[a-zA-Z_]\w*|\|\||\+|\-[-]?|\*[*]?|/[/]?|=|\?|:|,|;|\(|\)|\[|\]|\{|\}|\'|\")')
        self.__fileptr=open(filename,mode='r')
        self.__string=self.__fileptr.read()
        self.elementlist=self.re.findall(self.__string.upper())
        self.__fileptr.close()
        self.lineNo=lineNo
        self.items=[]
        self.GetScanner()
    def GetScanner(self):
        for key in self.elementlist:
            if key=='\n':
                self.lineNo+=1
                continue
            elif key in Token_Tab:
                self.items.append(Token_Tab[key])
            elif key.replace('.','',1).isdecimal():
                self.items.append([Token_Type['CONST_ID'],'CONST_ID',float(key),None])
            else:
                self.items.append(Token_Tab['ERRTOKEN'])
        self.items.append(Token_Tab['NONTOKEN'])
    '''
    def GetToken(self):
        self.key=key
        if key.upper() in Token_Tab:
            self.value=Token_Tab[key.upper()]
        elif key.isdecimal():
            self.value=[Token_Type['CONST_ID'],'CONST_ID',float(key),None]
        else:
            self.key='ERRTOKEN'
            self.value=Token_Tab['ERRTOKEN']'''