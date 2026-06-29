# ============================================
# Day 2 - TASKS
# ============================================
# Har task solve karo aur output check karo
# ============================================


# ==========================================
# TASK 1 - Easy ⭐
# ==========================================
# Apni personal info ke variables banao aur print karo:
# - name (string)
# - age (integer)
# - height in feet (float)
# - is_employed (boolean)
# - nickname (None rakho agar nahi hai)
#
# Expected Output:
# Name: [Tumhara naam]
# Age: [Tumhari umar]
# Height: [Tumhari height]
# Employed: [True/False]
# Nickname: None

print("TASK 1:")
print("-" * 30)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 2 - Easy ⭐
# ==========================================
# Neeche diye values ka type batao - type() use karo:
# 1. 42
# 2. 3.14
# 3. "Python"
# 4. True
# 5. None
# 6. "100"  (Yeh number hai ya string?)
# 7. 0b1111 (Binary)
#
# Expected Output:
# 42 ka type: <class 'int'>
# ... aur baaki bhi

print("\nTASK 2:")
print("-" * 30)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 3 - Easy ⭐
# ==========================================
# Multiple assignment use karo:
# - Ek line mein 3 variables banao: city, country, continent
#   city = "Punjab", country = "India", continent = "Asia"
# - Phir sab ko ek saath print karo
# - Phir city aur country ki values swap karo (exchange karo)
# - Phir dobara print karo

print("\nTASK 3:")
print("-" * 30)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 4 - Medium ⭐⭐
# ==========================================
# isinstance() use karke check karo:
# Variables:
#   x = 500
#   y = "Hello World"
#   z = 9.99
#   w = False
#
# Har variable ke liye check karo:
# - Kya yeh int hai?
# - Kya yeh str hai?
# - Kya yeh float hai?
# - Kya yeh bool hai?
# Aur result print karo

print("\nTASK 4:")
print("-" * 30)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 5 - Medium ⭐⭐
# ==========================================
# Apni favourite game ya movie ka data store karo:
# Variables banana hai:
# - title (str)
# - release_year (int)
# - rating (float - 0.0 to 10.0)
# - is_available (bool)
# - sequel_name (None agar sequel nahi)
#
# Phir ek achi formatted card print karo jaise:
# ================================
# Title    : [title]
# Year     : [year]
# Rating   : [rating]/10
# Available: [True/False]
# Sequel   : [None/Name]
# ================================

print("\nTASK 5:")
print("-" * 30)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 6 - Medium ⭐⭐
# ==========================================
# Variable ki value update karo:
# 
# 1. score = 0 se shuru karo - print karo
# 2. score mein 25 add karo (score = score + 25) - print karo
# 3. score mein 50 add karo - print karo  
# 4. score 10 se minus karo - print karo
# 5. Final score print karo
#
# Phir check karo:
# - Score 60 se zyada hai? (isinstance use karo)
# - Score ka type kya hai?

print("\nTASK 6:")
print("-" * 30)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 7 - Hard ⭐⭐⭐
# ==========================================
# Shop ka record banao:
#
# Variables:
# shop_name = "Ali Electronics"
# owner = "Muhammad Ali"
# city = "Karachi"
# established_year = 2010
# total_products = 500
# monthly_revenue = 150000.75
# is_online = True
# branch_city = None  (abhi tak nahi)
#
# Yeh cheezein print karo:
# 1. Poora shop card (formatted)
# 2. Har variable ka type
# 3. Shop kitne saal purana hai (2024 - established_year)
# 4. is_online True hai ya nahi - isinstance se check karo

print("\nTASK 7:")
print("-" * 30)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 8 - Hard ⭐⭐⭐
# ==========================================
# String unpack karo:
#
# 1. "PKR" string ko teen alag variables mein store karo
#    (currency1, currency2, currency3)
# 2. Phir print karo each character
# 3. Phir check karo har character ka type kya hai
#
# Bonus: "ABCDE" ko 5 variables mein store karo ek line mein

print("\nTASK 8:")
print("-" * 30)
# YAHAN APNA CODE LIKHO:





# ============================================
#                  ANSWERS
# ============================================
# Pehle khud try karo phir dekho!
#
#
#
#
# ============================================

# TASK 1 - ANSWER:
# name = "Deepak"
# age = 20
# height = 5.8
# is_employed = False
# nickname = None
# print("Name:", name)
# print("Age:", age)
# print("Height:", height)
# print("Employed:", is_employed)
# print("Nickname:", nickname)

# TASK 2 - ANSWER:
# print("42 ka type:", type(42))
# print("3.14 ka type:", type(3.14))
# print("'Python' ka type:", type("Python"))
# print("True ka type:", type(True))
# print("None ka type:", type(None))
# print("'100' ka type:", type("100"))     # str hai! number nahi
# print("0b1111 ka type:", type(0b1111))   # int hai (15)

# TASK 3 - ANSWER:
# city, country, continent = "Punjab", "India ", "Asia"
# print(city, country, continent)
# city, country = country, city   # Swap!
# print(city, country, continent)

# TASK 6 - ANSWER:
# score = 0
# print("Start:", score)
# score = score + 25
# print("After +25:", score)
# score = score + 50
# print("After +50:", score)
# score = score - 10
# print("After -10:", score)
# print("Final Score:", score)
# print("60 se zyada?", score > 60)
# print("Type:", type(score))

# TASK 8 - ANSWER:
# currency1, currency2, currency3 = "INR"
# print(currency1)  # I
# print(currency2)  # N
# print(currency3)  # R
# print(type(currency1))  # str
# a, b, c, d, e = "ABCDE"
# print(a, b, c, d, e)