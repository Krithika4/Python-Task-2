#Happy Numbers

numbers=[10, 501, 22, 37, 100, 999, 87, 351]

#creating list to store Happy numbers
Happy_numbers=[]

for num in numbers:
    visited=set() #Creating a set to keep track of visited numbers to avoid infinite loop
    original_num =num
    while num!=1 and num not in visited: #checks the condition
        visited.add(num) #adds to the set
        num=sum(int(digit)**2 for digit in str(num))
    if(num==1):
        Happy_numbers.append(original_num)
print(f"Happy Numbers:  {Happy_numbers}")
print(f"Count of Happy numbers: {len(Happy_numbers)}")
            
            

