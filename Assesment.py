
#the list is formatted as [class, tech_value, arts_value, health, writing_value]
classes = {"programming": [10, 1, 0, 4 ],"pe": [1, 1, 10, 3],"textiles": [3, 9, 2, 3],"hisotry": [2,1,2,9],"physics":[5,0,1,7]}
careers = {"programming":[10, 1, 0, 4 ],"pe": [1, 1, 10, 3],"textiles": [3, 9, 2, 3],"hisotry": [2,1,2,9],"physics":[5,0,1,7]}

#creating a temporary list from the keys of the dicctionary

def getList(dict):
    return list(dict.keys())

# Driver program
classes_list_temp = getList(classes)
print(type(classes_list_temp))


career_list_temp = getList(careers)
print(type(career_list_temp))
#chosen_career = input("What is you chosen career")
diff_var = 100000
best_class = ""
#print(careers[chosen_career])


difference_total = 0


#VARIABLES DEFINED
my_class = "hisotry"
career = career_list_temp[0]
#
class_num = len(classes_list_temp)
print(class_num)
print(classes_list_temp)

for i in range(0,class_num):
    print(i)
    print(career_list_temp[i])
    career = career_list_temp[i]
    my_class = classes_list_temp[i]
    for i in range(0,4):
        
        #print("class attribute: {}" .format(classes[my_class][i]))
        #print("career attribute: {}".format(careers[career][i]))
        difference_total = difference_total + abs(classes[my_class][i] - careers[career][i])

    #print("differences: " + str(differences))
    print("currentclass: {}" .format(best_class))
    print("current difference: " + str(difference_total))
    if difference_total < diff_var:
        best_class = my_class
        
        diff_var = difference_total
        print("lowwest difference:{} \n" .format(my_class))
    print("lowwest difference: {}" .format(diff_var))

print("THE BEST CLASS IS: {}" .format(best_class))

