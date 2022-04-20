import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
import time
from tkinter import messagebox as mb
from tkinter.ttk import Combobox

def end():
    c['state'] = DISABLED
    o['state'] = DISABLED
    g['state'] = DISABLED
    pop['state'] = DISABLED
    u.create_text(70, 470, text='Hello: ' + (o.get()), font=('Gabriola', 15), fill="brown4")
    #end = Label(root,  font=('Gabriola', 15), fg='brown4', text='Hello: ' + (o.get()))
    #end.place(x= 50,y=400)

    u.create_text(83, 500,  text='Your psw: ' + (g.get()), font=('Gabriola', 15), fill="brown4")
    #end1 = Label(root,  font=('Gabriola', 15), fg='brown4', text='Your psw: ' + (g.get()))
    #end1.place(x= 50,y=435)


def click():
    s = tx.get()
    if not s.isdigit():
        mb.showerror("Error ","Numbers needed!")
    p = int(tx.get())
    x = 8923
    if p == x:
        for i in range(100):
            root.update_idletasks()
            b['value'] += 1
            time.sleep(0.001)
            t['text'] = b['value'], '%'
        r = Label(root, text='100%    Successful!', font='Modern',  fg='red',bg='aliceblue')
        r.place(x=250, y=41)
        messagebox.showinfo(title="ClubHouse", message='Access is opened!')
    else:
        for i in range(85):
            root.update_idletasks()
            b['value'] += 1
            time.sleep(0.01)
            t['text'] = b['value'], '%'
        b.stop()
        answer = mb.askretrycancel(title="Password is incorrect",message="        Retry?")
        if answer:
            entry.delete(0, END)
        root.quit()
    tx['state']= DISABLED
    bt['state'] = DISABLED

    q = Progressbar(root, length=300, style='red.Horizontal.TProgressbar')
    q['value'] = 0
    h = Label(root, text='0%    connecting to the server...', font='Modern',  fg='red',bg='aliceblue')
    h.place(x=120, y=100)
    root.update()
    q.place(x=50, y=80)
    for i in range(100):
        root.update_idletasks()
        q['value'] += 1
        time.sleep(0.05)
        h['text'] = q['value'], '%'
    r = Label(root, text='   Сonnected to the \n   https:\clubhouse', font='Modern',  fg='red',bg='aliceblue')
    r.place(x=120, y=100)
    u.create_text(200, 200, text="ClubHouse",  font=('Gabriola', 40), fill="Red")
    #l = Label(root, text="ClubHouse",  font=('Gabriola', 40), fg = 'red')
    #l.place(x =110, y = 130)

    u.create_text(50, 250,text="Gender",  font=('Gabriola', 15), fill="brown4")
    #v = Label(root, text="Gender",  font=('Gabriola', 15), fg = 'brown4')
    #v.place(x =10, y = 220)

    global c
    c=Combobox(root, width=7, justify='center' )
    c['values']=('Male', 'Female')
    c.place(x=90, y=240)


    u.create_text(50, 300, text="Username", font=('Gabriola', 15), fill="brown4")
    #lbl = Label(root, text="Username", font=('Gabriola', 15), fg = 'brown4')
    #lbl.place(x =10, y = 250)
    global o
    o = Entry(root, fg='brown4',  justify="center",  bg='aliceblue')
    o.place(x =90, y = 290)


    u.create_text(50, 350, text="Password",  font=('Gabriola', 15), fill="brown4")
    #d = Label(root, text="Password",  font=('Gabriola', 15), fg = 'brown4')
    #d.place(x =10, y = 280)
    global g
    g = Entry(root, fg='brown4',  justify="center", bg='aliceblue')
    g.place(x =90, y = 340)

    global pop
    pop = Button(root, text="Sign Up!", font='Gabriola', bg="navajo white", activeforeground='white', foreground="brown4",activebackground="green", command=end)
    pop.place(x =300, y = 280)
    pop['relief'] = GROOVE
    pop['overrelief'] = RAISED


def clicked ():
        s = txt.get()
        if not s.isdigit():
            mb.showerror("Error","Numbers needed!")
        v = int(txt.get())
        if v >= 10 and v <= 16:
            for i in range(100):
                root.update_idletasks()
                bar['value'] += 1
                time.sleep(0.01)
                g['text'] = bar['value'], '%'
            messagebox.showwarning(title="ClubHouse" , message='Let us think!')
            root.quit()
        elif v >= 16 and v <= 100:
            for i in range(100):
                root.update_idletasks()
                bar['value'] += 1
                time.sleep(0.01)
                g['text'] = bar['value'], '%'
            c = Label(root, text='100%    Successful!', font='Modern', fg='red', bg='aliceblue')
            c.place(x=250, y=4)
            # messagebox.showinfo(title="ClubHouse" , message='Welcome!')
            #lb = Label(root, text="Invite Code",font='Modern')
            #lb.grid(column=0, row=2)

            u.create_text(40, 50, text="Invite Code", font='Modern', fill="Black")

            global b
            b = Progressbar(root, length=70, style='black.Horizontal.TProgressbar')
            b['value'] = 0
            root.update()
            b.place(x=170, y=44)

            global t
            t = Label(root, text='0%       Checking...',font='Modern',  fg='red',bg='aliceblue')
            t.place(x=250, y=41)

            global tx
            tx = Entry(root, width=4,fg='red',font='Modern', justify="center",  bg='aliceblue')
            tx.place(x=80, y=40)

            global bt
            bt = Button(root, text="Check!",font='Modern',bg="navajo white", activeforeground='white' ,foreground="red",activebackground="green", command=click)
            bt.place(x=119, y=37)
            bt['relief'] = GROOVE
            bt['overrelief'] = RAISED
        else:
            for i in range(100):
                root.update_idletasks()
                bar['value'] += 1
                time.sleep(0.01)
                g['text'] = bar['value'], '%'
            messagebox.showerror(title="ClubHouse" , message='Sorry you can not enter ! or your age is wrong!')
            root.quit()
        txt['state']= DISABLED
        btn['state'] = DISABLED

root = Tk()
img = PhotoImage(file="F:\П\p1.gif")
u = Canvas(width=400, height=600)
u.place(x=0,y=0)
u.create_image(200, 450, image=img)
#c.create_text(40, 10, text="  Your Age",font='Modern' ,fill="Black")


#label = Label(root, image=img, width=400, height=800)
#label.image_ref = img
#label.place(x=0,y=0)

root.title("ClubHouse")
root.geometry('400x600+600+200')
root.resizable (False,False)

style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='green')

bar = Progressbar(root, length=70, style='black.Horizontal.TProgressbar')
bar['value'] = 0
root.update()
bar.place(x=170,y=7)

g = Label(root,text='0%    waiting...',font='Modern',  fg='red', bg='aliceblue')
g.place(x=250, y=4)
u.create_text(30, 15, text="  Your Age",font='Modern' ,fill="Black")
#l = Label(root, text="  Your Age  ",font='Modern')
#l.grid(column=0, row=1)

txt = Entry(root, width=4, fg='red',justify="center",font='Modern',bg='aliceblue')
txt.place(x= 80,y=5)
txt['relief']=SUNKEN

btn = Button(root, text="Check!",font='Modern',bg="navajo white", activeforeground='white' ,foreground="red",activebackground="green",command=clicked)
btn.place(x=119,y=1)
btn['relief']=GROOVE
btn['overrelief']=RAISED

root.mainloop()
