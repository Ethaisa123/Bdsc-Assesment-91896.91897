# importing module
from pandas import *
 
# reading CSV file
data = read_csv("main + data\data-careers.csv")
 
#this code takes the column names from the csv file and adds them to their own list in order
#this first line adds all of the names of the carrer choices and adds them to a list in the format (career1,career2,career3,ect...)
name = data['class name'].tolist()
#the next 4 lines of code do roughly the same thing but they get the "heat values" (ill explain later) instead of names in the format (1.0,3.0,2.0)
data_1 = data['commerce'].tolist()
data_2 = data['writing'].tolist()
data_3 = data['stem'].tolist()
data_4 = data['arts'].tolist()
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
for i in range (0, len(name)):
    classes_list_data[name[i]] = [data_1[i], data_2[i], data_3[i], data_4[i]] 
print(classes_list_data)


# this is a test list i did to figure out the formatting
"""
classes_list = {"programming": [10, 1, 0, 4 ],"pe": [1, 1, 10, 3],"textiles": [3, 9, 2, 3],"hisotry": [2,1,2,9],"physics":[5,0,1,7]}
"""
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
my_class = "textiles"





for i in range(0,career_ammount):
    difference_total = 0
    career = career_list_temp[i]
    
    for i in range(0,3):
        difference_total = difference_total + abs(classes_list[my_class][i] - careers[career][i])
    
    print(difference_total)
    print(career)

    if difference_total < diff_var:
        best_career = career
        diff_var = difference_total

print(best_career)


