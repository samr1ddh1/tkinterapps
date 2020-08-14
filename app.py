import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []


def addApps():

    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("executables","*.exe"),("all files","*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height= 250, width =300, bg="#2634D2")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8,relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Select File", bg="#2634D2", fg="white", padx=10, pady=5, command=addApps)
runApps = tk.Button(root, text="Run Apps", bg="#2634D2", fg="white", padx=10, pady=5, command=runApps)
openFile.pack()

runApps.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')