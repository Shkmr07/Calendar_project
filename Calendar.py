# Import Library
from tkinter import *
from tkcalendar import *
# Create Object
m=Tk()

# Here, I write title name of the window
m.title("Calendar")

# Set the Geometry of the Window
m.wm_geometry("700x400")

# Here, I Perform Background color Operation
m.configure(bg="#EEDFCC")

# Add Calendar with Selectmode
c=Calendar(m,selectmode="day",year=1998,month=12,day=7)
c.pack(pady=40)

def data_fatch():
    date.config(font=("Times New Roman",12,"bold"),text="Selected Date:-"+c.get_date())

# Here, I Create Button and Label
Button(m,text="Select the Date",bg="#EEDFCC",font=("Georgia",12,"bold"),command=data_fatch).pack()
date=Label(m,text="")
date.configure(bg="#EEDFCC")
date.pack(pady=20)

# Here, I Execute tkinter
m.mainloop()

