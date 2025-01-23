#Prime numbers

#Given List
numbers=[10. 501. 22, 37, 100, 999, 87, 351]

#Empty list to store prime numbers
prime_numbers=[]

for i in numbers:
    if i>1:
        is_prime=True
        for j in range(2, int(i ** 0.5)+1):
            if i %j==0:
                is_prime= False
                break
        if is_prime:
            prime_numbers.append(i)

print("The prime numbers in the list:", prime_numbers)