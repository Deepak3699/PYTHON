# break ------- loop break at the fix condition ---
# continue -- skip that number and continue ------- l
# else      - if age = 15 print hoga warna else ---


for i in range (1,21):
    if i == 15:
        continue
    else:
        print(i)

for i in range (1,21):
    if i == 15:
        break
    print(i)
else:
    print("Break not executed")
    
    
#--------------- Practice -----------------

# accept an interger and print hello word n times 

n = int(input("Enter the number for how much time you want to print :- "))
for i in range(1,n+1):
    print("Hello World")


# Print natural numbers up to n 
n = int(input("Enter the number  to print natural number  :- "))
for i in range(1,n+1):
    print(i)

# Reverse for loop 
for i in range(9,1,-1):
    print(i) 
    
# Take input and print its table 
num = int(input("Enter the number to print Table :-"))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
    
# Sum upto n terms 

n = int(input(" enter the n term :-"))
sum = 0
for i in range(1,n+1):
    sum = sum+i
print(sum)

# Factorial of a number

num = int(input("Enter the number u want to see the factorial :-"))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print(fact)


# using module 

import math
num = int(input("Enter the number u want to see the factorial: "))
# Calculate without loops using the built-in function
facts = math.factorial(num)
print(facts)



# Print the sum of even and odd number 

num = int(input("Enter the number till you want sum of even and odd: "))

# 1. Initialize separate counters for even and odd sums
even_sum = 0
odd_sum = 0

# 2. Loop through the range
for i in range(1, num + 1):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

# 3. Print the final results outside the loop
print(f"Sum of even numbers is: {even_sum}")
print(f"Sum of odd numbers is: {odd_sum}")




# Enter number for find the factor of number

n = int(input("Enter the number :-"))
for i in range(1,n+1):
    if n%i==0:  
        print(i) 
# isme kaya hua for loop chalegi like user enter 4 
# for loop start from 1 enter in if abb yeah check karegi 4%1 == 0 print i 
# i =2 , i=3 not =0 not print 




# Accept a number and check it is perfect number or not 
# 1. Take a number input from the user and convert it into an integer
n = int(input("Enter the number to check a number is perfect or not :-"))

# 2. Initialize a variable to keep track of the sum of proper divisors
sum = 0

# 3. Loop from 1 up to (n-1). Perfect numbers exclude the number itself
for i in range(1, n):
    
    # 4. Check if 'n' is perfectly divisible by 'i' (remainder is 0)
    if n % i == 0:  
        '''
        Suppose user enters 6:
        i = 1 -> 6 % 1 == 0 (True)  -> sum = 0 + 1 = 1
        i = 2 -> 6 % 2 == 0 (True)  -> sum = 1 + 2 = 3
        i = 3 -> 6 % 3 == 0 (True)  -> sum = 3 + 3 = 6
        i = 4 -> 6 % 4 != 0 (False) -> sum stays 6
        i = 5 -> 6 % 5 != 0 (False) -> sum stays 6
        '''
        
        # 5. If 'i' is a factor/divisor, add it to our running total
        sum = sum + i

# 6. After the loop completes, check if the total sum equals the original number
if sum == n:
    # 7. If they match, it is a perfect number (e.g., 6 or 28)
    print("Your number is perfect number ")
else:
    # 8. If they do not match, it is not a perfect number
    print("Your number is not a perfect number")
    
    
# Check whether the number is prime or not 
# what is prime number which is only divide by its own and 1 only 2 factors 

n = int(input("Enter the number to check prime or not :-"))
count = 0
for i in range(1,n+1):
    if n%i == 0:
        count = count+1
if count == 2:
    print("Number is PRIME ")
else:
    print("Number is Not PRIME ")



# Reverse A string 
a = "Deepak"
print(a[::-1])
print(len(a))
 
# 1. Define a string variable named 'b' with a length of 7 characters.
b = "Khuttan"

# 2. Start a loop using range(start, stop, step).
#    - Start: len(b) - 1  -> 7 - 1 = 6 (the index of the last letter 'n')
#    - Stop:  -1          -> The loop stops BEFORE -1, meaning it includes 0 (the first letter 'K')
#    - Step:  -1          -> Count downward by 1 each time
for i in range(len(b)-1 , -1, -1):
    
    # 3. Print the character at the current index position 'i'.
    #    - 1st loop: i = 6 -> prints b[6], which is 'n'
    #    - 2nd loop: i = 5 -> prints b[5], which is 'a'
    #    - 3rd loop: i = 4 -> prints b[4], which is 't'
    #    - 4th loop: i = 3 -> prints b[3], which is 't'
    #    - 5th loop: i = 2 -> prints b[2], which is 'u'
    #    - 6th loop: i = 1 -> prints b[1], which is 'h'
    #    - 7th loop: i = 0 -> prints b[0], which is 'K'
    print(b[i])
    
    
    
#----------------- palindrome or not -------------------

b = "Khuttan"
c =""
for i in range(len(b) - 1, -1, -1):
    c = c+ b[i]
if c == b:
    print(f"Word {b} is palindrome ")
else:
    print(f"Not a palindrome")


#--------------------  Find all special characters from a given string------------------

str1 = "P@#yn26at^&i5ve"
char = 0
dig = 0
spchar = 0
for i in a:
    if i.isdigit():
        dig +=1
    elif i.isalpha():
        char +=1
    else:
        spchar +=1
print(f" Your Digits are {dig} \n Your Alphabet are {char} \n Your Special Characters are {spchar}")

print(dir(str))