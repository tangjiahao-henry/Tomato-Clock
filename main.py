import tkinter
from tkinter import messagebox
import time
import os
import winsound
root = tkinter.Tk()
root.title('番茄时钟')
root.geometry('230x280')
root.configure(bg='Tomato')
root.iconbitmap('image/tomato_clock.ico')
count = 0
remain_time0 = 1500
remain_time1 = 300
def mymsg():
    tkinter.messagebox.showinfo("提示", "完成一个番茄钟，记得休息")
def mymsg2():
    tkinter.messagebox.showinfo("提示", "休息时间到")
def tomato_clock():
    global remain_time0
    bb = time.strftime('/  %M:%S', time.gmtime(remain_time0))
    lb2.configure(text=bb)
    lb3.configure(text='剩余时间/总时间')
    for i in range(remain_time0):
        remain_time0 -= 1
        aa = time.strftime('%M:%S', time.gmtime(remain_time0))
        lb.configure(text=aa)
        root.update()
        time.sleep(1)
        if remain_time0 == 0:
            winsound.Beep(600,100)
            winsound.Beep(1000,2000)
            tomato_count()
            mymsg()
def tomato_count():
    global count
    count += 1
def relax():
    global remain_time1
    bbb = time.strftime('/  %M:%S', time.gmtime(remain_time1))
    lb2.configure(text=bbb)
    lb3.configure(text='剩余时间/总时间')
    for i in range(remain_time1):
        remain_time1 -= 1
        aaa = time.strftime('%M:%S', time.gmtime(remain_time1))
        lb.configure(text=aaa)
        root.update()
        time.sleep(1)
        if remain_time1 == 0:
            winsound.Beep(600,100)
            winsound.Beep(1000,2000)
            mymsg2()
def time_a():
    global remain_time1, remain_time0
    remain_time0 = 1500
    remain_time1 = 300
def time_b():
    global remain_time1, remain_time0
    remain_time0 = 2700
    remain_time1 = 600
def time_C():
    global remain_time1, remain_time0
    remain_time0 = 3600
    remain_time1 = 600
def exit():
    os._exit()
lb = tkinter.Label(root, text=' ', bg='Tomato', fg='blue', font='Verdana 16 bold', width=7, height=1)
lb.place(x=0, y=50)
lb2 = tkinter.Label(root, text=' ', bg='Tomato', fg='blue', font='Verdana 16 bold', width=8, height=1)
lb2.place(x=88, y=50)
lb3 = tkinter.Label(root, text=' ', bg='Tomato', fg='blue', font='Verdana 16 bold', width=14, height=1)
lb3.place(x=5, y=25)
Button1 = tkinter.Button(root, text='开启新的番茄时钟', bg='orange', fg='black', font='Verdana 13 bold', width=15, height=1,command=tomato_clock)
Button1.place(x=20, y=75)
Button2 = tkinter.Button(root, text='休息', bg='cornflowerblue', fg='black', font='Verdana 13 bold', width=15,height=1, command=relax)
Button2.place(x=20, y=125)
var = tkinter.IntVar()
rb1 = tkinter.Radiobutton(root, text='25+05', variable=var, value=0, command=time_a, bg='Tomato')
rb2 = tkinter.Radiobutton(root, text='45+10', variable=var, value=1, command=time_b, bg='Tomato')
rb3 = tkinter.Radiobutton(root, text='60+10', variable=var, value=2, command=time_C, bg='Tomato')
rb1.place(x=85, y=160)
rb2.place(x=85, y=185)
rb3.place(x=85, y=210)
Button3 = tkinter.Button(root, text='关闭', bg='#77f5c2', fg='black', font='Verdana 13 bold', width=15, height=1,command=root.destroy)
Button3.place(x=20, y=230)
root.mainloop()