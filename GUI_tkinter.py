from tkinter import *
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # Label是一个容器：文本显示
        self.nameInput = Entry(self)
        #利用pack()方法把容器放到父容器Frame中，实现布局
        self.nameInput.pack()
        #同上
        self.alterButton = Button(self, text = 'Hello', command = self.hello_input)
        self.alterButton.pack()

    def hello_input(self):
        name = self.nameInput.get() or 'World'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()