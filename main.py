from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
text =""
timer=None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    reps=0
    text=""
    window.after_cancel(timer)
    check_label.config(text="")
    Timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_Timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec= LONG_BREAK_MIN *60
    reps += 1
    if reps % 8 ==0:
        # If it´s the 8st/16rd/32th rep:
        print("Long break")
        countdown(long_break_sec)

    elif reps % 2 == 1:
        Timer_label.config(text="WORK", fg=GREEN)
        print("Work sec")
        # If it´s the 1st,3rd/5th rep:
        countdown(work_sec)
    else:
        print("Short Break")
        Timer_label.config(text="Break", fg=PINK)
        # If it´s the 2st,4rd/6th rep:
        countdown(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global reps
    global text
    global timer
    count_min =math.floor(count/60)
    count_sec = count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(10,countdown,count-1)
    else:
        if reps % 2 == 0:
            text += "✓"
            check_label.config(text=text)
        start_Timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100,pady=50, bg =YELLOW)
window.title("Pomodoro")

canvas = Canvas(width=200, height=224 , bg = YELLOW, highlightthickness=0)
tomato_img =PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)

Timer_label = Label()
Timer_label.config(text="Timer", bg=YELLOW,fg=GREEN, font=(FONT_NAME,35,"bold"))
Timer_label.grid(row=0, column=1)

start_button = Button()
start_button.config(text="Start", highlightthickness=0,command=start_Timer)
start_button.grid(row=2,column=0)

stop_button = Button()
stop_button.config(text="Reset", highlightthickness=0,command=reset_timer)
stop_button.grid(row=2,column=2)

check_label = Label()
check_label.config( bg=YELLOW, fg=GREEN, font=(FONT_NAME,30,"bold"))
check_label.grid(row=3,column=1)
window.mainloop()