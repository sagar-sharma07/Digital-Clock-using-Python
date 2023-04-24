from tkinter import*
import time


clr="black"
clr1="white"
cdate=time.strftime("%d - %B - %Y")

def dispTime():
    ctime=time.strftime("%H : %M : %S")
    clock["text"]=ctime
    clock.after(1000,dispTime) #1000 ms =1 sec


win=Tk()

win.title("Clock App")
win.wm_iconbitmap("icons/clock.ico")
win.geometry("500x250+200+100") #WxH+x+y
win.configure(background=clr)

d=Label(text="Digital clock",font="times 24 bold",bg=clr,fg="teal")
d.pack(pady=20)

clock=Label(font="times 30 bold",bg=clr,fg=clr1,text='Time')
clock.pack(pady=30)

Label(text=cdate,font="times 12 bold",bg=clr,fg=clr1).pack()

dispTime()

win.mainloop()
                                        
