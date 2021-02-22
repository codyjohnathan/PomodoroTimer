import time
import datetime as dt

import tkinter
from tkinter import messagebox

import winsound


#  Setting up our individual times
current_time = dt.datetime.now()  # Our current time
pomodoro = 25 * 60  # Our Pomodorro timer
delta_time = dt.timedelta(0, pomodoro)
future_time = current_time + delta_time
break_time = 5 * 60
finish_break = current_time + \
    dt.delta_time(0, pomodoro + break_time)  # break finishes


root = tkinter.Tk()
# Hiding tkinter's box
root.withdraw()

messagebox.showinfo("Pomodoro started!", "\n Time:" +
                    current_time.strftime("%H:%M") + " hrs. \n Timer set for 25 mins")

total_pomodoros = 0
breaks = 0

while True:

    if current_time < future_time:
        print("Pomodoro")

    elif future_time <= current_time <= finish_break:
        print("In break")
        if breaks == 0:
            print("if break")

            for i in range(5):
                winsound.Beep((i+100), 500)
            print("Break time!")
            breaks += 1

    else:
        print("Finished")

        breaks = 0

        for i in range(10):
            winsound.Beep((i+100), 500)

        ans = messagebox.askyesno(
            "Timer finished. Nice job!\n Would you like to start another Pomodoro?")
        total_pomodoros += 1

        if ans == True:
            current_time = dt.datetime.now()  # Our current time
            future_time = current_time + dt.timedelta(0, pomodoro)
            finish_break = current_time + \
                dt.delta_time(0, pomodoro + break_time)
            continue

        elif ans == False:
            messagebox.showinfo(
                "Pomodoro finished\n You have completed str(total_pomodoros)today.")
            break

        print("Sleeping")

        time.sleep(20)
        current_time = dt.datetime.now()

        now = current_time.strftime("%H:%M")
