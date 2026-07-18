# Write a program that checks if a number is even or odd.

# Example:
# Input: 7
# Output: "Odd"

# while True:
#     try:
#         num = int(input("Enter the Number to check ``even`` or ``Odd`` :- "))
#         if num == 0:
#             print(" Number is  Zero ")
#             break
#         elif num < 0 and num % 2 == -0 :
#             print(f"Number is Negative even {num}")
#         elif num < 0 and num %2 != 0 :
#             print(f"Number is Negative Odd {num}")
#         elif num % 2 == 0:
#             print(f"The Number {num} is Even ")
#             break
#         else:
#             print(f"The Number {num} is Odd ")
#             break
#     except ValueError:
#         print( " Enter correct Numbers ")
        



# Print the multiplication table of a given number (1-10)

# Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# ... and so on



num = int(input(" Enter the number you want a Table for :- "))
for i in range (1,11):
  print(f"{num} X {i} = {num*i}")
  
#----------------------------------------------


# 1. Take input from the user and convert it to integers
num1 = int(input("Enter the number from you want to start the Table :- "))
num2 = int(input("Enter the number where you want to end the Table :- "))

# 2. Outer loop handles the multiplier (1 to 10)
for i in range(1, 11):
    # 3. Inner loop iterates through your chosen range of numbers (inclusive)
    for j in range(num1, num2 + 1):
        # The \t adds a tab space so the tables print side-by-side cleanly
        print(f"{j} X {i} = {j*i}", end="\t")
    
    # Prints a new line after each row is complete
    print()
    
#------------------------------------------------------------------


