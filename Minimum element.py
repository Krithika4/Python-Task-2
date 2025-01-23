#Minimum element

#Creating a list
list1=[4, 5, 6, 7, 0, 1, 2]

#Assume the first element is minimum
minimum=list1[0]

for i in list1:
    if i<minimum:
        minimum=i

#Printing the minimum element
print("The minimum element is", minimum)
