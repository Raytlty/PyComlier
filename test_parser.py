__author__ = 'Benco'
from Parser import  *
from  Scanner import *

def test_parser():
    ExprNode_tree=Parser('a.txt')
    ExprNode_tree.Program()
    #for item in lists:
        ##print('%5d %5s %5f %5s'%(item.value[0],item.value[1],item.value[2],item.value[3]))
    #tmp=ExprNode_tree.Expression()
    #print(tmp)
    #print(ExprNode_tree.GetExprValue(tmp))
    #ExprNode_tree.Print_Tree(len(ExprNode_tree.node_lists)-1)
    #for i in range(len(ExprNode_tree.node_lists))
if __name__ == '__main__':
   test_parser()
