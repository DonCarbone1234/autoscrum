import selenium.common.exceptions

import test
import tkinter
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("1440x1080")

def button_pressed():
    print("rrmdspkfsd")

def ui():
    try:
        test.findNameAndNumber(text.get())
    except selenium.common.exceptions.InvalidArgumentException:
        print("Didn't work, try re-inputtng the link and make sure your jira login is correct")


text = customtkinter.StringVar()

entry_1 = customtkinter.CTkEntry(master=app, placeholder_text="URL", textvariable=text)
entry_1.pack(pady=10, padx=10)

button1 = customtkinter.CTkButton(master=app, text="test", command=ui)
button1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()

