from tkinter import Button, Label, Tk
import math
from simpleeval import simple_eval, NumberTooHigh

BUTTON_FONT = ("Ariel", 16, "bold")
EXTERNAL_BG_COLOR = "#5c5c5c"
DREW_COLOR = "#d6d6d6"
INNER_BG_COLOR = "#474747"
x = ""
# the mex number of chars that can be displayed
len_x = 16


def display(y):
    name = Label(bg="#333333", width=15, height=2, fg=DREW_COLOR, font=("Ariel", 30, "bold"),
                    anchor="sw", text=y)
    name.grid(row=1, column=0, columnspan=5)
    return display


def small_display(y):
    name = Label(bg="#333333", width=30, height=1, fg=DREW_COLOR, font=("Ariel", 15, "bold"),
                    anchor="sw", text=y)
    name.grid(row=0, column=0, columnspan=5)
    return small_display


class InnerButtons(Button):
    # there are 2 different classes so when a crate a member from the class i will not need to add the colors
    def __init__(self, text, row, col,  **kw):
        super().__init__(**kw)
        # inner buttons layout
        self.config(text=text, width=5, height=3, font=BUTTON_FONT, highlightthickness=0, bg=INNER_BG_COLOR,
                    fg=DREW_COLOR, activeforeground=DREW_COLOR, activebackground=INNER_BG_COLOR,
                    command=self.button_press)
        # place the button on the grid
        self.grid(row=row, column=col)

    def button_press(self):
        global x
        # prevents index error in the smell screen presentation

        small_display(x[:17]) if len(x) >= 17 else small_display(x)

        error = False
        char = self.cget("text")
        # checks if a "." can be add (its possible if the last char in x was a number)
        if char == ".":
            if x[-1] not in ("x", "^", "-", ".", "+", "/", "(", ")", "π"):
                if len(x) < len_x:
                    x += char
        # checks if a number as been pressed and if so checks if the len is not too long and checks that the first number
        # is not zero
        elif char != "=":
            if len(x) == 0 and char == "0":
                pass
            elif len(x) < len_x:
                x += char
        elif "ZeroDivisionError" in x or "NumberTooHigh" in x:
            x = ""
        # when "=" is pressed
        else:
            if len(x) > 0:
                # checks if the last char is a number and if it is will evaluate "x"
                if x[-1] in ("x", "^", "-", ".", "+", "/", "(", "√"):
                    error = True
                else:
                    # replace power symbol with the "**" chars so "x" can be evaluate
                    if "^" in x:
                        x = x.replace("^", "**")
                    # replace the time symbol with the "*" char so "x" can be evaluate
                    if "x" in x:
                        x = x.replace("x", "*")
                    # checks if all the () are closed and if not close the last one and will calculate x
                    if x.count("(") != x.count(")"):
                        x += ")"
                    # replace pi symbol with its value
                    if "π" in x:
                        # checks if there is a math operation before the pi symbol and if not add "*" for the times operation
                        # for each pi
                        res = [i for i in range(len(x)) if x.startswith("π", i)]
                        # a int to keep track of how many times a "*" as been inserted
                        loops = 0
                        for i in res:
                            if i == 0:
                                continue
                            elif x[i - 1 + loops].isdigit() or x[i - 1 + loops] == "π" or x[i - 1 + loops] == ")":
                                x = x[:i + loops] + "*" + x[i + loops:]
                                loops += 1
                        # insert the value of pi in "π" chars
                        x = x.replace("π", str(math.pi))
                    # if there is sqrt in "x" this will calculate the sqrt and write the result to "x"
                    # in its correct spot
                    if "√" in x:
                        sqr_start = x.find("√")
                        sqr_finish = x[sqr_start:].find(")") + sqr_start
                        # evaluate the exasperation inside the sqrt
                        try:
                            find_root = eval(x[sqr_start: sqr_finish+1].replace("√", "").replace(")", "").replace("(", ""))
                        except ZeroDivisionError:
                            x = "ZeroDivisionError"
                            error = True
                        else:
                            # find the sqrt
                            root = math.sqrt(find_root)
                            root = str(root)
                            # checks if there was a math operation before the sqrt and if not will add "*" for the times
                            # operation
                            if x[sqr_start - 1] not in ("/", "+", "*", "-") and x[0] != "√":
                                x = x[:sqr_start] + "*" + root + x[sqr_finish + 1:]
                            else:
                                x = x[:sqr_start] + root + x[sqr_finish + 1:]
                    if not error:
                        try:
                            x = simple_eval(x)
                        # catch zero div error
                        except ZeroDivisionError:
                            x = "ZeroDivisionError"
                        # catch number too high error from simpleeval library
                        except NumberTooHigh:
                            x = "NumberTooHigh"
                x = str(x)
                # if the number is too large to display will convert it to the scientific notation
                if len(x) > len_x and x != "ZeroDivisionError":
                    x = float(x)
                    x = f"{x:.10e}"

        display(x)


class ExternalButtons(Button):
    # there are 2 different classes so when a crate a member from the class i will not need to add the colors
    def __init__(self, text, row, col, **kw):
        super().__init__(**kw)
        self.config(text=text, width=5, height=3, font=BUTTON_FONT, highlightthickness=0, bg=EXTERNAL_BG_COLOR,
                    fg=DREW_COLOR, activeforeground=DREW_COLOR, activebackground=EXTERNAL_BG_COLOR,
                    command=self.button_press)
        self.grid(row=row, column=col)

    def button_press(self):
        global x
        # prevents index error in the smell screen presentation
        small_display(x[:17]) if len(x) >= 17 else small_display(x)

        char = self.cget("text")
        # del the last char
        if char == "⌫":
            char = ""
            if len(x) >= 0:
                # checks if there was a zerodivsion  or NumberTooHigh error and if so
                # del all the string and not just the "r" or the "h"
                if "ZeroDivisionError" in x or "NumberTooHigh" in x:
                    x = ""
                else:
                    # check if a root as been add and if so it will del the symbol "(" that been added if not will del
                    # the last char
                    if len(x) >= 2:
                        if x[-2] == "√":
                            x = x[:-2]
                        else:
                            x = x[:-1]
                    else:
                        x = x[:-1]
        # clear string button
        elif char == "C":
            char = ""
            x = ""
            small_display(x)
        # checks if a "(" can be add
        if char == "(":
            if len(x) > 0:
                if x[-1] in ("x", "^", "-", ".", "+", "/") and len(x) < len_x:
                    x += char
            else:
                x += char
        # if the char is root symbol will add "("
        elif char == "√":
            if len(x) < len_x:
                char += "("
                x += char
        # checks if a ")" can be add
        elif char == ")":
            if len(x) > 0:
                if x[-1] not in ("x", "^", "-", ".", "+", "/", "(", "√") and len(x) < len_x and "(" in x:
                    x += char

        elif char == "π":
            if len(x) < len_x:
                x += char
        # checks the last char of x and if it was in the list blow replace with the new char
        # make it that u cant enter two math operation that don't work together one after another
        else:
            if 0 < len(x) < len_x:
                if x[-1] in ("x", "^", "-", ".", "+", "/", "("):
                    if x[len(x)-2] == "√":
                        x = x[:-2]
                    else:
                        x = x[:-1]
            x += char
        # make sure the first char is a valid one
        if len(x) == 1:
            if x[0] in ("x", "^", "-", ".", "+", "/", ")"):
                x = ""
        display(x)

