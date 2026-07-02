# ============================================
# Day 4 - TASKS
# ============================================


# ==========================================
# TASK 1 - Easy ⭐
# ==========================================
# User se 2 numbers lo.
# Phir yeh sab calculate karke print karo:
# Addition, Subtraction, Multiplication,
# Division, Floor Division, Modulus, Exponent
#
# Output format:
# 10 + 3 = 13
# 10 - 3 = 7
# ... aur baaki bhi

print("TASK 1: Full Arithmetic Calculator")
print("-" * 40)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 2 - Easy ⭐
# ==========================================
# Even ya Odd Checker:
# User se koi number lo.
# Modulus (%) use karke check karo k yeh
# even hai ya odd.
# Output: "25 is ODD" ya "24 is EVEN"

print("\nTASK 2: Even or Odd Checker")
print("-" * 40)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 3 - Easy ⭐
# ==========================================
# Assignment Operators Practice:
# wallet = 500 se shuru karo.
# 1. 200 add karo (+=)
# 2. 100 minus karo (-=)
# 3. 2 se multiply karo (*=)
# 4. 4 se divide karo (//=)
# Har step ke baad wallet print karo.

print("\nTASK 3: Wallet Balance Tracker")
print("-" * 40)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 4 - Medium ⭐⭐
# ==========================================
# Comparison Operators:
# User se apni age lo.
# Phir check karo aur print karo:
# 1. Kya age 18 se zyada hai? (Adult?)
# 2. Kya age 65 se zyada hai? (Senior?)
# 3. Kya age exactly 18 hai? (Just turned adult?)
# 4. Kya age 13 aur 19 ke beech hai? (Teenager?)
# (Hint: and operator use karo for last one)

print("\nTASK 4: Age Category Checker")
print("-" * 40)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 5 - Medium ⭐⭐
# ==========================================
# Logical Operators - Movie Ticket System:
# Variables banao:
#   has_ticket = True
#   is_vip = False
#   age = 16
#
# Check karo:
# 1. Can enter? (has_ticket AND age >= 13)
# 2. Can get VIP lounge? (has_ticket AND is_vip)
# 3. Needs adult supervision? (has_ticket AND age < 18)
# 4. Cannot enter? (NOT has_ticket)
# Har cheez ka result print karo.

print("\nTASK 5: Movie Ticket System")
print("-" * 40)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 6 - Hard ⭐⭐⭐
# ==========================================
# BMI Calculator:
# User se weight (kg) aur height (meters) lo.
# BMI Formula: weight / (height ** 2)
#
# Phir yeh print karo:
# - BMI value
# - Kya BMI 18.5 se kam hai? (Underweight)
# - Kya BMI 18.5 aur 24.9 ke beech hai? (Normal)
# - Kya BMI 25 se zyada hai? (Overweight)
# (Hint: and/or operators use karo)

print("\nTASK 6: BMI Calculator")
print("-" * 40)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 7 - Hard ⭐⭐⭐
# ==========================================
# Time Converter:
# User se total minutes lo (e.g., 150).
# Usse hours aur minutes mein convert karo.
# Floor division (//) aur modulus (%) use karo.
# Output: "150 minutes = 2 hours and 30 minutes"
#
# Bonus: Phir seconds mein convert karo bhi.
# Total seconds = total_minutes * 60

print("\nTASK 7: Time Converter")
print("-" * 40)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 8 - Challenge ⭐⭐⭐⭐
# ==========================================
# Shopping Cart Calculator:
# User se yeh lo:
# 1. Price of item 1 (float)
# 2. Price of item 2 (float)
# 3. Price of item 3 (float)
# 4. Discount percentage (e.g., 10 for 10%)
# 5. Tax percentage (e.g., 8 for 8%)
#
# Calculate karo:
# - Subtotal (sum of all items)
# - Discount amount
# - Price after discount
# - Tax amount (on discounted price)
# - Final total
# - Round off to 2 decimal places
#
# Output:
# ================================
# Item 1      : $XX.XX
# Item 2      : $XX.XX
# Item 3      : $XX.XX
# Subtotal    : $XX.XX
# Discount    : -$XX.XX
# After Disc  : $XX.XX
# Tax         : +$XX.XX
# TOTAL       : $XX.XX
# ================================

print("\nTASK 8: Shopping Cart Calculator")
print("-" * 40)
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
# n1 = float(input("Enter first number: "))
# n2 = float(input("Enter second number: "))
# print(f"{n1} + {n2}  = {n1 + n2}")
# print(f"{n1} - {n2}  = {n1 - n2}")
# print(f"{n1} * {n2}  = {n1 * n2}")
# print(f"{n1} / {n2}  = {n1 / n2}")
# print(f"{n1} // {n2} = {n1 // n2}")
# print(f"{n1} % {n2}  = {n1 % n2}")
# print(f"{n1} ** {n2} = {n1 ** n2}")

# TASK 2 - ANSWER:
# num = int(input("Enter a number: "))
# is_even = num % 2 == 0
# if is_even:
#     print(f"{num} is EVEN")
# else:
#     print(f"{num} is ODD")

# TASK 3 - ANSWER:
# wallet = 500
# print("Start:", wallet)
# wallet += 200
# print("After +200:", wallet)
# wallet -= 100
# print("After -100:", wallet)
# wallet *= 2
# print("After *2:", wallet)
# wallet //= 4
# print("After //4:", wallet)

# TASK 6 - ANSWER:
# weight = float(input("Enter weight in kg: "))
# height = float(input("Enter height in meters: "))
# bmi = weight / (height ** 2)
# print(f"Your BMI: {bmi:.2f}")
# print(f"Underweight (BMI < 18.5)  : {bmi < 18.5}")
# print(f"Normal (18.5 <= BMI < 25) : {bmi >= 18.5 and bmi < 25}")
# print(f"Overweight (BMI >= 25)    : {bmi >= 25}")

# TASK 7 - ANSWER:
# total_minutes = int(input("Enter total minutes: "))
# hours = total_minutes // 60
# minutes = total_minutes % 60
# print(f"{total_minutes} minutes = {hours} hours and {minutes} minutes")
# total_seconds = total_minutes * 60
# print(f"In seconds: {total_seconds} seconds")

# TASK 8 - ANSWER:
# p1 = float(input("Item 1 price: $"))
# p2 = float(input("Item 2 price: $"))
# p3 = float(input("Item 3 price: $"))
# disc = float(input("Discount %: "))
# tax  = float(input("Tax %: "))
# subtotal      = p1 + p2 + p3
# disc_amount   = (subtotal * disc) / 100
# after_disc    = subtotal - disc_amount
# tax_amount    = (after_disc * tax) / 100
# final_total   = after_disc + tax_amount
# print("=" * 32)
# print(f"Item 1      : ${p1:.2f}")
# print(f"Item 2      : ${p2:.2f}")
# print(f"Item 3      : ${p3:.2f}")
# print(f"Subtotal    : ${subtotal:.2f}")
# print(f"Discount    : -${disc_amount:.2f}")
# print(f"After Disc  : ${after_disc:.2f}")
# print(f"Tax         : +${tax_amount:.2f}")
# print(f"TOTAL       : ${final_total:.2f}")
# print("=" * 32)