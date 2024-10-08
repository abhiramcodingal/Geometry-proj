# Program to calculate age using tkinter

from tkinter import *
from tkcalendar import Calendar
import datetime

window = Tk()
window.title("Age Calcuator")
window.geometry("620x320")

def pick_date(event):
    global cal, date_w
    date_w = Toplevel()
    date_w.grab_set()
    date_w.title("Choose DoB")
    date_w.geometry("250x220+590+370")
    cal = Calendar(date_w, date_pattern="y-mm-dd", selectmode="day")
    cal.pack()
    ok_btn = Button(master=date_w, text="OK", bg="orange", fg="white", command=grab_date, font=("Sitka Banner", 10), width=10)
    ok_btn.pack(pady=5)

def grab_date():
    dob_entry.delete(0, END)
    dob_entry.insert(0, cal.get_date())
    date_w.destroy()
    t_age = age_func(str(dob_entry.get()))
    lbl2 = Label(frame, bg="dark blue", fg="white", text=f"Your age is {t_age}", font=("Lucida Console", 15))
    lbl2.place(x=70, y=70)
    
frame = Frame(window, width=600, height=300, bg="lightblue")
frame.place(x=10,y=10)
lbl1 = Label(frame, text="Enter your DoB:", width=15, bg="dark blue", fg="white", font=("Times New Roman", 10))
lbl1.place(x=150,y=12)
dob_entry = Entry(frame, width=15, bg="white", fg="gray1", font=("Georgia", 10))
dob_entry.place(x=320, y=12)
dob_entry.bind("<1>", pick_date)
def age_func(d):  
    today = datetime.datetime.now()
    born = datetime.datetime.strptime(d, "%Y-%m-%d")
    t_days = (today - born).days
    years = t_days // 365
    months = (t_days % 365) // 30
    days = (t_days % 365) % 30
    age = str(years) + " years " + str(months) + " months " + str(days) + " days."
    return age   

window.mainloop()