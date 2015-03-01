__author__ = 'Benco'
from Scanner import *
from Error import *

class Node:
    def __init__(self,idx=0,token_type='NONTOKEN',token_val=0.0,token_func=None,left=None,right=None):
        self.idx=idx
        self.left=left
        self.right=right
        self.token_type=token_type
        self.token_val=token_val
        self.token_func=token_func
class Parser:
    def __init__(self,filename=None,pos=1):

        self.scanner=Scanner(filename)
        self.lists=self.scanner.items
        self.token=self.lists[0]
        self.node_lists=[]
        self.node_x_lists=[]
        self.node_y_lists=[]
        self.gui_lists=[]
        self.pos=pos

        self.Parameter=0
        self.Origin_x=0
        self.Origin_y=0
        self.Scale_x=0
        self.Scale_y=0
        self.Rot_angle=0
        self.x=0
        self.y=0
        self.start=0
        self.end=0
        self.step=0


    def Print_Tree(self,pos,index=0):
        if pos==None:
            return
        #print(pos)
        node=self.node_lists[pos]
        for i in range(index):
            print(' ',end=' ')
        if node.token_type=='CONST_ID':
            print('%.2f'%node.token_val)
        elif node.token_type=='MINUS':
            print('-')
        elif node.token_type=='PLUS':
            print('+')
        elif node.token_type=='MUL':
            print('*')
        elif node.token_type=='DIV':
            print('/')
        elif node.token_type=='POWER':
            print('**')
        elif node.token_type=='FUNC':
            print(node.token_func)
        else:
            print(node.token_type)
        self.Print_Tree(node.left,index+1)
        self.Print_Tree(node.right,index+1)

    def MakeExprNode(self,token_type='NONTOKEN',token_val=0.0,token_func=None,left=None,right=None):
        pos=len(self.node_lists)
        node=Node(idx=pos,token_type=token_type,token_val=token_val,token_func=token_func,left=left,right=right)
        self.node_lists.append(node)
        return pos
    '''
    def MakeExprNode_x(self,token_type='NONTOKEN',token_val=0.0,token_func=None,left=None,right=None):
        pos=len(self.node_x_lists)
        node=Node(idx=pos,token_type=token_type,token_val=token_val,token_func=token_func,left=left,right=right)
        self.node_x_lists.append(node)
        return pos
    def MakeExprNode_y(self,token_type='NONTOKEN',token_val=0.0,token_func=None,left=None,right=None):
        pos=len(self.node_y_lists)
        node=Node(idx=pos,token_type=token_type,token_val=token_val,token_func=token_func,left=left,right=right)
        self.node_y_lists.append(node)
        return pos'''
    def FetchToken(self):
        if self.pos<len(self.lists):
            token=self.lists[self.pos]
            if token[1]=='ERRTOKEN' :
                CerrError(1,self.scanner.lineNo,token[1])
            else:
                self.token=token
                #print(self.token[1])
                self.pos+=1

    def MatchToken(self,Token_type):
        #print(Token_type)
        if self.token[1]!=Token_type:
                CerrError(2,self.scanner.lineNo,Token_type)
        else :
            self.FetchToken()
    def GetExprValue(self,root):
        if root==None:
            return 0.0
        node=self.node_lists[root]
        #print(node.token_type,end=' ')
        if node.token_type=='PLUS':
            return self.GetExprValue(node.left)+self.GetExprValue(node.right)
        elif node.token_type=='MINUS':
            return self.GetExprValue(node.left)-self.GetExprValue(node.right)
        elif node.token_type=='MUL':
            return self.GetExprValue(node.left)*self.GetExprValue(node.right)
        elif node.token_type=='DIV':
            return self.GetExprValue(node.left)/self.GetExprValue(node.right)
        elif node.token_type=='POWER':
            return self.GetExprValue(node.left)**self.GetExprValue(node.right)
        elif node.token_type=='FUNC':
            return node.token_func(self.GetExprValue(node.right))
        elif node.token_type=='CONST_ID':
            return node.token_val
        elif node.token_type=='T':
            return self.Parameter
        else:
            return 0.0
    def DelExprTree(self):
        self.node_lists.clear()

    def Program(self):
        print('Enter Program')
        #print(self.token[1])
        while self.token[1]!='NONTOKEN' :
            self.Statement()
            self.MatchToken('SEMICO')
        print('Exit Program')

    def Statement(self):
        print('Enter Program')
        if self.token[1]=='ORIGIN':
            self.OriginStatement()
        elif self.token[1]=='SCALE':
            self.ScaleStatement()
        elif self.token[1]=='ROT':
            self.RotStatement()
        elif self.token[1]=='FOR':
            self.ForStatement()
        else :
            CerrError(3,self.scanner.lineNo,self.token[1])
        print('Exit Statement')

    def OriginStatement(self):
        print('Enter OriginStatement')
        self.MatchToken('ORIGIN')
        self.MatchToken('IS')
        self.MatchToken('L_BRACKET')
        tmp=self.Expression()
        self.Origin_x=self.GetExprValue(tmp)
        self.DelExprTree()
        self.MatchToken('COMMA')
        tmp=self.Expression()
        self.Origin_y=self.GetExprValue(tmp)
        self.DelExprTree()
        self.MatchToken('R_BRACKET')
        #print(self.Origin_x,self.Origin_y)
        print('Exit OriginStatement')

    def ScaleStatement(self):
        print('Enter ScaleStatement')
        self.MatchToken('SCALE')
        self.MatchToken('IS')
        self.MatchToken('L_BRACKET')
        tmp=self.Expression()
        self.Scale_x=self.GetExprValue(tmp)
        #print(self.Scale_x)
        self.DelExprTree()
        self.MatchToken('COMMA')
        tmp=self.Expression()
        self.Scale_y=self.GetExprValue(tmp)
        self.DelExprTree()
        self.MatchToken('R_BRACKET')
        print('Exit ScaleStatement')

    def RotStatement(self):
        print('Enter RotStatement')
        self.MatchToken('ROT')
        self.MatchToken('IS')
        tmp=self.Expression()
        self.Rot_angle=self.GetExprValue(tmp)
        self.DelExprTree()
        print('Exit RotStatement')

    def ForStatement(self):
        print('Enter ForStatement')
        self.MatchToken('FOR')
        self.MatchToken('T')
        self.MatchToken('FROM')
        start_ptr=self.Expression()

        self.start=self.GetExprValue(start_ptr)
        self.DelExprTree()

        self.MatchToken('TO')
        end_ptr=self.Expression()
        self.end=self.GetExprValue(end_ptr)
        self.DelExprTree()

        self.MatchToken('STEP')
        step_ptr=self.Expression()
        self.step=self.GetExprValue(step_ptr)
        self.DelExprTree()
        self.MatchToken('DRAW')
        self.MatchToken('L_BRACKET')

        x_ptr=self.Expression()
        self.MatchToken('COMMA')
        y_ptr=self.Expression()
        self.MatchToken('R_BRACKET')

        self.DrawLoop(Start=self.start,End=self.end,Step=self.step,HorPtr=x_ptr,VerPtr=y_ptr)
        self.DelExprTree()
        print('Exit ForStatement')
    def Expression(self):
        #print('fuck expression')
        print('Enter Expression')
        left=self.Term()
        while self.token[1]=='PLUS'or self.token[1]=='MINUS':
            token_tmp=self.token[1]
            self.MatchToken(token_tmp)
            right=self.Term()
            left=self.MakeExprNode(token_type=token_tmp,left=left,right=right)
        self.Print_Tree(left,0)
        print('Exit Expression')
        return left
    def Term(self):
        #print('fuck term')
        print('Enter Term')
        left=self.Factor()
        while self.token[1]=='MUL' or self.token[1]=='DIV':
            token_tmp=self.token[1]
            self.MatchToken(token_tmp)
            right=self.Factor()
            left=self.MakeExprNode(token_type=token_tmp,left=left,right=right)
        print('Exit Term')
        return left
    def Factor(self):
        print('Enter Factor')
        if self.token[1]=='PLUS':
            self.MatchToken('PLUS')
            right=self.Factor()
        elif self.token[1]=='MINUS':
            self.MatchToken('MINUS')
            right=self.Factor()
            left=self.MakeExprNode(token_type='CONST_ID',token_val=0.0)
            right=self.MakeExprNode(token_type='MINUS',left=left,right=right)
        else:
            right=self.Component()
        print('Exit Factor')
        return right
    def Component(self):
        print('Enter Component')
        left=self.Atom()
        if self.token[1]=='POWER':
            self.MatchToken('POWER')
            right=self.Component()
            left=self.MakeExprNode(token_type='POWER',left=left,right=right)
        print('Exit Component')
        return left
    def Atom(self):
        print('Enter Atom')
        #print('fuck atom')
        #print(self.pos)
        t=self.token
        address=None
        tmp=None
        if self.token[1]=='CONST_ID':
            self.MatchToken('CONST_ID')
            address=self.MakeExprNode(token_type='CONST_ID',token_val=t[2])
        elif self.token[1]=='T':
            self.MatchToken('T')
            address=self.MakeExprNode(token_type='T',token_val=self.Parameter)
        elif self.token[1]=='FUNC':
            self.MatchToken('FUNC')
            self.MatchToken('L_BRACKET')
            tmp=self.Expression()
            address=self.MakeExprNode(token_type='FUNC',token_func=t[3],right=tmp)
            self.MatchToken('R_BRACKET')
        elif self.token[1]=='L_BRACKET':
            self.MatchToken('L_BRACKET')
            address=self.Expression()
            self.MatchToken('R_BRACKET')
        print('Exit Atom')
        return address

    def DrawLoop(self,Start=None,End=None,Step=None,HorPtr=None,VerPtr=None):
        self.Parameter=Start
        #print(Start,End,Step,HorPtr,VerPtr)
        while self.Parameter<=End:
            self.CalcCoord(HorPtr,VerPtr)
            self.gui_lists.append((self.x,self.y))
            #self.DrawPiex()
            self.Parameter+=Step
    def CalcCoord(self,Horptr=None,VerPtr=None):
        HorCord=self.GetExprValue(Horptr)
        VerCord=self.GetExprValue(VerPtr)
        #print(HorCord,VerCord)
        HorCord*=self.Scale_x
        VerCord*=self.Scale_y

        Hor_tmp=HorCord*cos(self.Rot_angle)+VerCord*sin(self.Rot_angle)
        VerCord=VerCord*cos(self.Rot_angle)-HorCord*sin(self.Rot_angle)
        HorCord=Hor_tmp

        HorCord+=self.Origin_x
        VerCord+=self.Origin_y
        #print('1:%f %f'%(self.x,self.y),end=' ')
        self.x=HorCord
        self.y=VerCord
        #print('2:%f %f'%(self.x,self.y))

