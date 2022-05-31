#collect data from datasheets and adds them to dictionarys
import pandas as pd

df = pd.read_excel('filename.xlsm', sheetname=0) # can also index sheet by name or fetch all sheets
mylist = df['column name'].tolist()



#the list is formatted as [class, tech_value, arts_value, health, writing_value]
classes_list = {"programming": [10, 1, 0, 4 ],"pe": [1, 1, 10, 3],"textiles": [3, 9, 2, 3],"hisotry": [2,1,2,9],"physics":[5,0,1,7]}
careers = {"programming":[10, 1, 0, 4 ],"pe": [1, 1, 10, 3],"textiles": [3, 9, 2, 3],"hisotry": [2,1,2,9],"physics":[5,0,1,7]}

#creating a temporary list from the keys of the dicctionary

def getList(dict):
    return list(dict.keys())

# Driver program
classes_list_temp = getList(classes_list)
print(type(classes_list_temp))

#
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


