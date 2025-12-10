from tkinter import*
from tkinter.ttk import*
root=Tk()
root.geometry('200x150')
Style=Style()
Style.configure('TButton',
                font=('calibri',10,'bold','underline'),
                foreground='red')
btn1=Button(root,text='Quit!',
            style='TButton',
            command=root.destroy)

btn1.grid(row=0, column=3, pady=10, padx=10)
def on_click():
    print("button clicked!")

btn2=Button(root,text='click me!',command=on_click)
btn2.grid(row=1,column=3,pady=10,padx=10)
root.mainloop()
