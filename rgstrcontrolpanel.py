import tkinter as tk
from tkinter import ttk
import mysql.connector
from RGSTRconnect import *
from RGSTRadd import *
import datetime
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
            #(i)=ttk.Entry(frame).grid(row=row,column=2)
            row+=1
        ULN=ttk.Entry(frame)
        ULN.grid(row=1,column=2)
        Firstname=ttk.Entry(frame)
        Firstname.grid(row=2,column=2)
        Lastname=ttk.Entry(frame)
        Lastname.grid(row=3,column=2)
        Form=ttk.Entry(frame)
        Form.grid(row=4,column=2)
        button=ttk.Button(frame,text='Write Card',command=lambda: writecard(ULN)).grid(column=1,row=10)
        button=ttk.Button(frame,text='Add user',command=lambda:print("test")).grid(column=2,row=10)
        button=ttk.Button(frame,text='Scan card',command=lambda:print("scan")).grid(column=3,row=10)
    def importtab(self,root,frame):
        label=ttk.Label(frame,text=".csv name")
        label.grid(row=1,column=1)
        filenameentry=ttk.Entry(frame)
        filenameentry.grid(row=1,column=2)
        log=tk.Text(frame,height='15',width='30')
        button=ttk.Button(frame,text='Import',command=lambda: importfile(filenameentry,log)).grid(column=3,row=1)
        log.grid(row=2,columnspan=4,sticky='S')
    def querytab(self,root,frame):
        buttons=("runquery","viewusers","viewstatus")
        queryentry=tk.Text(frame,height='15',width='30')
        Button=ttk.Button(frame,text="Run",command=lambda:runquery(queryentry)).grid(row=1,column=1)
        queryentry.grid(row=2,columnspan=4,sticky='S')
        label=ttk.Label(frame,text="")
        label.grid(row=3,columnspan=4,sticky='S')
def runquery(queryentry):
    query=queryentry.get('0.0','end')
    print(query)
    queryresults=tk.Tk()
    queryresults.title(title)
    queryresult=tk.Text(queryresults)
    try:
        conn=databaseconnect(configfile='config.ini')
        cursor=conn.cursor()
        cursor.execute(query)
        try:
            row=cursor.fetchall()
            for record in row:
                for data in record:
                    queryresult.insert('end',(data,"|"))
                queryresult.insert('end','\n')
                
        except:
            conn.commit()
            queryresult.insert('0.0','Query Ran')
    except:
        queryresult.insert('0.0','Error')
    queryresult.pack()
        
    
def importfile(filenameentry,log):
    log.delete('0.0','end')
    
    Datetime=datetime.datetime.now()
    try:
        filename=filenameentry.get()
        result=rgstradd(filename,Datetime)
        log.insert('0.0',result)
    except:
        log.insert('0.0',"No file found")
def writecard(ULN):
    uln=ULN.get()
    print(uln)
                
            
def main():
    root=tk.Tk()
    root.geometry(geometry)
    root.title(title)
    root.iconbitmap(icon)
    mainapp(root)
    label=ttk.Label(root,text="RGSTR Created by William Grimshaw").pack()
    root.mainloop()

main()
