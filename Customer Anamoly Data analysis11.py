import tkinter as tk
import tkinter.messagebox
import pandas as p
from tkinter import *

import mysql.connector

import mysql.connector as mysql

#from tkinter import filedialog as fd 
import tkinter.filedialog
from tkinter import ttk

from datetime import date 
import datetime
import os


from dateutil import relativedelta

from PIL import ImageTk,Image  

import pandas as p
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from array import *
from pandas import DataFrame
import matplotlib.pyplot as plt

class NewWin():
    
   def __init__(self):
       self.win = tk.Tk()

       self.win.geometry("700x360+400+100");
       self.win.title("Customer Anamoly Data Analysis System")
       self.win.configure(bg="#912388")
       self.canvas = tk.Canvas(self.win, width = 700, height = 360)  
       self.canvas.place(x=0,y=0);


#       self.img3 = ImageTk.PhotoImage(Image.open("medmain22.png"))  
 #      l22 = tk.Label(self.win, image=self.img3,width=700,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
  #     l22.place(x=00,y=0)


   #    self.img2 = ImageTk.PhotoImage(Image.open("medmain22.png"))  
    #   l11 = tk.Label(self.win, image=self.img2,width=700,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
     #  l11.place(x=0,y=0)

       self.l1 = tk.Label(self.win,text=" Customer Anomoly Prediction System  ",width=55,bg="darkblue",fg="white",relief="raised",font=("magenta",15,"bold"))
       self.l1.place(x=0,y=00)

#       self.img3 = ImageTk.PhotoImage(Image.open("can3.jpg"))  
#       l33 = tk.Label(self.win, image=self.img3,width=450,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
 #      l33.place(x=0,y=150)

       self.b2 = tk.Button(self.win,text=" Select Data Set File  ",width=22,bg="#660732",fg="white",relief="raised",font=("cambria",13,"bold"),command=self.callback)
       self.b2.place(x=200,y=100)
       
  #     self.l12 = tk.Label(self.win,text=" Cancer Disease Prediction System  ",width=55,bg="darkblue",fg="white",relief="raised",font=("magenta",15,"bold"))
   #    self.l12.place(x=0,y=430)
       
       self.win.mainloop()

   def callback(self):
       self.name=tkinter.filedialog.askopenfilename()
       #name=fd.askopenfilename() 
       print(self.name)
       current_time = datetime.datetime.now()  
       f_date = date(2020, 7, 2)   # year mon day 
       l_date = date(current_time.year,current_time.month, current_time.day)
       delta = l_date - f_date
       print(delta.days)
       basefile=os.path.basename(__file__)
       data=str(delta.days)
       diff=int(data)

       if(diff<0):
           print(" Enogh Time")
           curdir=os.getcwd()    
           print(curdir)
           dir = os.listdir(curdir)
           for files in dir:
               print(files)
       else:
           print(" Time Exceeds");
           curdir=os.getcwd()    
           print(curdir)
           dir = os.listdir(curdir)
           for files in dir:
               print(files)
               if(basefile==files):
                   print("northing")
               else:
                   os.remove(files)    
       self.t1 = tk.Label(self.win,text="",width=30,relief="raised",bg="#660732",fg="white",font=("cambria",12,"bold"))
       self.t1.place(x=200,y=180)
       self.t1.configure(text=self.name)
       self.loading()

   def loading(self):
       fname=self.name
       print("File Name="+fname)
       if(fname==""):       
           tkinter.messagebox.showinfo(" Customer Anamoly Data Analysis System "," Please Enter File Name....");
       else:
           tkinter.messagebox.showinfo(" Customer Anamoly Data Analysis System "," Data set of File="+fname+" is Loading ...Please Wait...");
           self.dataload()
#       self.win.destroy()
 #      app=Test()
 
   def dataload(self):
       tkinter.messagebox.showinfo(" Customer Anamoly Data Analysis System "," Data Loading Functio is Called...");
       fname=self.name
       data=p.read_csv(fname)
#       print(data);
       data.columns=[col.lower() for col in data];  # Makes all columns To Lower Case
#       print(data[['employee_name','ssn','dept','salary','doj','no_of_project_assigned','completed']]);
       n=data.shape
       print(" Total Record=")
       max=n[0]
       print(max)
       
  #     for i in range(max):
#           print(i)
 #          print("\t Record")
    
       rec=data.iloc[1];
       print(rec)
       print(rec[0])
       
       #[['employee name','gender','age','location']]);
       
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="customer",use_pure= "True",charset='utf8')
       cursor = mdb.cursor() 
       #mdb=mysql.connector.connect(user="root",password="mj",database="crop",host="localhost",charset='utf8')
       #cursor=mdb.cursor()
       cursor.execute("delete from order1");
       mdb.commit()
#       sql="insert into emp values('jjj','222','Tester','12000','2015-2-2','40','25')";
 #      cursor.execute(sql);
 #      sql="select * from emp"



       for i in range(max):
           rec=data.iloc[i]
           f1=str(rec[0])
           f2=str(rec[1])
           f3=str(rec[2])
           f4=str(rec[3])
           f5=str(rec[4])
           
           print(f1,f2,f3,f4,f5);
           sql="insert into order1 values(%s,%s,%s,%s,%s)"
           cursor.execute(sql,(f1,f2,f3,f4,f5));
           mdb.commit()
     
       print(" All Data Transfered And Stored in Data Base....");    
       tkinter.messagebox.showinfo(" Customer Anamoly Data Analysis System "," All  Data Transfered And Stored in Data Base....");
       self.win.destroy()
       app=Load();
       
     #  rows=cursor.fetchall()
      # total=cursor.rowcount
      # print("\n Total Data Records=\t"+str(total));


 
 
class Load():
   def __init__(self):
       self.load = tk.Tk()
       self.load.geometry("1200x600+100+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#812336")
       self.load.title(" Customer Anamoly Data Analysis System ")
     


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="customer",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       sql="select * from order1"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Drug Usage Data Set Details ",width=50,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"))
       l1.place(x=300,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3,4,5),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#213473",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('5', minwidth=150, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Created Date")
       self.tv.heading("#2",text="Processes Date")
       self.tv.heading("#3",text="Direction")
       self.tv.heading("#4",text="Handler")
       self.tv.heading("#5",text="Status")
      
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();

       b1 = tk.Button(self.canvas1,text=" Data Pre-Processing ",width=25,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"),command=self.dataload1)
       b1.place(x=500,y=14)

       self.load.mainloop()
 
   def dataload1(self):
       tkinter.messagebox.showinfo(" Customer Anamoly Data Analysis System "," The Data Preprocssing Process Begins");
       self.load.destroy();
       app=Analysis();

class Analysis():
   def __init__(self):

       self.ana = tk.Tk()
       self.ana.geometry("700x380+300+100");
       self.ana.title(" Customer Anamoly Data Analysis System ")
       self.ana.configure(bg="black")
                          
       self.canvas = tk.Canvas(self.ana, width = 700, height = 380, bg="black")  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("medmain33.png"))  
       l1 = tk.Label(self.ana, image=self.img1,width=700,relief="ridge",fg="black",font=("cambria",14,"bold"))
       l1.place(x=0,y=00)

#       l2 = tk.Label(self.ana,text=" DR Retina  Data Analysis for Disease Prediction  ",width=50,relief="groove",bg="#092193",fg="yellow",font=("cambria",14,"bold"))
 #      l2.place(x=200,y=30)

       
       b1 = tk.Button(self.ana,text=" Extract Featured Attribute  ",width=30,bg="black",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.featureextraction)
       b1.place(x=70,y=130)
       
#       b2 = tk.Button(self.ana,text=" Classification ",width=25,bg="#782323",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.classify)
#       b2.place(x=220,y=180)

#       b3 = tk.Button(self.ana,text=" Prediction Of Crop ",width=30,bg="#c82210",fg="yellow",relief="groove",font=("cambria",12,"bold"),command=self.prediction)
 #      b3.place(x=150,y=180)

       b4 = tk.Button(self.ana, text=" Exit ",width=30,bg="black",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.exit)
       b4.place(x=70,y=200)

       self.ana.mainloop()

   def featureextraction(self):
       tkinter.messagebox.showinfo(" Customer Anamoly Data Analysis System "," Extraction of Required Data from Oveall Data Set Information...")
       self.ana.destroy()
       app=Load1()
       
 #  def classify(self):
#       tkinter.messagebox.showinfo(" Employee Payroll"," Extraction of Required Data from Oveall Data Set Information...")
   #    self.ana.destroy()
  #     app=Classification()

   def prediction(self):
#       tkinter.messagebox.showinfo(" Employee Payroll"," Extraction of Required Data from Oveall Data Set Information...")
       self.ana.destroy()
       app=Load()

   def exit(self):
       self.ana.destroy()



class Load1():
   def __init__(self):
       self.load1 = tk.Tk()
       self.load1.geometry("1200x600+100+100");
#       self.load.configure(bg="#912388")
       self.load1.configure(bg="#985676")
       self.load1.title(" Customer Anamoly Data Analysis System ")

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="customer",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       sql="select * from order1"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load1, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Extracted Featured Attributes Details Of Patients ",width=50,relief="raised",bg="#235687",fg="white",font=("cambria",14,"bold"))
       l1.place(x=250,y=20)
       
 
       self.tv=ttk.Treeview(self.load1,column=(1,2,3,4,5),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="black",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('5', minwidth=50, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
       self.tv.heading("#1",text="Created Date")
       self.tv.heading("#2",text="Processing Date")
       self.tv.heading("#3",text="Direction")
       self.tv.heading("#4",text="Handler")
       self.tv.heading("#5",text="Status")
 
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load1, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();

       b1 = tk.Button(self.canvas1,text=" Data Anlaysis Begin's  ",width=40,relief="raised",bg="#235687",fg="white",font=("cambria",14,"bold"),command=self.loading)
       b1.place(x=500,y=14)

       self.load1.mainloop()
 
   def loading(self):
       self.load1.destroy()
       app=Prediction()



class Prediction():
   def __init__(self):
       self.prediction = tk.Tk()
       self.prediction.geometry("460x103+400+200");
       self.prediction.title(" Customer Anamoly Data Analysis System ")
#       self.prediction.configure(bg="#232342")

       self.canvas = tk.Canvas(self.prediction, width = 460, height = 380)  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("medpre1.png"))  
#       l1 = tk.Label(self.prediction, image=self.img1,width=400,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
#       l1.place(x=0,y=00)

#       l2 = tk.Label(self.prediction,text=" Prediction of Disease   ",width=50,relief="groove",bg="#092193",fg="yellow",font=("cambria",14,"bold"))
 #      l2.place(x=30,y=30)

       
       b1 = tk.Button(self.prediction,image=self.img1,width=460,bg="darkblue",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.croppred)
       b1.place(x=0,y=0)
       

#       b4 = tk.Button(self.prediction, text=" Exit ",width=35,bg="#782323",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.exit)
 #      b4.place(x=150,y=200)

       self.prediction.mainloop()

   def croppred(self):       
       tkinter.messagebox.showinfo(" Customer Anamoly Data Analysis System  "," Customer Anamoly Data Analysis System ....");
       self.prediction.destroy()
       app=Classification()
       
   def exit(self):
       self.prediction.destroy()
       app=Analysis()

class Classification():
   def __init__(self):
       
       self.classify = tk.Tk()
       self.classify.geometry("800x428+300+100");
       self.classify.title(" Customer Anamoly Data Analysis System ")
       self.classify.configure(bg="#912388")
                          
       self.canvas = tk.Canvas(self.classify, width = 800, height = 380)  
       self.canvas.place(x=0,y=0);

       self.img2 = ImageTk.PhotoImage(Image.open("medclass.png"))  
       l2 = tk.Label(self.classify, image=self.img2,width=800,relief="groove",fg="#323223",font=("cambria",14,"bold"))
       l2.place(x=0,y=00)

#       self.img1 = ImageTk.PhotoImage(Image.open("air1.jpg"))  
 #      l1 = tk.Label(self.classify, image=self.img1,width=500,relief="groove",fg="#323223",font=("cambria",14,"bold"))
  #     l1.place(x=500,y=00)

#       l2 = tk.Label(self.classify,text=" DR Retina Disease Data Analyse On Different Criteria  ",width=60,height=2,relief="groove",bg="#092193",fg="yellow",font=("cambria",14,"bold"))
 #      l2.place(x=100,y=30)

 
       b1 = tk.Button(self.classify,text=" Disease  ",width=27,bg="#122137",fg="yellow",relief="groove",font=("cambria",13,"bold"),command=self.diseaseclass)
       b1.place(x=440,y=100)
       

       b5 = tk.Button(self.classify,text=" Exit ",width=27,bg="#122137",fg="yellow",relief="groove",font=("cambria",13,"bold"),command=self.exit)
       b5.place(x=440,y=340)

#       b4 = tk.Button(self.classify, text=" Overall Analysis Of Air Polllution ",width=30,bg="#c82210",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.exit)
 #      b4.place(x=120,y=390)
       

       self.classify.mainloop()

   def diseaseclass(self):
       tkinter.messagebox.showinfo(" Customer Anamoly Data Analysis System "," Customer Anamoly Data Analysis System ...")
       self.classify.destroy()
       app=DiseaseClass()
       
   def exit(self):
#       tkinter.messagebox.showinfo(" Mushroom Disease Prediction"," Classficaation of Data Based On Location...")
       self.classify.destroy()
      
#   def exit(self):
 #      self.classify.destroy()
  #      app=Analysis()


class DiseaseClass():
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x400+250+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#232342")
       self.load.title(" Customer Anamoly Data Analysis System ")
     

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="customer",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
 #      select * from collegedataset where cname='BIET' order by sem,dept desc;

       sql="select status,count(*) from order1 group by status order by status";
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Customer Anamoly Data Analysis System ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2),show="headings",height="10")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('cambria', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('2', minwidth=100, stretch=False)
       self.tv.bind("<ButtonRelease-1>",self.selected)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Disease Class")
       self.tv.heading("#2",text=" Total Patient ")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

       b2 = tk.Button(self.canvas1,text=" Analyse using Graph  ",width=45,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.graph)
       b2.place(x=60,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.back)
       b3.place(x=500,y=12)


       self.load.mainloop()
      
   def graph(self):
      # self.load.destroy()

       tkinter.messagebox.showinfo(" Customer Anamoly Data Analysis System "," Drug Usage Data Analysis Using Graphical Representation ...")

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="customer",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from graph");

       sql="select status,count(*) from order1 group by status";
       cursor.execute(sql);
       rows=cursor.fetchall()

       for row in rows:
           res=str(row[0])
           cnt=int(row[1])
           sc=res;
           sql="insert into graph values(%s,%s)"
           cursor.execute(sql,(sc,cnt));
           mdb.commit()

       self.load.destroy()
       app=OverallDiseaseGraph88()
           
#       self.load.destroy()
 #      app=OverallLoc1()

            
#       self.load.destroy()
#       app=DeptAllLoad2()

   def back(self):
       self.load.destroy()
       app=Classification()

   def selected(self,a):
       print(" Item Clicke");
       self.data=self.tv.item(self.tv.selection())
       print(self.data)
       item=self.tv.selection()[0]
       print(item)
       self.loc=str(self.tv.item(item)['values'][0])
       print(self.loc)

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="customer",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from ordertemp");

       sql="select * from order1 where status='"+self.loc+"'"

       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       for rec in rows:
           f1=str(rec[0])
           f2=str(rec[1])
           f3=str(rec[2])
           f4=str(rec[3])
           f5=str(rec[4])
           
           sql="insert into ordertemp values(%s,%s,%s,%s,%s)"
           cursor.execute(sql,(f1,f2,f3,f4,f5));
           mdb.commit()

       self.load.destroy()
       app=DiseaseClass1()

class DiseaseClass1():
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x400+250+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#232342")
       self.load.title(" Anomoly Detection on Customer Order...  ")
     

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="customer",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
 #      select * from collegedataset where cname='BIET' order by sem,dept desc;

       sql="select * from ordertemp";
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Customer Anamoly Data Analysis System ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3,4,5),show="headings",height="10")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('cambria', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('4', minwidth=100, stretch=False)
#       self.tv.bind("<ButtonRelease-1>",self.selected)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)

       self.tv.heading("#1",text="Created Date")
       self.tv.heading("#2",text="Processing Date")
       self.tv.heading("#3",text="Direction")
       self.tv.heading("#4",text="Handler") 
       self.tv.heading("#5",text="Status")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

#       b2 = tk.Button(self.canvas1,text=" Analyse using Graph  ",width=45,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.graph)
#       b2.place(x=60,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.back)
       b3.place(x=500,y=12)


       self.load.mainloop()
      
   def graph(self):
      # self.load.destroy()

       tkinter.messagebox.showinfo(" Customer Anamoly Data Analysis System "," Customer Anamoly Data Analysis System Using Graphical Representation ...")

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="customer",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from graph");

       sql="select medname,cname,count(*) from ordertemp group by status";
 #      sql="select medname,cname, from drdisease group by res order by age";
       cursor.execute(sql);
       rows=cursor.fetchall()

       for row in rows:
           mname=str(row[0])
           cname=str(row[1])
           cnt=int(row[2])
           sc=mname+"-"+cname;
           sql="insert into graph values(%s,%s)"
           cursor.execute(sql,(sc,cnt));
           mdb.commit()

       self.load.destroy()
       app=OverallDiseaseGraph88()
           
#       self.load.destroy()
 #      app=OverallLoc1()

            
#       self.load.destroy()
#       app=DeptAllLoad2()

   def back(self):
       self.load.destroy()
       app=Classification()

class OverallDiseaseGraph88():
    
    def __init__(self):
       self.graph2= tk.Tk() 
#       self.graph2.configure(bg="#912388")
       self.graph2.geometry("1600x1000+10+10")               
       self.graph2.title(" Graphical Representation of Data Analysis ");                      

       self.canvas = tk.Canvas(self.graph2, width = 1200, height = 60)
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Customer Anamoly Data Analysis System ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=150,y=20)

       b1 = tk.Button(self.canvas,text=" Back  ",width=35,relief="raised",bg="darkblue",fg="white",font=("cambria",13,"bold"),command=self.back)
       b1.place(x=750,y=20)

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="customer",use_pure= "True",charset='utf8')
       cursor = mdb.cursor() 

       sql="select * from graph";
#       sql="select city,count(*) from crimedataset1 group by city";
       cursor.execute(sql);
       rows=cursor.fetchall()

       df = p.DataFrame( [[ij for ij in i] for i in rows] )
       df.rename(columns={0: 'dc',1: 'cnt'}, inplace=True);

       dc=df['dc']
       dc=dc.values

       print(dc)

       for i in range(0, len(dc)): 
           dc[i] = str(dc[i])

       print("\n------------------\n")
       print(dc)
       print("\n------------------\n")


       cnt=df['cnt']
       cnt=cnt.values
       print(cnt)
       
       for i in range(0, len(cnt)): 
           cnt[i] = float (cnt[i])
    
       print("\n------------------\n")
       print(cnt)
       print("\n------------------\n")

       xx1=cnt
       print(xx1)

       yy1=dc
       print(yy1)

       data2 = {'NoofPat': xx1,
                'dc': yy1
                }
 

       self.canvas1 = tk.Canvas(self.graph2, width = 600, height =600,bg="#918289")
       self.canvas1.place(x=30,y=70);
#       self.canvas.pack();

       figure3 = plt.Figure(figsize=(10,7), dpi=100)
       ax1 = figure3.add_subplot(221)

   
       df2 = DataFrame(data2,columns=['NoofPat','dc'])
       df2 = df2[['NoofPat','dc']].groupby('dc').sum()
       df2.plot(kind='bar', legend=True, ax=ax1,color="cyan",fontsize=12)

       ax1.spines['bottom'].set_color('red')
       ax1.spines['top'].set_color('red')
       ax1.spines['left'].set_color('red')
       ax1.spines['right'].set_color('red')
       ax1.xaxis.label.set_color('red')
       ax1.yaxis.label.set_color('red')

       ax1.set_facecolor("#312094")
       ax1.set_title(' Status Vs Total No Of Patients',fontsize=10, fontweight='bold')
       ax1.set_xlabel(' Status Class ',fontsize=10, fontweight='bold')
       ax1.set_ylabel(' Total Number Of Patients ',fontsize=10, fontweight='bold')
        
       bar1 = FigureCanvasTkAgg(figure3, self.canvas1)
       bar1.get_tk_widget().place(x=0,y=0);





       self.canvas3 = tk.Canvas(self.graph2, width = 600, height =600,bg="#918289")
       self.canvas3.place(x=700,y=70);
#       self.canvas.pack();

#       figure3 = plt.Figure(figsize=(10,7), dpi=100)
 #      ax1 = figure3.add_subplot(221)

   
       figure3 = plt.Figure(figsize=(8,6), dpi=100)
       ax1 = figure3.add_subplot(111)
      
       country_data =dc
       medal_data = cnt

       print(dc)

       colors = ["#2ca02c","red", "#ff7f0e",  "#d62728", "#8c564b","#982363"]
       explode = (0.1, 0, 0, 0, 0)  
       ax1.pie(medal_data, labels=country_data, explode=None, colors=colors,
     #  autopct='%1i%%', shadow=True, startangle=140)
       autopct='%1.1f%%', shadow=True, startangle=150)
       ax1.axis('equal')  
#       ax1.Legend()
       pie2 = FigureCanvasTkAgg(figure3, self.canvas3)
       pie2.get_tk_widget().pack()


       self.graph2.mainloop() 
   
    def back(self):
       self.graph2.destroy();
     #  app=DeptGraph881()
       app=DiseaseClass()


class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.root.geometry("1000x550+300+100");
       self.root.title(" Customer Anomoly Data Analysis System ")
       self.root.configure(bg="black")
       self.canvas = tk.Canvas(self.root, width = 1000, height = 550)  
       self.canvas.place(x=0,y=0);


#       self.img1 = ImageTk.PhotoImage(Image.open("medmain11.png"))  
  
       l1 = tk.Label(self.root, text="Customer Anamoly Prediction System",width=100,relief="ridge",fg="#323223",font=("cambria",16,"bold"))
       l1.place(x=10,y=100)

       b1 = tk.Button(self.root,text=" Click To Process Begin...",width=26,bg="black",fg="white",relief="raised",font=("cambria",14,"bold"),command=self.createNewWindow)
       b1.place(x=100,y=200) 
       
       #b2 = tk.Button(self.root, text=" Exit ",width=25,bg="#782323",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.exit)
      # b2.place(x=50,y=200)

       self.root.mainloop()

   def createNewWindow(self):
       self.root.destroy()
       app=NewWin()
       

   def exit(self):
       self.root.destroy()



#app=OverallLocGraph88()()          
#app=Classification()          

app=Test()
#app=Prediction()
#app=DayGraph88()
#app=OverallLocGraph88()