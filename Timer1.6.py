# Import the libraries
from tkinter import *
import time
from tkinter import messagebox
from PIL import ImageTk, Image


# Create the window
win = Tk()
win.geometry('380x270')
win.title('Timer')
win.wm_iconbitmap('timer_icon.ICO')

# Set a picture for the background
bg = ImageTk.PhotoImage(Image.open('logo1.png'))
img = Label(win, image=bg, bg='red')
img.place(x=0, y=45)


# Configure the background
win.config(bg='red')


lbl_title = Label(win, width=500, text="S.M.H Naghavi",
                  fg='red', bg='yellow', font=('Lalezar', 20))
lbl_title.pack(fill=X)

set_label = Label(win, text='set timer', font=(
    'Times New Roman', 22), fg='yellow', bg='red')
set_label.place(x=240, y=70)


# Create Entry Widgets for HH MM SS
sec = StringVar()
sec_entry = Entry(win, textvariable=sec, width=2, font=(
    'Arial', 14), fg='red', bg='yellow')
sec_entry.place(x=310, y=130)

sec.set('00')
mins = StringVar()
min_entry = Entry(win, textvariable=mins, width=2, font=(
    'Arial', 14), fg='red', bg='yellow')
min_entry.place(x=280, y=130)
mins.set('00')
hrs = StringVar()
hr_entry = Entry(win, textvariable=hrs, width=2, font=(
    'Arial', 14), fg='red', bg='yellow')
hr_entry.place(x=250, y=130)
hrs.set('00')


def countdowntimer():
    global times
    set_label.config(text='')
    sec_entry.place(x=310, y=100)
    min_entry.place(x=280, y=100)
    hr_entry.place(x=250, y=100)
    times = int(hrs.get())*3600 + int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute, second = (times // 60, times % 60)
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        # Update the time
        win.update()
        time.sleep(1)
        if times == 0:
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1
        if times == 0:
            messagebox.showinfo("Timer", "Time's up.")
            set_label.config(text='set timer')
            sec_entry.place(x=310, y=130)
            min_entry.place(x=280, y=130)
            hr_entry.place(x=250, y=130)
            start_button.place(x=264, y=190)
            start_button.config(text='start', command=countdowntimer)


# Create the start button
start_button = Button(win, text='start', fg='red', bg='yellow', font=(
    'Calibry', 16), command=countdowntimer)
start_button.place(x=264, y=190)


win.mainloop()
