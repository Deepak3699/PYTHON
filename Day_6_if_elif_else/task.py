# ============================================
# Day 6 - TASKS
# ============================================


# ==========================================
# TASK 1 - Easy ⭐
# ==========================================
# User se number lo.
# Check karo:
# 1. Positive hai ya Negative ya Zero
# 2. Even hai ya Odd
# 3. 100 se bada hai ya chhota ya equal
#
# Output Example (number = 42):
# 42 is Positive
# 42 is Even
# 42 is Less than 100

print("TASK 1: Number Analyzer")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 2 - Easy ⭐
# ==========================================
# Simple Traffic Light System:
# User se light color lo (red/yellow/green).
# Phir batao kya karna chahiye:
# red    -> "STOP! Do not cross."
# yellow -> "SLOW DOWN! Get ready."
# green  -> "GO! You may cross."
# Koi aur color -> "Invalid traffic light color!"

print("\nTASK 2: Traffic Light System")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 3 - Easy ⭐
# ==========================================
# User se 3 numbers lo.
# Sabse bada number dhundo aur print karo.
# (if-elif-else use karo)
#
# Output Example:
# Numbers: 45, 12, 78
# Largest number is: 78

print("\nTASK 3: Find Largest Number")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 4 - Medium ⭐⭐
# ==========================================
# Rock Paper Scissors Game:
# User se choice lo (rock/paper/scissors).
# Computer ki choice "paper" hai (hardcoded).
# Decide karo kaun jeeta:
# - rock vs paper      -> Computer wins
# - paper vs paper     -> Draw
# - scissors vs paper  -> User wins
#
# Output:
# Your choice   : rock
# Computer      : paper
# Result        : Computer Wins!

print("\nTASK 4: Rock Paper Scissors")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 5 - Medium ⭐⭐
# ==========================================
# Restaurant Ordering System:
# Menu:
# 1. Burger    - $8.99
# 2. Pizza     - $12.99
# 3. Pasta     - $9.99
# 4. Salad     - $6.99
#
# User se item number lo.
# Phir quantity poocho.
# Total calculate karo.
# Agar total > $30 toh 10% discount.
# Final bill print karo.

print("\nTASK 5: Restaurant Ordering")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 6 - Hard ⭐⭐⭐
# ==========================================
# Student Result System:
# User se yeh lo:
# - Student name
# - Marks in 3 subjects (out of 100 each)
#
# Calculate:
# - Total marks (out of 300)
# - Percentage
# - Grade:
#   90%+ = A+ (Outstanding)
#   80%+ = A  (Excellent)
#   70%+ = B  (Very Good)
#   60%+ = C  (Good)
#   50%+ = D  (Pass)
#   Below 50% = F (Fail)
#
# Agar kisi bhi subject mein 33 se kam marks
# hain toh student fail hai (even if percentage > 50%)
#
# Print karo ek result card.

print("\nTASK 6: Student Result System")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 7 - Hard ⭐⭐⭐
# ==========================================
# Number Guessing Hint System:
# Secret number = 42 (hardcoded)
# User se guess lo.
# Hint do:
# - "Too High!" agar guess > 42
# - "Too Low!"  agar guess < 42
# - "Too High but Very Close!" agar guess > 42 aur diff <= 5
# - "Too Low but Very Close!"  agar guess < 42 aur diff <= 5
# - "Correct! You got it!" agar exactly 42
#
# Difference: abs(guess - secret)
# abs() function negative number ko positive karta hai

print("\nTASK 7: Number Guessing Hints")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 8 - Challenge ⭐⭐⭐⭐
# ==========================================
# Complete Shopping System:
# User se yeh lo:
# 1. Customer type: (1)Regular (2)Member (3)VIP
# 2. Total purchase amount
# 3. Payment method: (1)Cash (2)Card (3)Online
#
# Discount Rules:
# Regular  -> 0%  discount
# Member   -> 10% discount
# VIP      -> 20% discount
#
# Payment Bonus:
# Cash     -> Extra 2% off
# Card     -> No extra
# Online   -> Extra 5% off
#
# Tax: 8% on final amount
#
# Print complete bill:
# ============================
# Customer Type : VIP
# Payment       : Online
# Original Price: $XXX.XX
# Discount (20%): -$XXX.XX
# Online Bonus(5%): -$XX.XX
# After Discount: $XXX.XX
# Tax (8%)      : +$XX.XX
# FINAL TOTAL   : $XXX.XX
# ============================

print("\nTASK 8: Complete Shopping System")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ============================================
#                  ANSWERS
# ============================================
# Pehle khud try karo phir dekho!
#
#
#
# ============================================

# TASK 1 - ANSWER:
# num = int(input("Enter a number: "))
# if num > 0:
#     print(f"{num} is Positive")
# elif num < 0:
#     print(f"{num} is Negative")
# else:
#     print(f"{num} is Zero")
# if num % 2 == 0:
#     print(f"{num} is Even")
# else:
#     print(f"{num} is Odd")
# if num > 100:
#     print(f"{num} is Greater than 100")
# elif num < 100:
#     print(f"{num} is Less than 100")
# else:
#     print(f"{num} is Equal to 100")

# TASK 2 - ANSWER:
# light = input("Enter light color: ").lower()
# if light == "red":
#     print("STOP! Do not cross.")
# elif light == "yellow":
#     print("SLOW DOWN! Get ready.")
# elif light == "green":
#     print("GO! You may cross.")
# else:
#     print("Invalid traffic light color!")

# TASK 3 - ANSWER:
# n1 = float(input("First number : "))
# n2 = float(input("Second number: "))
# n3 = float(input("Third number : "))
# if n1 >= n2 and n1 >= n3:
#     print(f"Largest: {n1}")
# elif n2 >= n1 and n2 >= n3:
#     print(f"Largest: {n2}")
# else:
#     print(f"Largest: {n3}")

# TASK 6 - ANSWER:
# name = input("Student name: ")
# m1 = int(input("Subject 1 marks: "))
# m2 = int(input("Subject 2 marks: "))
# m3 = int(input("Subject 3 marks: "))
# total = m1 + m2 + m3
# percentage = (total / 300) * 100
# failed_subject = m1 < 33 or m2 < 33 or m3 < 33
# if failed_subject:
#     grade = "F"
#     remark = "Fail (Failed in a subject)"
# elif percentage >= 90:
#     grade, remark = "A+", "Outstanding"
# elif percentage >= 80:
#     grade, remark = "A",  "Excellent"
# elif percentage >= 70:
#     grade, remark = "B",  "Very Good"
# elif percentage >= 60:
#     grade, remark = "C",  "Good"
# elif percentage >= 50:
#     grade, remark = "D",  "Pass"
# else:
#     grade, remark = "F",  "Fail"
# print("=" * 35)
# print(f"  RESULT CARD - {name}")
# print("=" * 35)
# print(f"Subject 1 : {m1}/100")
# print(f"Subject 2 : {m2}/100")
# print(f"Subject 3 : {m3}/100")
# print(f"Total     : {total}/300")
# print(f"Percentage: {percentage:.2f}%")
# print(f"Grade     : {grade}")
# print(f"Remark    : {remark}")
# print("=" * 35)

# TASK 7 - ANSWER:
# secret = 42
# guess  = int(input("Enter your guess: "))
# diff   = abs(guess - secret)
# if guess == secret:
#     print("Correct! You got it!")
# elif guess > secret and diff <= 5:
#     print("Too High but Very Close!")
# elif guess < secret and diff <= 5:
#     print("Too Low but Very Close!")
# elif guess > secret:
#     print("Too High!")
# else:
#     print("Too Low!")