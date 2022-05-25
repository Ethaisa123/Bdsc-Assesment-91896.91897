
#the list is formatted as [class, tech_value, arts_value, health, writing_value]
classes = {"programming": [10, 1, 0, 4 ],"pe": [1, 1, 10, 3],"textiles": [3, 9, 2, 3],"hisotry": [2,1,2,9],"physics":[5,0,1,7]}
careers = {"programming":[10, 1, 0, 4 ],"pe": [1, 1, 10, 3],"textiles": [3, 9, 2, 3],"hisotry": [2,1,2,9],"physics":[5,0,1,7]}


#chosen_career = input("What is you chosen career")

#print(careers[chosen_career])

print(classes["programming"][0])
print(careers["programming"][0])
differences = []
difference_total = 0


print("for i in: \n")
my_class = "hisotry"
career = "textiles"

for i in range (0, len(classes)):
    print(classes[])

for i in range(0,4):
    
    print("class attribute: {}" .format(classes[my_class][i]))
    print("career attribute: {}".format(careers[career][i]))
    differences.append(abs(classes[my_class][i] - careers[career][i]))
    difference_total = difference_total + abs(classes[my_class][i] - careers[career][i])

print("differences: " + str(differences))
print("total: " + str(difference_total))

