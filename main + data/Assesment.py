# importing module
from numpy import diff
from pandas import *
 
#FORMATTING THE LIST OF CLASSES AVALILE FROM THE EXCEL/CVS FILE
# reading CSV file of the classes
data = read_csv("main + data\data-classes.csv")
 
#this code takes the column names from the csv file and adds them to their own list in order
#this first line adds all of the names of the carrer choices and adds them to a list in the format (career1,career2,career3,ect...)
name_classes = data['class name'].tolist()
#the next 4 lines of code do roughly the same thing but they get the "heat values" (ill explain later) instead of names in the format (1.0,3.0,2.0)
data_1_cl = data['commerce'].tolist()
data_2_cl = data['writing'].tolist()
data_3_cl = data['stem'].tolist()
data_4_cl = data['arts'].tolist()
#these lists are made in such a way that the first variable of each list match and and so on from each concecutive pair


# this is testing code that is used to make sure the values are lined up correctly
"""
name_list = ('class name', name)
print('commerce', data_1)
print('writing', data_2)
print('stem', data_3)
print('arts', data_4)
print(name_list)
"""
#this is the final dictionary that the excel file will be writen to
classes_list_data = {}

#this code takes the data from name and data lists and turns them into a format that is easily usable in future code the format is {"name of class: [int1,int2,int3,int4]"} (the ints corrispond to heat values)
for i in range (0, len(name_classes)):
    classes_list_data[name_classes[i]] = [data_1_cl[i], data_2_cl[i], data_3_cl[i], data_4_cl[i]] 
#print(classes_list_data)


#chosing variable
my_career = "Social Work Health Practice"


# This code does the same thing but with different variables
data = read_csv("main + data\data-careers.csv")
name_careers = data['career name'].tolist()
data_1_cr = data['commerce'].tolist()
data_2_cr = data['writing'].tolist()
data_3_cr = data['stem'].tolist()
data_4_cr = data['arts'].tolist()
careers_list_data = {}
for i in range (0, len(name_careers)):
    careers_list_data[name_careers[i]] = [data_1_cr[i], data_2_cr[i], data_3_cr[i], data_4_cr[i]] 
placement = name_careers.index("Marketing")
total = 0
#finding diff
difference_list = {}
p_career = careers_list_data[name_careers[placement]]
for i in range(0,len(name_classes)):
    curr_name = name_classes[i]
    class_data = classes_list_data[curr_name]
    difference = 0
    for i in range(0,4):
        difference = abs(p_career[i] - class_data[i])
        total = total + difference
    difference_list[curr_name] = total
    total = 0
difference_list = {k: v for k, v in sorted(difference_list.items(), key=lambda item: item[1])}
print(difference_list)
"""
for i in range(0,len(name_careers)):  
    current_name = name_careers[i]  
    diff = 0
    for i in range(0,3):
        diff =+ abs([my_career][i] - classes_list_data[current_name][i])

    difference_list[name_careers[i]] =  diff
print(difference_list)

    

classes_list = {"programming": [10, 1, 0, 4 ],"pe": [1, 1, 10, 3],"textiles": [3, 9, 2, 3],"hisotry": [2,1,2,9],"physics":[5,0,1,7]}

careers = {"programming":[10, 1, 0, 4 ],"pe": [1, 1, 10, 3],"textiles": [3, 9, 2, 3],"hisotry": [2,1,2,9],"physics":[5,0,1,7]}

#this code creats a temporary list from the keys of the dicctionary

def getList(dict):
    return list(dict.keys())

# Driver program
classes_list_temp = getList(classes_list_data)
print(type(classes_list_temp))

#what
career_list_temp = getList(careers)
print(type(career_list_temp))

#chosen_career = input("What is you chosen career")
diff_var = 100000000

#print(careers[chosen_career])
career_ammount = len(career_list_temp)





#YOU CHOOSE THIS VARIABLE
my_class = "Business Information Analytics"





for i in range(0,career_ammount):
    difference_total = 0
    career = career_list_temp[i]
    
    for i in range(0,3):
        difference_total = difference_total + abs(classes_list_data[my_class][i] - careers[career][i])
    
    print(difference_total)
    print(career)

    if difference_total < diff_var:
        best_career = career
        diff_var = difference_total

print(best_career)
"""

