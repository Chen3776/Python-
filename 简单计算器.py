from tkinter import *
from tkinter.font import names
class App:
    def __init__(self,master):
        self.master = master
        self.initWidgets()
        self.hi = None
    def initWidgets(self):
        #创建一个输入组件
        self.show = Label(relief=SUNKEN,font=('Courier New',24),width=23,bg='white',anchor=W)
        self.show.pack(side=TOP,pady=10)
        p = Frame(self.master)
        p.pack(side=TOP)
        #定义字符串的元组
        names = ('+','1','2','3','clear','-','4','5','6','**','*','7','8','9','//','/','.','0','%','=')
        #遍历字符串的元组
        for i in range(len(names)):
            #创建button，并放入p组件
            b = Button(p,text=names[i],font=("Verdana",20),width=5)
            b.grid(row=i // 5,column=i % 5)
            #为鼠标左键的单击事件绑定处理方法
            b.bind('<Button-1>',self.click)
            #为鼠标左键的双击事件绑定处理方法
            if b['text'] == 'clear':b.bind("<Button-1>",self.clean)
        #定义一个记录输入数字次数的变量
        self.i = 0
    def click(self,event):
        #如果用户单击数字键或dot
        if(event.widget['text'] in ('0','1','2','3','4','5','6','7','8','9','.')):
            #判断self.i是否0,0就清空show['text']的值
            if self.i == 0:
                self.show['text'] = ''
            self.show['text'] = self.show['text'] + event.widget['text']
            self.i = self.i + 1
            print(self.i)
        #如果用户单击了运算符
        elif(event.widget['text'] in ('+','-','*','/','//','*','**','%')):
            #输入的数字与输入的字符相结合，组成一个数学表达式
            self.show['text'] = self.show['text'] + event.widget['text']
        elif(event.widget['text'] == '=' and self.show['text'] is not None):
            #赋值给self.hi
            self.hi = self.show['text']
            print(self.hi)
            #使用eval函数计算表达式的值
            self.show['text'] = str(eval(self.hi))
            self.hi = None
            self.i = 0
    #点击clear按钮时，程序清空计算结果，表达式变成None
    def clean(self,event):
        self.hi = None
        self.show['text'] = ''
root = Tk()
root.title("简单计算器")
App(root)
root.mainloop()