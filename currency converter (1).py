from tkinter import *
from tkinter import ttk
converter=Tk()
converter.geometry("600x400")
converter.title("Currency Converter")
#converter.wm_iconbitmap("")
OPTIONS ={
    "US Dollar":72.10,
    "EURO":79.30,
    "British Pound":92.92,
    "AUS Dollar":49.27,
    "Canadian Dollar":54.04,
    "Singapore Dollar":52.09,
    "Swiss Franc":72.83,
    "Malaysian Ringgit":17.36,
    "Japanese Yen":0.66,
    "chinese Yuan Renminbi":10.28,
    }
def ok():
    price=rupees.get()
    answer=variable.get()
    DICT=OPTIONS.get(answer,None)
    converted=float(DICT)*float(price)
    result.delete(1.0,END)
    result.insert(INSERT,"Price In",INSERT,answer,INSERT,"=",INSERT,converted)
   
appName1 = Label(converter,text="Currency",
                font=("arial",25,"bold","underline"),fg="dark red")
appName1.grid(row=0,column=0,padx=10)
#photo = PhotoImage(file="final.png",height="",width="")
#logo = Label(converter,image=photo)
#logo.grid(row=0,column=1)
appName2=Label(converter,text="Converter",
              font=("arial",25,"bold","underline"),fg="dark red")
appName2.grid(row=0,column=2,ipadx=10)
result=Text(converter,height=5,width=50,font=("arial",10,"bold"),bd=5)
result.grid(row=1,columnspan=10,padx=3)
india=Label(converter,text="Indian Rupees:",
            font=("arial",10,"bold"),fg="red")
india.grid(row=2,column=0)
rupees=Entry(converter,font=("calibri",10))
rupees.grid(row=2,column=1)
choice=Label(converter,text="choose country:",
            font=("arial",10,"bold"),fg="red")
choice.grid(row=3,column=0)
variable=StringVar(converter)
variable.set(None)
option = OptionMenu(converter,variable,*OPTIONS)
option.grid(row=3,column=1,sticky="ew")
button = Button(converter,text="Convert",fg="green",
                font=("Calibri",20),bg="powder blue",command=ok)
button.grid(row=3,column=2)


mainloop()
