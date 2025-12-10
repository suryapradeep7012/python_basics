import tkinter as tk
def clicked():
    print("Button clicked")
def cancel():
    print("Template Closing....")
    rt.destroy()
rt = tk.Tk()
rt.geometry('100x100')
b1=tk.Button(rt,text="Submit",bd=5,bg='green',command=clicked)
cancel_b2=tk.Button(rt,text="Cancel",bd=5,bg='red',command=cancel)
b1.pack()
cancel_b2.pack()
rt.mainloop()
