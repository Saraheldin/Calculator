import tkinter as tk

window = tk.Tk()

window.title("Calculator")

print("Creating window...")  # Add this line
#label = tk.Label(window, text="1")
#label.grid(row=0, column=0)
   
variable=""

def button_click(number):
    global variable
    variable +=str(number)
    print(variable);
    display_label.config(text=variable)

def clear():
    global variable
    variable=""
    display_label.config(text=variable)

def operator(op):
    global variable
    if  variable and variable[-1] not in "+-*/":
        variable+=str(op)
        display_label.config(text=variable)


     

def equal():
    global variable
    try:
     result = str(eval(variable))
     variable = result
     display_label.config(text=variable)
    except (SyntaxError, ZeroDivisionError, NameError):
     variable = "Error"
     display_label.config(text=f"Error: {e}")

button = tk.Button(window, text="0",width=5,height=3,highlightbackground="red", highlightthickness=1,command=lambda : button_click(0))
button.grid(row=0, column=0)

button = tk.Button(window, text="1",width=5,height=3,highlightbackground="red", highlightthickness=1,command=lambda : button_click(1))
button.grid(row=0, column=1)

button = tk.Button(window, text="2",width=5,height=3,highlightbackground="red", highlightthickness=1,command=lambda : button_click(2))
button.grid(row=0, column=2)

button = tk.Button(window, text="3",width=5,height=3,highlightbackground="red", highlightthickness=1,command=lambda : button_click(3))
button.grid(row=1, column=0)

button = tk.Button(window, text="4",width=5,height=3,highlightbackground="red", highlightthickness=1,command=lambda : button_click(4))
button.grid(row=1, column=1)

button = tk.Button(window, text="5",width=5,height=3,highlightbackground="red", highlightthickness=1,command=lambda : button_click(5))
button.grid(row=1, column=2)

button = tk.Button(window, text="6",width=5,height=3,highlightbackground="red", highlightthickness=1,command=lambda : button_click(6))
button.grid(row=2, column=0)

button = tk.Button(window, text="7",width=5,height=3,highlightbackground="red", highlightthickness=1,command=lambda : button_click(7))
button.grid(row=2, column=1)


button = tk.Button(window, text="8",width=5,height=3,highlightbackground="red", highlightthickness=1,command=lambda : button_click(8))
button.grid(row=2, column=2)


button = tk.Button(window, text="9",width=5,height=3,highlightbackground="red", highlightthickness=1,command=lambda : button_click(9))
button.grid(row=3, column=1)

button=tk.Button(window,text='clear',width=5,height=3,highlightbackground="red", highlightthickness=1,command=clear)
button.grid(row=3, column=0)

button=tk.Button(window,text='+',width=5,height=3,highlightbackground="red", highlightthickness=1,command=lambda:operator("+"))
button.grid(row=3, column=2)

button=tk.Button(window,text='-',width=5,height=3,highlightbackground="red", highlightthickness=1,command=lambda:operator("-"))
button.grid(row=4, column=1)

button=tk.Button(window,text='*',width=5,height=3,highlightbackground="red", highlightthickness=1,command=lambda:operator("*"))
button.grid(row=4, column=2)

button=tk.Button(window,text='=',width=5,height=3,highlightbackground="red", highlightthickness=1,command=equal)
button.grid(row=4, column=0)


display_label=tk.Label(window,text="",width=10,height=3)
display_label.grid(row=5,column=0,columnspan=3)

window.mainloop()
