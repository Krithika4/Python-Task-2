#Even and odd numbers in the list

Total_list=[10, 501, 22, 37, 100, 99, 87, 351]

#creating even list to store even numbers
even=[]

#creating odd list to store odd numbers
odd=[]

for x in Total_list:
    if x % 2==0:
        even.append(x) # Add to even list if the numbers are even
    else:
        odd.append(x) #Add to odd list if numbers are odd

print("Even numbers:", even)
print("Odd numbers:" ,odd)
