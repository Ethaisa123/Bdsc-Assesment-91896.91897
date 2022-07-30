from ast import Pass
from cProfile import label
import tkinter as tk
from tkinter import *
from tkinter import ttk
from pandas import *
global name_careers
data = read_csv("main + data\data-careers.csv")
name_careers = data['career name'].tolist()

root = Tk()
root.geometry("600x700")
root.resizable(False, False)
root.title("test page")

global items
items = ["Test_list", "Test_list1", "Test_list2"]
canvas = Canvas(root,height=155,width=750)
canvas.pack()
#Styles for the varios headers and button widgets
style = ttk.Style()
style.theme_use('clam')

style.configure("button_arrow.TButton", font=('MT Extra', 20), relief="flat" ,foreground="#056", background="White")
style.configure("button_con.TButton", font=('cocogoose', 20), relief="flat" ,foreground="white", background="#087", border="black", bordercolor = "black")
style.configure("TEntry", relief="flat" ,foreground="#000", background="#087")
style.configure("TMenubutton", font=('arial', 15), foreground="black", background="White")

global page_num
page_num = 0


def clear_page():
        print("clear")
        root.delete



def button_comfirm():
        global page_num
        page_num = 1
        print("page move please")

        for widgets in root.winfo_children():
          print(widgets)
          if str(widgets) != ".!canvas":
                widgets.destroy()
        update_page()



def button_left():
        global page_num
        if page_num == 1:
                page_num = 3
        else:
                page_num -= 1
        update_page()

def button_right():
        global page_num
        if page_num >= 3:
                page_num = 1
        else:
                page_num += 1
        update_page()

def start_screen():
        #adds the button variabe
        global button

        #place label
        lable = tk.Label(root, text = "Full name:", font=('arial 25'), fg = "teal")
        lable.place(x=7,y=200)
        
        lable = tk.Label(root, text = "Age:", font=('arial 25'), fg = "teal")
        lable.place(x=10,y=300)

        lable = tk.Label(root, text = "Desired Career:", font=('arial 25'), fg = "teal")
        lable.place(x=5,y=400)
        global lable_title
        lable_title = tk.Label(canvas, text = "Select Career Goal.", font=('biko 50 bold'),bg = "teal", fg = "white")
        lable_title.place(x=10,y=1)
        global lable_subhead
        lable_subhead = tk.Label(canvas, text = "Career selection screen.", font=('arial 40'),bg = "teal", fg = "white")
        lable_subhead.place(x=10,y=90)
        #adds the rectangle
        canvas.create_rectangle(0, 0, 1000, 155, outline="teal", fill="teal")
        button = ttk.Button(root, text = "Confirm", command=button_comfirm, style = "button_con.TButton")
        button.pack(side = BOTTOM, pady=20)
        #adds cambobox
        
        

        variable = StringVar(root)
        variable.set(0)

        variable = StringVar(root)
        variable.set(name_careers[0])

        w = ttk.OptionMenu(root, variable, *name_careers, style = "TMenubutton")
        w.place(x=10,y=450)

        
        
        #defines how the temporary text in the textbos will dissapear
        def temp_text(e):
           entry.delete(0,"end")
        #adding text box
        entry = ttk.Entry(root, text = "", font=('arial 15'), style = "TEntry", width= 20)
        #temporary text is inserted
        entry.insert(0, "Full name")
        entry.place(x=10,y=260)
        #entry.pack(side = LEFT, padx = 10)
        #when user clicks the box the temporary text is deleted
        entry.bind("<FocusIn>", temp_text)

        #defines how the temporary text in the textbos will dissapear
        def temp_text2(e):
           entry2.delete(0,"end")
        #adding text box
        entry2 = ttk.Entry(root, text = "", font=('arial 15'), style = "TEntry", width= 5)
        #temporary text is inserted
        entry2.insert(0, "Age")
        entry2.place(x=10,y=360)
        #entry.pack(side = LEFT, padx = 10)
        #when user clicks the box the temporary text is deleted
        entry2.bind("<FocusIn>", temp_text2)




def screen_1():
        button = ttk.Button(root,text= ">",command=button_right, style = "button_arrow.TButton")
        button.place(y=655,x=450)
        button = ttk.Button(root,text= "<",command=button_left, style = "button_arrow.TButton")
        button.place(y=655,x=0)
        



def update_page():
        global page_num
        print(page_num)
        if page_num == 0:
                start_screen()
        elif page_num == 1:
                screen_1()
                lable_subhead["text"] = "Classtype1"
                lable_title["text"] = "Suggested Class 1:"
        elif page_num == 2:
                screen_1()
                lable_subhead["text"] = "Classtype2"
                lable_title["text"] = "Suggested Class 2:"
        elif page_num == 3:
                screen_1()
                lable_subhead["text"] = "Classtype3"
                lable_title["text"] = "Suggested Class 3:"
        else:
                lable = tk.Label(canvas, text = "A major error has occured please restart the programm.", font=('arial 40'),bg = "teal", fg = "white")
                lable.place(x=10,y=90)
        

update_page()






if __name__ == '__main__':
        root.mainloop()