__author__ = 'Benco'
import tkinter

class Painter:
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.title("PyComlier@Benco")
        self.canvas=tkinter.Canvas(self.root,width=700,height=1000,bg='white')
        self.canvas.pack()
    def DrawPiex(self,cood_x,cood_y):
        self.canvas.create_oval(cood_x,cood_y,cood_x,cood_y,fill='red',width=0)
    def MainLoop(self,PaintPoint=[]):
        for item in PaintPoint:
            #print(item[0],item[1])
            self.DrawPiex(item[0],item[1])
        self.root.mainloop()