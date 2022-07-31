from cProfile import label
import operator
import tkinter as tk
from tkinter import *
from tkinter import ttk
from pandas import *
from operator import itemgetter

global items
global check
check = False
root = Tk()
root.geometry("600x700")
root.resizable(False, False)
root.title("test page")
canvas = Canvas(root,height=155,width=750)
canvas.pack()

#adding images





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
        #print("clear")
        root.delete


# Sets the csv file to a variable

data = read_csv("main + data\data-classes.csv")

#sets the colums of the csv file to their own lists
global name_classes
global type_cl
global description_cl
name_classes = data["class name"].tolist()
data_1_cl = data["commerce"].tolist()
data_2_cl = data["writing"].tolist()
data_3_cl = data["stem"].tolist()
data_4_cl = data["arts"].tolist()
type_cl = data["type"].tolist()
description_cl = data["description"].tolist()

global classes_list_data
classes_list_data = {}

#adds the lists and the name from the csv file and adds them to a dictionary in the format {NAME: [data1,data2,data3,data4]}
for i in range (0, len(name_classes)):
        classes_list_data[name_classes[i]] = [data_1_cl[i], data_2_cl[i], data_3_cl[i], data_4_cl[i]] 

my_career = "Social Work Health Practice"

# simmilar code to the class lists but with careers
data = read_csv("main + data\data-careers.csv")
name_careers = data["career name"].tolist()
data_1_cr = data["commerce"].tolist()
data_2_cr = data["writing"].tolist()
data_3_cr = data["stem"].tolist()
data_4_cr = data["arts"].tolist()
careers_list_data = {}
for i in range (0, len(name_careers)):
        careers_list_data[name_careers[i]] = [data_1_cr[i], data_2_cr[i], data_3_cr[i], data_4_cr[i]] 



#takes the values from the chosen career and compares them against different class outcomes



def calc_class(name_classes, classes_list_data,p_career):
        total = 0
        global difference_list
        difference_list = {}
        for i in range(0,len(name_classes)):
                curr_name = name_classes[i]
                class_data = classes_list_data[curr_name]
                difference = 0
                for i in range(0,4):
                        difference = abs(p_career[i] - class_data[i])
                        total = total + difference
                print("name : {}, data : {}".format(curr_name, class_data))
                difference_list[curr_name] = total
                total = 0
        #sorts the outcomes from the best to worst in terms of compatibility and usability
        difference_list = dict(sorted(difference_list.items(),key=operator.itemgetter(1)))
        print(difference_list)

def calc_top(difference_list):
        global difference_top
        global screen_1_info
        global screen_2_info
        global screen_3_info
        difference_top = list(difference_list.keys())
        difference_top = [difference_top[0], difference_top[1] ,difference_top[2]]
        pos = name_classes.index(difference_top[0])
        screen_1_info = [difference_top[0], description_cl[pos], type_cl[pos]]
        pos = name_classes.index(difference_top[1])
        screen_2_info = [difference_top[1], description_cl[pos], type_cl[pos]]
        pos = name_classes.index(difference_top[2])
        screen_3_info = [difference_top[2], description_cl[pos], type_cl[pos]]
        
def button_comfirm():
        global check
        #print(check)
        
        

        if entry2.get().isdigit() == True:
                age = int(entry2.get())
                if age < 0 or age > 100:
                        lable = tk.Label(root, text = "Age must be a number between 0 and 100", font=('arial 8'), fg = "red")
                        lable.place(x=10,y=390)
                        return                       
        else:
                
                lable = tk.Label(root, text = "Age must be a number between 0 and 100", font=('arial 8'), fg = "red")
                lable.place(x=10,y=390)
                return
        if entry.get() == "Full name":
                lable = tk.Label(root, text = "Name cannot be Full name", font=('arial 8'), fg = "red")
                lable.place(x=10,y=240)
                return
        
        if check == True:
                pass
        elif age < 16 or age > 25:
                lable = tk.Label(root, text = "At your current age the results may be inacurate", font=('arial 8'), fg = "green")
                lable.place(x=10,y=390)
                check = True
                return

        
        global desc
        global page_num
        page_num = 1
        placement = name_careers.index(variable.get())
        p_career = careers_list_data[name_careers[placement]]
        calc_class(name_classes, classes_list_data,p_career)
        calc_top(difference_list)
        for widgets in root.winfo_children():
          if str(widgets) != ".!canvas":
                widgets.destroy()
        """
        canvas2 = Canvas(root,height=100,width=400)
        canvas2.pack(side = BOTTOM, pady=50)
        canvas2.create_rectangle(0, 10, 100, 400, outline="teal", fill="teal")
        """
        desc = tk.Label(root, text = "", font=('arial 15'), fg = "white" , bg = "teal", wraplength = 400,justify= "left")
        desc.pack(side = BOTTOM, pady=50)
        lable_subhead.config(font=('arial 20'),wraplength = 600, justify= "left")
        lable_title.config(font = ("biko 30 bold"), wraplength = 600, justify= "left")
        lable_title.place(x=5,y=3)
        lable_subhead.place(x=5,y=115)
        def image_chs(name_img):
                print(name_img)
                if name_img.find("Social") != -1:
                        return PhotoImage(file='main + data\images\scocial_sci.png')
                elif name_img.find("science/software") != -1:
                        return PhotoImage(file='main + data\images\Engineering.png')
                elif name_img.find("Sports") != -1 or name_img.find("Education") != -1:
                        return PhotoImage(file='main + data\images\education.png')
                elif name_img.find("Arts") != -1:
                        return PhotoImage(file='main + data\images\-art.png')
                elif name_img.find("science") != -1:
                        return PhotoImage(file='main + data\images\science.png')
                elif name_img.find("Engineering") != -1:
                        return PhotoImage(file='main + data\images\Engineering.png')
                else:
                        return PhotoImage(file='main + data\images\math.png')
        global img2
        global img1
        global img3
        global backround
        print(str(screen_1_info[2]))
        print(str(screen_2_info[2]))
        print(str(screen_3_info[2]))
        img1 = image_chs(str(screen_1_info[2]))
        img2 = image_chs(str(screen_2_info[2]))
        img3 = image_chs(str(screen_3_info[2]))
        backround = Label(root,image=img1,width=500,height=400)
        backround.lower(desc)
        backround.place(x=50,y=210)
        update_page()





#print
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
        
     
        
        global variable
        variable = StringVar(root)
        variable.set(0)
        variable = StringVar(root)
        variable.set(name_careers[0])
        dropdown = ttk.OptionMenu(root, variable, *name_careers, style = "TMenubutton")
        dropdown.place(x=10,y=450)
        
        global entry
        global entry2
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
        #print(page_num)
        if page_num == 0:
                start_screen()
        elif page_num == 1:
                screen_1()
                lable_subhead["text"] = "Class type: {}" .format(screen_1_info[2])
                lable_title["text"] = "Suggested Class 1:{}" .format(screen_1_info[0])
                desc["text"] = screen_1_info[1]
                backround["image"] = img1
        elif page_num == 2:
                screen_1()
                lable_subhead["text"] = "Class type: {}" .format(screen_2_info[2])
                lable_title["text"] = "Suggested Class 1:{}" .format(screen_2_info[0])
                desc["text"] = screen_2_info[1]
                backround["image"] = img2
        elif page_num == 3:
                lable_subhead["text"] = "Class type: {}" .format(screen_3_info[2])
                lable_title["text"] = "Suggested Class 1:{}" .format(screen_3_info[0])
                desc["text"] = screen_3_info[1]
                backround["image"] = img3

        else:
                lable = tk.Label(canvas, text = "A major error has occured please restart the programm.", font=('arial 40'),bg = "teal", fg = "white")
                lable.place(x=10,y=90)
        

update_page()






if __name__ == '__main__':
        root.mainloop()