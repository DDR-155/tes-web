
from tkinter import *
from time import strftime
root = Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title('We are your solution')
root.configure(bg='black')
def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(10, time)
mark = Label(root, background='black',font = ('DS-Digital', 70, 'bold'),
            pady=150,
            foreground = 'red')
mark.pack(anchor = 'center')
# mark.configure(bg='black')
Label(root,background='black', text = 'IT Infrastructure and Contractor',foreground='white', font ='arial 15 bold').pack(side=BOTTOM)
Label(root,background='black', text = 'Morin & Jasatekindo',foreground='white', font ='kabel 20 bold',pady=30).pack(side=BOTTOM)
time()
mainloop()
