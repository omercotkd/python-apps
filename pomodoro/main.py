import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    timer_text.config(text="Timer", fg=GREEN)
    background.itemconfig(TIMER_TEXT, text="00:00")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_text.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_text.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps
    global timer
    count_min = int(count / 60)
    count_sec = str(count % 60)
    if len(count_sec) == 1:
        count_sec = "0" + count_sec

    background.itemconfig(TIMER_TEXT, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            text = CHECK_MARK * int(reps / 2)
            check_marks.config(text=text)

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_text = tk.Label()
timer_text.config(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer_text.grid(row=0, column=1)

background = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
background.create_image(100, 112, image=tomato_img)
TIMER_TEXT = background.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
background.grid(row=1, column=1)

start_button = tk.Button()
start_button.config(text="Start", font=("ariel", 12, "normal"), highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=0)

reset_button = tk.Button()
reset_button.config(text="Reset", font=("ariel", 12, "normal"), highlightthickness=0, command=reset_timer)
reset_button.grid(row=3, column=2)

check_marks = tk.Label()
check_marks.config(font=(FONT_NAME, 22, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(row=4, column=1)


window.mainloop()
