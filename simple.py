import tkinter as tk

base = tk.Tk()
menu_bar = tk.Menu(base)

file =  tk.Menu(menu_bar,tearoff= 0)
menu_bar.add_cascade(label ="File",menu=file)
file.add_command(label ="save",command=None)
file.add_separator()
file.add_command(label ="Exit",command=base.destroy)

edit =  tk.Menu(menu_bar,tearoff= 0)
menu_bar.add_cascade(label ="Edit",menu=edit)
edit.add_command(label ="copy",command=None)
edit.add_command(label ="paste",command=base.destroy)

base.config(menu = menu_bar)
base.mainloop()