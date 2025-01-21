#Non-repeating element

#Creating input list
list1=[4,5,1,2,0,4,1,2]

#finding the first non-repeating element
for num in list1:
    if list1.count(num)==1:
        print(f"The first non-repeating element: {num}")
        break
else:
    print("Non non-repeating element found in the list")












              
