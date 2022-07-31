# importing module
from pandas import *
 
# Sets the csv file to a variable
data = read_csv("main + data\data-classes.csv")
 
 #sets the colums of the csv file to their own lists
name_classes = data['class name'].tolist()
data_1_cl = data['commerce'].tolist()
data_2_cl = data['writing'].tolist()
data_3_cl = data['stem'].tolist()
data_4_cl = data['arts'].tolist()

classes_list_data = {}

#adds the lists and the name from the csv file and adds them to a dictionary in the format {NAME: [data1,data2,data3,data4]}
for i in range (0, len(name_classes)):
    classes_list_data[name_classes[i]] = [data_1_cl[i], data_2_cl[i], data_3_cl[i], data_4_cl[i]] 

my_career = "Social Work Health Practice"

# simmilar code to the class lists but with careers
data = read_csv("main + data\data-careers.csv")
name_careers = data['career name'].tolist()
data_1_cr = data['commerce'].tolist()
data_2_cr = data['writing'].tolist()
data_3_cr = data['stem'].tolist()
data_4_cr = data['arts'].tolist()
careers_list_data = {}
for i in range (0, len(name_careers)):
    careers_list_data[name_careers[i]] = [data_1_cr[i], data_2_cr[i], data_3_cr[i], data_4_cr[i]] 
placement = name_careers.index("Youth Work")
p_career = careers_list_data[name_careers[placement]]

#defining variables used in sorting
total = 0
difference_list = {}


#takes the values from the chosen career and compares them against different class outcomes
for i in range(0,len(name_classes)):
    curr_name = name_classes[i]
    class_data = classes_list_data[curr_name]
    difference = 0
    for i in range(0,4):
        difference = abs(p_career[i] - class_data[i])
        total = total + difference
    difference_list[curr_name] = total
    total = 0
#sorts the outcomes from the best to worst in terms of compatibility and usability
difference_list = {k: v for k, v in sorted(difference_list.items(), key=lambda item: item[1])}
print(difference_list)
