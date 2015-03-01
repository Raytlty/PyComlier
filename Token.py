__author__ = 'Benco'
from math import *
Token_Type={
    "ORIGIN":0,"SCALE":1,"ROT":2,"IS":3,
    "TO":4,"STEP":5,"DRAW":6,"FOR":7,"T":8,
    "SEMICO":9,"L_BRACKET":10,"R_BRACKET":11,"COMMA":12,"PLUS":13,
    "MINUS":14,"MUL":15,"DIV":16,"POWER":17,
    "FUNC":18,"CONST_ID":19,"NONTOKEN":20,"ERRTOKEN":21,
    'FROM':22,'COMMENT':23
}

Token_Tab={
    "PI":[Token_Type["CONST_ID"],"PI",pi,None],
    "E":[Token_Type["CONST_ID"],"E",e,None],
    "T":[Token_Type["T"],"T",0.0,None],
    "SIN":[Token_Type["FUNC"],"SIN",0.0,sin],
    "COS":[Token_Type["FUNC"],"COS",0.0,cos],
    "LN":[Token_Type["FUNC"],'LN',0.0,log],
    "EXP":[Token_Type["FUNC"],'EXP',0.0,exp],
    "SQRT":[Token_Type['FUNC'],'SQRT',0.0,sqrt],
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
    #'COMMENT':[Token_Type['COMMENT'],'COMMENT',0.0,None],
    #'POWER':[Token_Type['POWER'],'POWER',0.0,None]
}
class Token:
    pos=0
    def __init__(self,key='NONTOKEN',value=[Token_Type['NONTOKEN'],'NONTOKEN',0.0,None],lists=[]):
        self.key=key
        self.value=value
        self.lists=lists
    def CheckToken(self,fileptr):
        Tokenstr=""
        fileptr.seek(self.__class__.pos,0)
        ch=fileptr.read(1).upper()
       # print(ch,end=' ')
        self.__class__.pos+=1
        if ch=='\n' or ch =='\t':
            self.__class__.pos+=1
            self.key=None
            self.value=None
            return
        if ch.isalpha():
            Tokenstr=Tokenstr+ch
            ch=fileptr.read(1).upper()
            self.__class__.pos+=1
            while ch.isalpha():
                Tokenstr=Tokenstr+ch
                ch=fileptr.read(1).upper()
                self.__class__.pos+=1
            if not (ch.isspace() or ch == '\n' or ch == '\t'):
                self.__class__.pos-=1
            self.key=Tokenstr
            if self.key in Token_Tab.keys():
                self.value=Token_Tab[self.key]
        elif ch.isdigit():
            Tokenstr=Tokenstr+ch
            ch=fileptr.read(1)
            self.__class__.pos+=1
            while ch.isdigit():
                Tokenstr=Tokenstr+ch
                ch=fileptr.read(1)
                self.__class__.pos+=1
            if not (ch.isspace() or ch == '\n' or ch == '\t'):
                self.__class__.pos-=1
            self.key=Tokenstr
            self.value=[Token_Type["CONST_ID"],Tokenstr,float(Tokenstr),None]
        else:
            if ch == '+':
                self.key = 'PLUS'
                self.value = [Token_Type[self.key],self.key,0.0,None]
            elif ch == '-':
                ch=fileptr.read(1)
                self.__class__.pos+=1
                if ch == '-':
                    self.key='COMMENT'
                    self.value=[Token_Type[self.key],self.key,0.0,None]
                else:
                    self.key='MINUS'
                    self.value = [Token_Type[self.key],self.key,0.0,None]
                    self.__class__.pos-=1
            elif ch == '*':
                ch=fileptr.read(1)
                self.__class__.pos+=1
                if ch == '*':
                    self.key='POWER'
                    self.value=[Token_Type[self.key],self.key,0.0,None]
                else:
                    self.key='MUL'
                    self.value = [Token_Type[self.key],self.key,0.0,None]
                    self.__class__.pos-=1
            elif ch == '/':
                ch=fileptr.read(1)
                self.__class__.pos+=1
                if ch == '-':
                    self.key='COMMENT'
                    self.value=[Token_Type[self.key],self.key,0.0,None]
                else:
                    self.key='DIV'
                    self.value = [Token_Type[self.key],self.key,0.0,None]
                    self.__class__.pos-=1
            elif ch == ';':
                self.key='SEMICO'
                self.value=[Token_Type[self.key],self.key,0.0,None]
            elif ch == ',':
                self.key='COMMA'
                self.value=[Token_Type[self.key],self.key,0.0,None]
            elif ch == '(':
                self.key='L_BRACKET'
                self.value=[Token_Type[self.key],self.key,0.0,None]
            elif ch==')':
                self.key='R_BRACKET'
                self.value=[Token_Type[self.key],self.key,0.0,None]
            else:
                self.key='ERRTOKEN'
                self.value=[Token_Type[self.key],self.key,0.0,None]
    def GetTokenList(self,fileptr):
        line=fileptr.readline()






