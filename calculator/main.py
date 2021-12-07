from tkinter import Tk
from sy_nu_buttons import ExternalButtons, InnerButtons, display, small_display

# ---------------------------- UI SETUP ------------------------------- #
# screen config
screen = Tk()
screen.title("Calculator")
screen.config(bg="#333333", padx=3, pady=3)

# make the display
display = display("")
small_display = small_display("")

# buttons layout
bracket_button = ExternalButtons("(", 2, 0)
bracket_button1 = ExternalButtons(")", 2, 1)
pow_button = ExternalButtons("^", 2, 2)
clear_button = ExternalButtons("C", 2, 3)
del_button = ExternalButtons("⌫", 2, 4)
div_button = ExternalButtons("/", 4, 3)
mul_button = ExternalButtons("x", 3, 3)
plus_button = ExternalButtons("+", 5, 3)
minus_button = ExternalButtons("-", 6, 3)
pi_button = ExternalButtons("π", 3, 4)
sqr_button = ExternalButtons("√", 4, 4)
empty_button2 = ExternalButtons("", 5, 4)
empty_button2.config(state="disabled")
empty_button3 = ExternalButtons("", 6, 4)
empty_button3.config(state="disabled")

dot_button = InnerButtons(".", 6, 0)
eql_button = InnerButtons("=", 6, 2)

nu_0_button = InnerButtons("0", 6, 1)
nu_1_button = InnerButtons("1", 5, 0)
nu_2_button = InnerButtons("2", 5, 1)
nu_3_button = InnerButtons("3", 5, 2)
nu_4_button = InnerButtons("4", 4, 0)
nu_5_button = InnerButtons("5", 4, 1)
nu_6_button = InnerButtons("6", 4, 2)
nu_7_button = InnerButtons("7", 3, 0)
nu_8_button = InnerButtons("8", 3, 1)
nu_9_button = InnerButtons("9", 3, 2)

# make the window pop at the center(ish) of the screen
screen.resizable(False, False)
windowWidth = screen.winfo_reqwidth()
windowHeight = screen.winfo_reqheight()
positionRight = int(screen.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(screen.winfo_screenheight()/2 - windowHeight/2 - 100)
screen.geometry(f"+{positionRight}+{positionDown}")

screen.mainloop()
