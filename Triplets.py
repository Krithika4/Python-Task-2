#Triplets

#input list and target value
num=[10, 20, 30, 9]
target_value=59

#A flag to check if the triplet is found
found = False

#checking all possible conditions of three numbers
for i in range (len(num)):
    for j in range(i+1, len(num)):
        for k in range (j+1, len(num)):
            if num[i] + num[j] + num[k]==target_value:
                print("The triplet is:", num[i], num[j], num[k])
                found = True
                break
        if found:
            break
    if found:
        break
if not found:
    print("No triplets are found with the given sum")



