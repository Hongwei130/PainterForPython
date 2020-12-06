from tkinter.colorchooser import *
from tkinter import *

win_width = 900
win_height = 450


class Application(Frame):

    def __init__(self, master=None, bgcolor='#000000'):
        super().__init__(master)
        self.master = master
        self.bgcolor = bgcolor
        self.fgcolor = '#ff0000'
        self.lastDraw = 0
        self.startDrawFlag = False
        self.x = 0
        self.y = 0
        self.pack()
        self.create_widget()

    def create_widget(self):
        # 创建画板
        self.drawpad = Canvas(self.master, width=win_width, height=win_height*0.9, bg=self.bgcolor)
        # 创建按钮
        btn_start = Button(self.master, text='开始', name='start')
        btn_pen = Button(self.master, text='画笔', name='pen')
        btn_rect = Button(self.master, text='矩形', name='rect')
        btn_clear = Button(self.master, text='清屏', name='clear')
        btn_erasor = Button(self.master, text='橡皮擦', name='eraser')
        btn_line = Button(self.master, text='直线', name='line')
        btn_lineArrow = Button(self.master, text='箭头直线', name='lineArrow')
        btn_color = Button(self.master, text='颜色', name='color')
        self.drawpad.pack()
        btn_start.pack(side='left', padx='10')
        btn_pen.pack(side='left', padx='10')
        btn_rect.pack(side='left', padx='10')
        btn_clear.pack(side='left', padx='10')
        btn_erasor.pack(side='left', padx='10')
        btn_line.pack(side='left', padx='10')
        btn_lineArrow.pack(side='left', padx='10')
        btn_color.pack(side='left', padx='10')
        btn_pen.bind_class('Button', '<1>', self.eventManager)
        self.drawpad.bind('<ButtonRelease-1>', self.stopDraw)

        self.master.bind('<KeyPress-r>', self.my_short_cut)
        self.master.bind('<KeyPress-y>', self.my_short_cut)
        self.master.bind('<KeyPress-g>', self.my_short_cut)

    def my_short_cut(self, event):
        if event.char == 'r':
            self.fgcolor = "#ff0000"
        elif event.char == 'g':
            self.fgcolor = "#00ff00"
        elif event.char == 'y':
            self.fgcolor = "#ffff00"

    def stopDraw(self, event):
        self.startDrawFlag = False
        self.lastDraw = 0

    def eventManager(self, event):
        name = event.widget.winfo_name()
        print(name)
        if name == 'line':
            self.drawpad.bind('<B1-Motion>', self.myline)
        elif name == 'lineArrow':
            self.drawpad.bind('<B1-Motion>', self.mylineArrow)
        elif name == 'rect':
            self.drawpad.bind('<B1-Motion>', self.myRect)
        elif name == 'pen':
            self.drawpad.bind('<B1-Motion>', self.myPen)
        elif name == 'eraser':
            self.drawpad.bind('<B1-Motion>', self.myEraser)
        elif name == 'clear':
            self.drawpad.delete('all')
        elif name == 'color':
            c = askcolor(color=self.fgcolor, title='选择画笔颜色')
            self.fgcolor = c[1]

    def startDraw(self, event):
        self.drawpad.delete(self.lastDraw)
        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

    def myEraser(self, event):
        self.startDraw(event)
        self.drawpad.create_rectangle(event.x-4, event.y-4, event.x+4, event.y+4, fill=self.bgcolor)
        self.x = event.x
        self.y = event.y

    def myPen(self, event):
        self.startDraw(event)
        self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
        self.x = event.x
        self.y = event.y

    def myRect(self,event):
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)

    def mylineArrow(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=self.fgcolor)

    def myline(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)



if __name__ == '__main__':
    root = Tk()
    root.geometry(str(win_width)+'x'+str(win_height)+'+200+300')
    root.title('画图软件')
    app = Application(master=root)
    root.mainloop()