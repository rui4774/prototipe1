from tkinter import *
import tkinter as tk
from tkinter import ttk, font

# defs
def entered1(event):
   tic1['image'] = tick2
def left1(event):
   tic1['image'] = tick1
def ticke1():
   eye1['text'] = ent1.get()
def entered2(event):
   tic2['image'] = tick2
def left2(event):
   tic2['image'] = tick1
def ticke2():
   eye2['text'] = ent2.get()
def entered3(event):
   tic3['image'] = tick2
def left3(event):
   tic3['image'] = tick1
def ticke3():
   eye3['text'] = ent3.get()
def entered4(event):
   tic4['image'] = tick2
def left4(event):
   tic4['image'] = tick1
def ticke4():
   eye4['text'] = ent4.get()
def entered5(event):
   tic5['image'] = tick2
def left5(event):
   tic5['image'] = tick1
def ticke5():
   eye5['text'] = ent5.get()

def clear(object):
   slaves = object.grid_slaves()
   for x in slaves:
      x.destroy()

# Доска с тасками
def firstpage():
   clear(mframe)
   clear(win)
   win.title('Доска с тасками')
   win.geometry('600x400+150+100')
   win.resizable(False, False)
   ttk.Style().theme_use('clam')
   pic2 = PhotoImage(file='logo.png')
   win.iconphoto(False, pic2)
   mframe1 = Frame(mframe, bg='white')
   mframe1.rowconfigure(index=6, weight=1)
   mframe1.columnconfigure(index=2, weight=1)
   mframe2 = Frame(mframe, bg='white')
   mframe2.rowconfigure(index=6, weight=1)

   # global
   global tic1
   global tic2
   global tic3
   global tic4
   global tic5
   global ent1
   global ent2
   global ent3
   global ent4
   global ent5
   global eye1
   global eye2
   global eye3
   global eye4
   global eye5

   lbl2 = Label(mframe1, text='Не выполнены', bg='#ADD8E6')
   lbl2.grid(column=2, row=1)
   lbl4 = Label(mframe2, text='Выполнены', bg='#ADD8E6')
   lbl4.place(x=50, y=60)

   ent1 = ttk.Entry(mframe1)
   ent1.grid(column=2, row=2)
   ent2 = ttk.Entry(mframe1)
   ent2.grid(column=2, row=3)
   ent3 = ttk.Entry(mframe1)
   ent3.grid(column=2, row=4)
   ent4 = ttk.Entry(mframe1)
   ent4.grid(column=2, row=5)
   ent5 = ttk.Entry(mframe1)
   ent5.grid(column=2, row=6)

   tic1 = Button(mframe1, image=tick1, command=ticke1)
   tic1.bind('<Enter>', entered1)
   tic1.bind('<Leave>', left1)
   tic1.grid(column=1, row=2)
   tic2 = Button(mframe1, image=tick1, command=ticke2)
   tic2.bind('<Enter>', entered2)
   tic2.bind('<Leave>', left2)
   tic2.grid(column=1, row=3)
   tic3 = Button(mframe1, image=tick1, command=ticke3)
   tic3.bind('<Enter>', entered3)
   tic3.bind('<Leave>', left3)
   tic3.grid(column=1, row=4)
   tic4 = Button(mframe1, image=tick1, command=ticke4)
   tic4.bind('<Enter>', entered4)
   tic4.bind('<Leave>', left4)
   tic4.grid(column=1, row=5)
   tic5 = Button(mframe1, image=tick1, command=ticke5)
   tic5.bind('<Enter>', entered5)
   tic5.bind('<Leave>', left5)
   tic5.grid(column=1, row=6)

   eye1 = ttk.Label(mframe2)
   eye1.place(x=50, y=90)
   eye2 = ttk.Label(mframe2)
   eye2.place(x=50, y=130)
   eye3 = ttk.Label(mframe2)
   eye3.place(x=50, y=170)
   eye4 = ttk.Label(mframe2)
   eye4.place(x=50, y=210)
   eye5 = ttk.Label(mframe2)
   eye5.place(x=50, y=250)

   mframe1.pack(side=tk.LEFT)
   mframe1.pack_propagate(False)
   mframe1.config(width=250, height=400)

   mframe2.pack(side=tk.RIGHT)
   mframe2.pack_propagate(False)
   mframe2.config(width=250, height=400)

   mframe.pack(side=tk.TOP)
   mframe.pack_propagate(False)
   mframe.config(width=500, height=400)

# Логин
def secondpage():
   clear(mframe)
   clear(win)
   win.title('Аккаунт')
   win.geometry('600x400+150+100')
   win.resizable(False, False)
   ttk.Style().theme_use('clam')
   pic2 = PhotoImage(file='logo.png')
   win.iconphoto(False, pic2)

   log = Label(mframe, text='LOGIN', font='codicon', fg='red', bg='white')
   log.place(x=200, y=80)
   login = ttk.Entry(mframe)
   login.place(x=150, y=170, width=200)
   password = ttk.Entry(mframe)
   password.place(x=150, y=200, width=200)
   tuk = ttk.Button(mframe, text='Enter')
   tuk.place(x=150, y=230)

   mframe.pack(side=tk.RIGHT)
   mframe.pack_propagate(False)
   mframe.config(width=500, height=400)


# window
win = Tk()
win.title('Таск-менеджер')
win.geometry('600x400+150+100')
win.resizable(False, False)
ttk.Style().theme_use('clam')
pic2 = PhotoImage(file='logo.png')
win.iconphoto(False, pic2)

# font
font1 = font.Font(family='codicon.ttf', size=12)
ttk.Style().configure('my.TButton', font=font1, background='#4169E1', foreground='white')

# images
pic1 = PhotoImage(file='cifra1.png')
tick1 = PhotoImage(file='tick1.png')
tick2 = PhotoImage(file='tick2.png')

# notebook
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
frame1 = ttk.Frame(notebook)
frame1.pack(fill=BOTH, expand=True)
notebook.add(frame1, text="Task manager", image=pic2, compound=LEFT)

# option frame
oframe = Frame(win, bg='#4169E1')

lbl1 = Label(oframe, image=pic1).pack()

btn1 = ttk.Button(oframe, text='Таски', style='my.TButton', width=100, command=firstpage).pack()
btn3 = ttk.Button(oframe, text='Аккаунт', style='my.TButton', width=100, command=secondpage).pack()

oframe.pack(side=tk.LEFT)
oframe.pack_propagate(False)
oframe.config(width=100, height=400)

# main frame
mframe = Frame(win, bg='white')

lbl10 = Label(mframe, text='<-- Выбери одну из страничек', bg='blue', fg='white').pack(padx=30)

mframe.pack(side=tk.RIGHT)
mframe.pack_propagate(False)
mframe.config(width=500, height=400)


win.mainloop()
