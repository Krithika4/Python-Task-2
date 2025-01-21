#Finding Duplicates in the list

#Creating 3 lists
list1 =["java","python","selenium"]
list2 =["javascript","python","C","Handhoop","selenium"]
list3 =["SQL","cucumber","selenium","python"]

#Finding duplicates across the three lists
Duplicate_list=set(list1) & set(list2) & set(list3)

print("Duplicates across the three list are :", Duplicate_list)

