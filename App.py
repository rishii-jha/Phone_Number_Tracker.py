import tkinter as tk 
from time import strftime

root = tk.Tk()
root.title("Digital clock")

def time():
    string = strftime('%I:%M:%S %P \n %D')
    lable.config(text=string)
    lable.after(1000,time)

    lable = tk.Label(root, font=('calibri', 50 , 'bold'), background='yellow', foreground='black')
    lable.pack(anchor='center')

    time()
    root.mainloop()