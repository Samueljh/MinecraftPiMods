# -*- coding: utf-8 -*-
import minecraft.minecraft as minecraft
import minecraft.block as block
import time
from Tkinter import *
from Tkinter import StringVar
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
root = Tk()


def sayhi():
    mc.postToChat('[Guest] Hi')
    time.sleep(2)
    
def saybye():
    mc.postToChat('[Guest] Bye!')
    time.sleep(2)

def askwhere():
    mc.postToChat('[Guest] Where Are You?')
    time.sleep(2)

def saywhere():
    pos = mc.player.getTilePos()
    mc.postToChat("[Guest] I'm at: ")
    mc.postToChat(pos)
    time.sleep(2)

bname=StringVar()
def newbutton():
    newbutton=Entry(root, textvariable=bname)
    newbutton.pack(side=LEFT)
    addbutton=Button(root,text='Add', command=addnbutton)
    addbutton.pack(side=LEFT)
def addnbutton():
    butname=bname.get()
    addbutton=Button(root,text= butname, command=saycustom)
    addbutton.pack(side=LEFT)
    
def sayinput():
    rettext=var.get()
    mc.postToChat(rettext)
    time.sleep(2)

def saycustom():
    butname=bname.get()
    mc.postToChat(butname)
    time.sleep(2)

def stopscrpt():
    quit()
#menu
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New Button", command=newbutton)
filemenu.add_command(label="Close",command=stopscrpt)
menubar.add_cascade(label="File",menu=filemenu)
root.config(menu=menubar)

var = StringVar()
root.title('SimpleChat')
#messages
startbutton = Button(root, text='Hi', command=sayhi)
startbutton.pack(side=LEFT)

startbutton = Button(root, text='Where Are You?', command=askwhere)
startbutton.pack(side=LEFT)

startbutton = Button(root, text="I'm At <pos>", command=saywhere)
startbutton.pack(side=LEFT)

startbutton = Button(root, text='Bye!', command=saybye)
startbutton.pack(side=LEFT)

inputchat = Entry(root, textvariable=var, cursor= 'arrow')
inputchat.pack(side=LEFT)

startbutton = Button(root, text='<--- Say', command=sayinput)
startbutton.pack(side=LEFT)

#stop chat button
stopsbutton = Button(root, text='End SinpleChat', command=stopscrpt, fg = "yellow", bg = "Red")
stopsbutton.pack(side=LEFT)


root.mainloop()
