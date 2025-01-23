#Sublist

list2=[4, 2, -3, 1, 6]

#initializing  and empty set to store the sums
sums=set()

sum=0
#flag to check if a sublist with sum 0
found=False

#Checking each iterations
for num in list2:
    sum+=num
    #check if the sum is 0 or if has already been present in sum set
    if  sum==0 or sum in sums:
        found = True
        break

    #Add cumulative sum to set
    sums.add(sum)

    if found:
        print("sublist with sum 0 exixt")
    else:
        print("No sublist with sum 0 exist")


