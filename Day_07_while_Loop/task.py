# ============================================
# Day 7 - TASKS
# ============================================


# ==========================================
# TASK 1 - Easy ⭐
# ==========================================
# while loop use karke:
# 1. 1 se 20 tak saare numbers print karo
# 2. 20 se 1 tak ulta count karo (countdown)
# 3. 1 se 50 tak sirf 5 ke multiples print karo
#    (5, 10, 15, 20 ... 50)

print("TASK 1: Basic Counting")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 2 - Easy ⭐
# ==========================================
# Multiplication Table:
# User se koi number lo (e.g., 6).
# Uski multiplication table print karo (1 se 12 tak).
#
# Output:
# 6 x 1  = 6
# 6 x 2  = 12
# ...
# 6 x 12 = 72

print("\nTASK 2: Multiplication Table")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 3 - Easy ⭐
# ==========================================
# Sum Calculator:
# User se numbers enter karane do.
# Jab user "done" likhe toh band karo.
# Sab numbers ka total print karo.
#
# Output:
# Enter number (or 'done' to stop): 10
# Enter number (or 'done' to stop): 25
# Enter number (or 'done' to stop): 15
# Enter number (or 'done' to stop): done
# Total sum: 50
# Numbers entered: 3

print("\nTASK 3: Sum Calculator")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 4 - Medium ⭐⭐
# ==========================================
# ATM PIN System:
# Correct PIN = "4321"
# User ko 3 chances do.
# Agar sahi PIN -> "Welcome! Balance: $2500"
# Agar 3 baar galat -> "Card Blocked!"
# Har galat attempt mein remaining chances batao.

print("\nTASK 4: ATM PIN System")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 5 - Medium ⭐⭐
# ==========================================
# continue use karko:
# 1 se 30 tak numbers print karo
# lekin jo numbers 3 ya 7 se divisible hain
# unhe skip karo (continue use karo)
# Skipped numbers alag print karo.
#
# Output:
# Printed: 1 2 4 5 8 ...
# Skipped: 3 6 7 9 ...

print("\nTASK 5: Skip Divisible Numbers")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 6 - Hard ⭐⭐⭐
# ==========================================
# Shopping Cart System:
# while loop se user ko items add karne do.
# Har baar poochho: item name aur price.
# Jab "done" likhe toh:
# - Sab items aur prices print karo
# - Subtotal calculate karo
# - 10% tax add karo
# - Final total print karo
#
# Output:
# ================================
# Item          Price
# --------------------------------
# Apple       : $2.50
# Bread       : $3.99
# Milk        : $1.50
# --------------------------------
# Subtotal    : $7.99
# Tax (10%)   : $0.80
# TOTAL       : $8.79
# ================================

print("\nTASK 6: Shopping Cart")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 7 - Hard ⭐⭐⭐
# ==========================================
# Pattern Printer:
# User se rows ka number lo.
# Yeh patterns print karo nested while use karke:
#
# Pattern 1 (Number Triangle):
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#
# Pattern 2 (Right-aligned Stars):
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

print("\nTASK 7: Pattern Printing")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 8 - Challenge ⭐⭐⭐⭐
# ==========================================
# Complete Quiz Game:
# 3 questions ki quiz banao.
# Har question ke liye:
# - Question print karo
# - User se answer lo
# - 3 chances do (while loop)
# - Sahi hone par next question
# - Galat hone par hint do
# - 3 chances khatam hone par answer batao
#
# End mein:
# - Total score print karo (har sahi = 10 points)
# - Grade do (30=A, 20=B, 10=C, 0=D)
#
# Questions:
# Q1: What is 15 * 4?          Answer: 60
# Q2: Python was created in?   Answer: 1991
# Q3: What does CPU stand for? Answer: central processing unit

print("\nTASK 8: Quiz Game")
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
# # Part 1
# i = 1
# while i <= 20:
#     print(i, end=" ")
#     i += 1
# print()
# # Part 2
# i = 20
# while i >= 1:
#     print(i, end=" ")
#     i -= 1
# print()
# # Part 3
# i = 5
# while i <= 50:
#     print(i, end=" ")
#     i += 5
# print()

# TASK 2 - ANSWER:
# num = int(input("Enter a number: "))
# i   = 1
# while i <= 12:
#     print(f"{num} x {i:2} = {num * i}")
#     i += 1

# TASK 3 - ANSWER:
# total   = 0
# count   = 0
# while True:
#     entry = input("Enter number (or 'done'): ")
#     if entry.lower() == "done":
#         break
#     try:
#         total += float(entry)
#         count += 1
#     except ValueError:
#         print("Invalid! Enter a number.")
# print(f"Total sum    : {total}")
# print(f"Numbers entered: {count}")

# TASK 4 - ANSWER:
# correct_pin = "4321"
# attempts    = 0
# max_att     = 3
# while attempts < max_att:
#     pin = input(f"Enter PIN (Attempt {attempts+1}/{max_att}): ")
#     attempts += 1
#     if pin == correct_pin:
#         print("Welcome! Balance: $2500")
#         break
#     else:
#         remaining = max_att - attempts
#         if remaining > 0:
#             print(f"Wrong PIN! {remaining} chances left.")
# else:
#     print("Card Blocked!")

# TASK 6 - ANSWER:
# items  = []
# prices = []
# while True:
#     item = input("Item name (or 'done'): ")
#     if item.lower() == "done":
#         break
#     price = float(input(f"Price of {item}: $"))
#     items.append(item)
#     prices.append(price)
# subtotal = sum(prices)
# tax      = subtotal * 0.10
# total    = subtotal + tax
# print("=" * 32)
# print(f"{'Item':<15} {'Price':>10}")
# print("-" * 32)
# i = 0
# while i < len(items):
#     print(f"{items[i]:<15} ${prices[i]:>8.2f}")
#     i += 1
# print("-" * 32)
# print(f"{'Subtotal':<15} ${subtotal:>8.2f}")
# print(f"{'Tax (10%)':<15} ${tax:>8.2f}")
# print(f"{'TOTAL':<15} ${total:>8.2f}")
# print("=" * 32)

# TASK 7 - ANSWER:
# rows = int(input("Enter rows: "))
# # Pattern 1
# i = 1
# while i <= rows:
#     j = 1
#     while j <= i:
#         print(j, end=" ")
#         j += 1
#     print()
#     i += 1
# # Pattern 2
# i = 1
# while i <= rows:
#     spaces = rows - i
#     j = 0
#     while j < spaces:
#         print("  ", end="")
#         j += 1
#     k = 0
#     while k < i:
#         print("*", end=" ")
#         k += 1
#     print()
#     i += 1