import tkinter as tk
terminate = False
text = "0"

def scanPrompt(error):
    def submit(event):
        global text 
        text = Entry.get()
        window.destroy()

    window = tk.Tk()
    window.config(cursor = "none")
    window.title("Scan or Enter your Student ID Number")

    Error = tk.Label(text ="", font=("arial", 15))
    if error:
        Error.configure(text="\n \n Please enter your student ID in the correct format, it should have a p, space, then the student number (p 80000).")


    Prompt = tk.Label(text="\n \n \n \n \n Scan or Enter your Student ID Number \n \n", font=("arial", 50), )
    Prompt.pack()

    Success = tk.Label(text="Success", font=("arial", 75), fg="green")
    Success.pack()
    window.after(2000, lambda: Success.pack_forget())


    Entry = tk.Entry(font=("arial", 35))
    Entry.bind('<Return>', submit)
    window.after(2000, lambda: Entry.pack())

    window.after(250, lambda: Entry.focus_force())
    Info = tk.Label(text="\n Contact a mentor or team leadership if you forgot your student ID for attendance corrections.")

    Info.pack()

    window.attributes('-fullscreen',True)
    window.mainloop()
    if text[0].lower() == "p":
        if text[2] == "8":
            return text[2:8]
        else:
            scanPrompt(True)
    elif text == "kill":
        return text[2:8]
    else:
        scanPrompt(True)

    