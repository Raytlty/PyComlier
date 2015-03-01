__author__ = 'Benco'
import  tkinter
from Parser import  *
from Scanner import  *
from GUI import *


def test_gui():
    parser=Parser('a.txt')
    parser.Program()
    painter=Painter()
    #print(parser.gui_lists)
    painter.MainLoop(parser.gui_lists)
if __name__ == '__main__':
    test_gui()