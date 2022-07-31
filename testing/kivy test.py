from tkinter import *

ws = Tk()
ws.title('PythonGuides')


img = PhotoImage(file='main + data\images\-ace.png')
Label(
    ws,
    image=img
).place(x=10,y=10)

ws.mainloop()