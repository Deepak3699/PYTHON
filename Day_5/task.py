# ============================================
# Day 5 - TASKS
# ============================================


# ==========================================
# TASK 1 - Easy ⭐
# ==========================================
# User se unka full name lo.
# Phir yeh print karo:
# 1. Name in UPPERCASE
# 2. Name in lowercase
# 3. Name in Title Case
# 4. Name ki total length (spaces ke saath)
# 5. Pehla character
# 6. Aakhri character
#
# Output Example:
# Original  : john smith
# Uppercase : JOHN SMITH
# Lowercase : john smith
# Title     : John Smith
# Length    : 10
# First     : j
# Last      : h

print("TASK 1: Name Formatter")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 2 - Easy ⭐
# ==========================================
# String Slicing Practice:
# word = "Programming"
#
# In sab ko slice karke nikalo:
# 1. Pehle 4 characters
# 2. Aakhri 3 characters
# 3. Characters index 3 se 7 tak
# 4. Har doosra character
# 5. Ulti string (reversed)

print("\nTASK 2: String Slicing")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 3 - Easy ⭐
# ==========================================
# User se ek sentence lo.
# Phir yeh check karke print karo:
# 1. Kitne words hain? (split use karo)
# 2. Kitne characters hain? (spaces ke saath)
# 3. Kya "Python" word hai is mein? (in use karo)
# 4. Sentence kis letter se start hota hai?
# 5. Sentence kis letter par khatam hota hai?

print("\nTASK 3: Sentence Analyzer")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 4 - Medium ⭐⭐
# ==========================================
# Email Validator:
# User se email address lo.
# Check karo:
# 1. Kya "@" hai email mein? (in operator)
# 2. Kya "." hai email mein?
# 3. Username kya hai? (@ se pehle)
# 4. Domain kya hai? (@ ke baad)
# 5. Kya email ".com" par khatam hoti hai?
#
# Output:
# Email    : user@example.com
# Has @    : True
# Has .    : True
# Username : user
# Domain   : example.com
# Is .com? : True

print("\nTASK 4: Email Validator")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 5 - Medium ⭐⭐
# ==========================================
# Text Cleaner:
# Yeh messy string di gayi hai:
# messy = "  hElLo WoRlD   fRoM   pYtHoN  "
#
# Isko clean karo:
# 1. Pehle strip() se extra spaces hatao
# 2. Phir title case mein convert karo
# 3. "World" ko "Universe" se replace karo
# 4. "From" ko "Powered By" se replace karo
# 5. Final cleaned string print karo

print("\nTASK 5: Text Cleaner")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 6 - Hard ⭐⭐⭐
# ==========================================
# CSV Data Processor:
# Yeh data string di gayi hai:
# data = "Emma,28,Designer,London,4500.75"
#
# split() use karke information nikalo aur
# ek formatted profile card print karo:
#
# ╔══════════════════════════════╗
# ║       EMPLOYEE PROFILE       ║
# ╠══════════════════════════════╣
# ║ Name      : Emma             ║
# ║ Age       : 28               ║
# ║ Profession: Designer         ║
# ║ City      : London           ║
# ║ Salary    : $4,500.75        ║
# ╚══════════════════════════════╝

print("\nTASK 6: CSV Data Processor")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 7 - Hard ⭐⭐⭐
# ==========================================
# Username & Password Generator:
# User se yeh lo:
# 1. First name
# 2. Last name
# 3. Birth year
#
# Generate karo:
# Username = first name ka pehla letter +
#            last name (sab small) +
#            birth year ke aakhri 2 digits
# Example: John Smith 1998 -> jsmith98
#
# Password = last name ulta (reverse) +
#            birth year +
#            "!" sign
# Example: Smith 1998 -> htimS1998!
#
# Dono print karo

print("\nTASK 7: Username & Password Generator")
print("-" * 35)
# YAHAN APNA CODE LIKHO:




# ==========================================
# TASK 8 - Challenge ⭐⭐⭐⭐
# ==========================================
# Secret Message Encoder:
# User se ek message lo.
#
# Encoding rules:
# 1. Message ko reverse karo
# 2. Reversed message ko upper case karo
# 3. Spaces ko "_" se replace karo
# 4. Message ke aage "MSG:" lagao
# 5. Message ke peeche ":END" lagao
#
# Example:
# Input : "hello world"
# Step 1: "dlrow olleh"
# Step 2: "DLROW OLLEH"
# Step 3: "DLROW_OLLEH"
# Step 4: "MSG:DLROW_OLLEH"
# Step 5: "MSG:DLROW_OLLEH:END"
#
# Phir Decode bhi karo - ulta process karo!

print("\nTASK 8: Secret Message Encoder")
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
# name = input("Enter your full name: ")
# print(f"Original  : {name}")
# print(f"Uppercase : {name.upper()}")
# print(f"Lowercase : {name.lower()}")
# print(f"Title     : {name.title()}")
# print(f"Length    : {len(name)}")
# print(f"First     : {name[0]}")
# print(f"Last      : {name[-1]}")

# TASK 2 - ANSWER:
# word = "Programming"
# print(f"First 4      : {word[:4]}")
# print(f"Last 3       : {word[-3:]}")
# print(f"Index 3 to 7 : {word[3:8]}")
# print(f"Every 2nd    : {word[::2]}")
# print(f"Reversed     : {word[::-1]}")

# TASK 4 - ANSWER:
# email = input("Enter email: ")
# has_at  = "@" in email
# has_dot = "." in email
# username = email[:email.index("@")]
# domain   = email[email.index("@")+1:]
# is_com   = email.endswith(".com")
# print(f"Email    : {email}")
# print(f"Has @    : {has_at}")
# print(f"Has .    : {has_dot}")
# print(f"Username : {username}")
# print(f"Domain   : {domain}")
# print(f"Is .com? : {is_com}")

# TASK 5 - ANSWER:
# messy = "  hElLo WoRlD   fRoM   pYtHoN  "
# clean = messy.strip()
# clean = clean.title()
# clean = clean.replace("World", "Universe")
# clean = clean.replace("From", "Powered By")
# print(f"Cleaned: {clean}")

# TASK 7 - ANSWER:
# first = input("First name: ").lower()
# last  = input("Last name: ").lower()
# year  = input("Birth year: ")
# username = first[0] + last + year[-2:]
# password = last[::-1].capitalize() + year + "!"
# print(f"Username: {username}")
# print(f"Password: {password}")

# TASK 8 - ANSWER:
# message = input("Enter a message: ")
# step1 = message[::-1]
# step2 = step1.upper()
# step3 = step2.replace(" ", "_")
# encoded = "MSG:" + step3 + ":END"
# print(f"Encoded: {encoded}")
# Decode:
# decode1 = encoded[4:-4]
# decode2 = decode1.replace("_", " ")
# decode3 = decode2.lower()
# decoded = decode3[::-1]
# print(f"Decoded: {decoded}")