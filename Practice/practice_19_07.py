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
    print(i)


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
        # 5. If 'i' is a factor/divisor, add it to our running total
        sum = sum + i

# 6. After the loop completes, check if the total sum equals the original number
if sum == n:
    # 7. If they match, it is a perfect number (e.g., 6 or 28)
    print("Your number is perfect number ")
else:
    # 8. If they do not match, it is not a perfect number
    print("Your number is not a perfect number")


