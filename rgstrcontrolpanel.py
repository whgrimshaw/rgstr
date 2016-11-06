import tkinter as tk
from tkinter import ttk

#style
title=("RGSTR")
geometry=("300x330")
icon=('favicon.ico')
class mainapp:
    def __init__(self,root):
        self.createnotebook(root)
    def createnotebook(self,root):
        nb=ttk.Notebook(root)
        nb.pack(fill='both',expand='true')
        nb.enable_traversal()
        self.createtabs(nb,root)
    def createtabs(self,nb,root):
        tabs=("add","import","query")
        for i in tabs:
            frame=ttk.Frame(nb,name=i)
            frame.pack(fill='both',expand='true')
            if i =="add":
                self.addtab(root,frame)
            elif i =="import":
                self.importtab(root,frame)
            elif i =='query':
                self.querytab(root,frame)
            else:
                break
            nb.add(frame,text=i)
    def addtab(self,root,frame):
        fields=("ULN","Firstname","Lastname","Form")
        row=1
        for i in fields:
            label=ttk.Label(frame,text=i).grid(row=row,column=1)
            (i)=ttk.Entry(frame).grid(row=row,column=2)
            row+=1
        button=ttk.Button(frame,text='Write Card',command=lambda: print(ULN.get())).grid(column=1,row=10)
        button=ttk.Button(frame,text='Add user',command=lambda:print("test")).grid(column=2,row=10)
        button=ttk.Button(frame,text='Scan card',command=lambda:print("scan")).grid(column=3,row=10)
    def importtab(self,root,frame):
        label=ttk.Label(frame,text=".csv name")
        label.grid(row=1,column=1)
        filenameentry=ttk.Entry(frame)
        filenameentry.grid(row=1,column=2)
        button=ttk.Button(frame,text='Import',command=lambda:print("import")).grid(column=3,row=1)
        log=tk.Text(frame,height='15',width='30')
        log.grid(row=2,columnspan=4,sticky='S')
    def querytab(self,root,frame):
        buttons=("runquery","viewusers","viewstatus")
        column=1
        for i in buttons:
            print(i)
            (i)=ttk.Button(frame,text=i).grid(row=1,column=column)
            column+=1
        queryentry=tk.Text(frame,height='15',width='30')
        queryentry.grid(row=2,columnspan=4,sticky='S')
        label=ttk.Label(frame,text="")
        label.grid(row=3,columnspan=4,sticky='S')
    def runquery(self,frame,queryentry):
        query=queryentry.get()
        print(query)

def main():
    root=tk.Tk()
    root.geometry(geometry)
    root.title(title)
    root.iconbitmap(icon)
    mainapp(root)
    label=ttk.Label(root,text="RGSTR Created by William Grimshaw").pack()
    root.mainloop()

main()
