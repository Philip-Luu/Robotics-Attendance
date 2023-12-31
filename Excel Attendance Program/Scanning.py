import tkinter as tk
terminate = False
text = ""

def scanPrompt(error):
    def submit(event):
        global text 
        text = Entry.get()
        window.destroy()

    window = tk.Tk()
    window.config(cursor = "none")
    window.title("Scan or Enter your Student ID Number")

    Error = tk.Label(text ="", font=("arial", 25))
    if error:
        Error.configure(text="\n You have not completed the requirements, either complete your team application or join teams.")
        Error.pack()
        window.after(2000, lambda: Error.pack_forget())

    

    Prompt = tk.Label(text="\n \n \n \n \n Scan or Enter your Student ID Number \n \n", font=("arial", 50), )
    Prompt.pack()
    if error == False:
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
            scanPrompt(True, False)
    elif text == "kill":
        return text[2:8]
    else:
        scanPrompt(True, False)

    