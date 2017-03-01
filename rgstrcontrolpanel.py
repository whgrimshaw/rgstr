import tkinter as tk
from tkinter import ttk
import mysql.connector
from RGSTRconnect import *
from RGSTRadd import *
import datetime
import smtplib
#style
title=("RGSTR")
geometry=("250x340")
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
            text=("{}{}").format(i[0].upper(),i[1:])
            nb.add(frame,text=(text))
    def addtab(self,root,frame):
        fields=("Card ID","Firstname","Lastname","Form","Year")
        row=1
        for i in fields:
            label=ttk.Label(frame,text=i).grid(row=row,column=1)
            #(i)=ttk.Entry(frame).grid(row=row,column=2)
            row+=1
        CardID=ttk.Entry(frame)
        CardID.grid(row=1,column=2,columnspan=2)
        Firstname=ttk.Entry(frame)
        Firstname.grid(row=2,column=2,columnspan=2)
        Lastname=ttk.Entry(frame)
        Lastname.grid(row=3,column=2,columnspan=2)
        Form=ttk.Entry(frame)
        Form.grid(row=4,column=2,columnspan=2)
        Year=ttk.Entry(frame)
        Year.grid(row=5,column=2,columnspan=2)
        button=ttk.Button(frame,text='Add user',command=lambda: adduser(CardID,Firstname,Lastname,Form,Year)).grid(column=2,row=6)
    def importtab(self,root,frame):
        filenameentry=ttk.Entry(frame)
        filenameentry.grid(row=1,column=1,sticky='W')
        log=tk.Text(frame,height='15',width='30')
        button=ttk.Button(frame,text='Import',command=lambda: importfile(filenameentry,log)).grid(column=3,row=1,sticky='W')
        log.grid(row=2,columnspan=4,sticky='S')
    def querytab(self,root,frame):
        queryentry=tk.Text(frame,height='15',width='30')
        Button=ttk.Button(frame,text="Run",command=lambda:runquery(queryentry,(" "," "," "," "," "," "))).grid(row=1,column=1)
        Button=ttk.Button(frame,text="View Users",command=lambda:viewtable(queryentry,'users')).grid(row=1,column=2)
        Button=ttk.Button(frame,text="View Status",command=lambda:viewtable(queryentry,'status')).grid(row=1,column=3)
        queryentry.grid(row=2,columnspan=4,sticky='S')
        Button=ttk.Button(frame,text="Email report",command=lambda:report(queryentry)).grid(row=3,column=1)
        Button=ttk.Button(frame,text="Emergency report",command=lambda:emergencybutton(queryentry)).grid(row=3,column=2)
    def reporttab(self,root,frame):
        pass
def runquery(queryentry,columns):
    query=queryentry.get('0.0','end')
    print(query)
    queryresults=tk.Tk()
    queryresults.title(title)
    queryresult=ttk.Treeview(queryresults)
    try:
        conn=databaseconnect(configfile='config.ini')
        cursor=conn.cursor()
        cursor.execute(query)
        try:
            row=cursor.fetchall()
            queryresult['columns']=columns
            for i in queryresult['columns']:
                print (i)
                queryresult.column(i,anchor='e')
                queryresult.heading(i,text=i)
            for i, item in enumerate(row):
                queryresult.insert('','end',text=i,values=item)
        except:
            conn.commit()
            queryresult.insert('','end','Query Ran')
    except:
        queryresult.insert('','end','Error')
    queryresult.pack()
    global queryresult



def viewtable(queryentry,table):
    queryentry.delete('0.0','end')
    queryentry.insert('0.0',"SELECT *\nFROM {};".format(table))
    if table=="users":
        columns=('ID','Firstname','Lastname','Form','Year')
    elif table=="status":
        columns=('ID','Status','DateTime')
    else:
        columns=()
    runquery(queryentry,columns)

def emergencybutton(queryentry):
    queryentry.delete('0.0','end')
    queryentry.insert('0.0','SELECT users.Firstname,users.Lastname,users.Form\nFROM users,status\nWHERE users.CardID=status.CardID\nAND status.Status="0"\nORDER BY users.Form,users.Lastname,users.Firstname;')
    report(queryentry)
def report(queryentry):
    To="10wgrimshaw@huttongrammar.org,williamhenrygrimshaw@gmail.com"
    query=queryentry.get('0.0','end')
    if (query)=='SELECT users.Firstname,users.Lastname,users.Form\nFROM users,status\nWHERE users.CardID=status.CardID\nAND status.Status="0"\nORDER BY users.Form,users.Lastname,users.Firstname;':
        columns=("Firstname","Lastname","Status")
    else:
        columns=("","","","","","","","","")
    runquery(queryentry,columns)
    querydata=("")
    rows=queryresult.get_children()
    print (rows)
    for i in rows:
        columns=queryresult.set(i)
        for a in columns:
            print(columns[a])
            querydata=(querydata+columns[a]+' | ')
        querydata=(querydata+'\n')
    print(querydata)
    header= """From: RGSTR email report <from@fromdomain.com>
Subject: RGSTR report

DO NOT REPLY TO THIS EMAIL. I AM A BOT.
"""
    msg=header+querydata
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("noreplyrgstr@gmail.com", "a1b2c3a1b2c3")
    server.sendmail("noreplyrgstr@gmail.com",To, msg)
    server.quit()
        
    
def importfile(filenameentry,log):
    log.delete('0.0','end')
    
    Datetime=datetime.datetime.now()
    filename=filenameentry.get()
    result=rgstrimport(filename,Datetime)
    log.insert('0.0',result)
    #log.insert('0.0',"No file found")
def writecard(ULN):
    uln=ULN.get()
    print(uln)
def adduser(CardID,Firstname,Lastname,Form,Year):
    Datetime=datetime.datetime.now()
    CardID=CardID.get()
    Firstname=Firstname.get()
    Lastname=Lastname.get()
    Form=Form.get()
    Year=Year.get()
    print(CardID,Firstname,Lastname,Form,Year)
    rgstradd(CardID,Firstname,Lastname,Form,Year,Datetime)
            
def main():
    root=tk.Tk()
    root.geometry(geometry)
    root.title(title)
    root.iconbitmap(icon)
    mainapp(root)
    label=ttk.Label(root,text="RGSTR Created by William Grimshaw").pack()
    root.mainloop()

main()
