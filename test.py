import tkinter as tk

window = tk.Tk()
print("Creating window...")  # Add this line
#label = tk.Label(window, text="1")
#label.grid(row=0, column=0)

button = tk.Button(window, text="0",width=5,height=3,highlightbackground="red", highlightthickness=1)
button.grid(row=0, column=0)

button = tk.Button(window, text="1",width=5,height=3,highlightbackground="red", highlightthickness=1)
button.grid(row=0, column=1)

button = tk.Button(window, text="2",width=5,height=3,highlightbackground="red", highlightthickness=1)
button.grid(row=0, column=2)

button = tk.Button(window, text="3",width=5,height=3,highlightbackground="red", highlightthickness=1)
button.grid(row=1, column=0)

button = tk.Button(window, text="4",width=5,height=3,highlightbackground="red", highlightthickness=1)
button.grid(row=1, column=1)

button = tk.Button(window, text="5",width=5,height=3,highlightbackground="red", highlightthickness=1)
button.grid(row=1, column=2)

button = tk.Button(window, text="6",width=5,height=3,highlightbackground="red", highlightthickness=1)
button.grid(row=2, column=0)

button = tk.Button(window, text="7",width=5,height=3,highlightbackground="red", highlightthickness=1)
button.grid(row=2, column=1)


button = tk.Button(window, text="8",width=5,height=3,highlightbackground="red", highlightthickness=1)
button.grid(row=2, column=2)


button = tk.Button(window, text="9",width=5,height=3,highlightbackground="red", highlightthickness=1)
button.grid(row=3, column=1)

window.mainloop()