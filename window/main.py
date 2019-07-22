# -*- coding=utf-8 -*-
from tkinter import *
from tkinter import ttk
from batscript import  batscript
import sys
import codecs

class portal(object):
    # 初始化参数
    def __init__(self,master):
        print("------portal init-----")
        print(sys.getdefaultencoding())

        self.master = master
        self.init_widgets()
    # 创建界面组件
    def init_widgets(self):
        win=self.master

        win.filenew_icon = PhotoImage(file='../images/add.png')
        win.fileopen_icon = PhotoImage(file='../images/open.png')
        menubar = Menu(win)
        # 添加菜单条
        win['menu'] = menubar
        # 创建file_menu菜单，它被放入menubar中
        file_menu = Menu(menubar, tearoff=0)
        # 使用add_cascade方法添加file_menu菜单
        menubar.add_cascade(label='文件', menu=file_menu)
        # 创建lang_menu菜单，它被放入menubar中
        lang_menu = Menu(menubar, tearoff=0)
        # 使用add_cascade方法添加lang_menu菜单
        menubar.add_cascade(label='选择语言', menu=lang_menu)
        # 使用add_command方法为file_menu添加菜单项
        file_menu.add_command(label="新建", command=None,
                              image=win.filenew_icon, compound=LEFT)
        file_menu.add_command(label="打开", command=None,
                              image=win.fileopen_icon, compound=LEFT)
        # 使用add_command方法为file_menu添加分隔条
        file_menu.add_separator()
        # 为file_menu创建子菜单
        sub_menu = Menu(file_menu, tearoff=0)
        # 使用add_cascade方法添加sub_menu子菜单
        file_menu.add_cascade(label='选择性别', menu=sub_menu)
        self.genderVar = IntVar()
        # 使用循环为sub_menu子菜单添加菜单项
        for i, im in enumerate(['男', '女', '保密']):
            # 使用add_radiobutton方法为sub_menu子菜单添加单选菜单项
            # 绑定同一个变量，说明它们是一组
            sub_menu.add_radiobutton(label=im, command=None,
                                     variable=self.genderVar, value=i)
        self.langVars = [StringVar(), StringVar(), StringVar(), StringVar()]
        # 使用循环为lang_menu菜单添加菜单项
        for i, im in enumerate(('Python', 'Kotlin', 'Swift', 'Java')):
            # 使用add_add_checkbutton方法为lang_menu菜单添加多选菜单项
            lang_menu.add_checkbutton(label=im, command=None,
                                      onvalue=im, variable=self.langVars[i])
        #主页布局
        self.init_main();

        '''
        #添加滚动条
        win.rowconfigure(0, weight=1)
        win.columnconfigure(0, weight=1)
        text = Text(win);
        text.grid();

        # 纵向
        sb = Scrollbar(win)
        sb.grid(row=0, column=1, sticky='ns')
        text.configure(yscrollcommand=sb.set)
        sb.configure(command=text.yview)
        # 横向
        sb = Scrollbar(win, orient='horizontal')
        sb.grid(row=1, column=0, sticky='ew')
        text.configure(xscrollcommand=sb.set)
        sb.configure(command=text.xview)
        '''
    def init_main(self):
        # 主界面
        self.initface = Frame(self.master)
        self.initface.pack()

        # 读取配置文件，获取根目录
        with codecs.open("../resource/bat.txt", 'r', 'utf-8', buffering=True) as f:
            # 使用for循环遍历文件对象
            for line in f:
                if line.startswith("#"):
                    continue
                list = line.split("@")
                btn = Button(self.initface, text=list[0], command=lambda arr=list: self.executebat(arr))
                btn.pack()

    def executebat(self,list):
        bat = batscript(list[1])
        bat.executebat()

    def changeFace(self):
        self.initface.destroy()
        self.master.config(bg='blue')
        self.initface = Frame(self.master)
        self.initface.pack()
        btn_back = Button(self.initface, text='face1 back', command=self.changeFace2)
        btn_back.pack()

    def changeFace2(self):
        self.initface.destroy()
        self.master.config(bg='red')
        self.initface = Frame(self.master, )
        self.initface.pack()
        btn_back = Button(self.initface, text='face1 back', command=self.changeFace)
        btn_back.pack()


if __name__ == "__main__":
    # 主程序执行
    win = Tk()
    win.title("桌面快捷工具")  # 菜单
    # 得到屏幕宽度
    sw = win.winfo_screenwidth()
    # 得到屏幕高度
    sh = win.winfo_screenheight()
    ww = 600
    wh = 300
    '''
    窗口宽高为100
    屏幕宽 - 窗口宽 = 窗口两边的宽度（记得是两边，仔细想想）
    然后我们除于一半得到屏幕左边的宽度，这就是我们窗口位于屏幕x轴开始的位置
    '''
    x = (sw - ww) / 2
    y = (sh - wh) / 2
    win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
    # win.geometry("500x620")  # #窗口位置500后面是字母x
    win.iconbitmap('../images/Panda.ico')
    # 禁止改变窗口大小
    #win.resizable(width=False, height=False)
    # 设定窗口总是显示在最前面
    #win.wm_attributes("-topmost", 1)
    portal(win);
    mainloop()
