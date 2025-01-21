#Sum of first and last digit

user_input=int(input("Enter an integer : "))

#Convert a num to string to easy access of digits
num = str(abs(user_input)) #use abs to handle negative numbers

#creating a logic to add the first and last digit
first_digit=int(num[0])
last_digit=int(num[-1])

#Calculating the sum
Sum_of_digits = first_digit + last_digit

print(f"The sum of first and last digit of {num} is {Sum_of_digits} ")