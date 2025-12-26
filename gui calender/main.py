from tkinter import *
import calendar

def show_calendar():
    year = year_entry.get()

    if not year.isdigit():
        error_label.config(text="Enter a valid year")
        return

    year = int(year)
    error_label.config(text="")

    cal_window = Toplevel(root)
    cal_window.title("Year Calendar")
    cal_window.geometry("560x600")
    cal_window.config(bg="light pink")

    cal_data = calendar.calendar(year)

    cal_label = Label(
        cal_window,
        text=cal_data,
        font=("Courier", 11),
        bg="light pink",
        justify=LEFT
    )
    cal_label.pack(padx=20, pady=20)


root = Tk()
root.title("GUI Calendar")
root.geometry("300x200")
root.config(bg="yellow")
root.resizable(False, False)

title = Label(
    root,
    text="CALENDAR",
    font=("Arial", 18, "bold"),
    bg="yellow"
)
title.pack(pady=10)

year_label = Label(
    root,
    text="Enter the Year",
    font=("Arial", 14),
    bg="yellow"
)
year_label.pack()

year_entry = Entry(
    root,
    font=("Arial", 14),
    width=10,
    justify="center"
)
year_entry.pack(pady=5)

show_btn = Button(
    root,
    text="Show Calendar",
    font=("Arial", 13, "bold"),
    bg="black",
    fg="white",
    command=show_calendar
)
show_btn.pack(pady=10)

error_label = Label(
    root,
    text="",
    font=("Arial", 12),
    fg="red",
    bg="yellow"
)
error_label.pack()

root.mainloop()
