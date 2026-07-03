# ============================================
# Day 5 - Strings and String Methods
# ============================================


# ==========================================
# SECTION 1: String Banane Ke Tarike
# ==========================================
print("=" * 45)
print("   SECTION 1: Creating Strings")
print("=" * 45)

# Single quotes
name1 = 'John Doe'

# Double quotes
name2 = "Sarah Connor"

# Triple quotes - multiple lines
bio = """My name is David.
I am a Python developer.
I love coding!"""

# Triple single quotes
address = '''123 Main Street
New York, USA'''

print("Single quotes   :", name1)
print("Double quotes   :", name2)
print("Triple quotes   :")
print(bio)
print("Triple single   :")
print(address)

# String type check
print("\nType:", type(name1))         # <class 'str'>
print("Length:", len(name1))          # 8


# ==========================================
# SECTION 2: String Indexing
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 2: String Indexing")
print("=" * 45)

word = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5   (Positive)
#      -6 -5 -4 -3 -2 -1   (Negative)

print(f"String: {word}")
print(f"Length: {len(word)}")
print("-" * 45)

# Positive indexing
print(f"word[0]  = '{word[0]}'   (Pehla character)")
print(f"word[1]  = '{word[1]}'   (Doosra character)")
print(f"word[3]  = '{word[3]}'   (Chautha character)")
print(f"word[5]  = '{word[5]}'   (Chatha / aakhri)")

# Negative indexing
print(f"\nword[-1] = '{word[-1]}'   (Aakhri character)")
print(f"word[-2] = '{word[-2]}'   (Doosra aakhri)")
print(f"word[-6] = '{word[-6]}'   (Pehla, ulti taraf se)")

# Real example
full_name = "James Anderson"
print(f"\nfull_name = '{full_name}'")
print(f"Pehla letter : {full_name[0]}")
print(f"Aakhri letter: {full_name[-1]}")
print(f"Space kahan  : index {full_name.index(' ')}")


# ==========================================
# SECTION 3: String Slicing
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 3: String Slicing")
print("=" * 45)

text = "Hello World Python"
#       0123456789...

print(f"Original String: '{text}'")
print(f"Length         : {len(text)}")
print("-" * 45)

# Basic slicing [start:stop]
print(f"text[0:5]    = '{text[0:5]}'")     # Hello
print(f"text[6:11]   = '{text[6:11]}'")    # World
print(f"text[12:18]  = '{text[12:18]}'")   # Python

# Start ya stop chhod do
print(f"\ntext[:5]     = '{text[:5]}'")     # Hello (start=0)
print(f"text[6:]     = '{text[6:]}'")       # World Python (end tak)
print(f"text[:]      = '{text[:]}'")        # Puri string

# Step use karna [start:stop:step]
print(f"\ntext[::2]    = '{text[::2]}'")    # Har doosra character
print(f"text[::3]    = '{text[::3]}'")      # Har teesra character
print(f"text[0:10:2] = '{text[0:10:2]}'")  # 0 se 10 tak, doosra doosra

# String Reverse karna
print(f"\ntext[::-1]   = '{text[::-1]}'")   # Ulti string!

# Practical Examples
email = "user@example.com"
username = email[:email.index('@')]          # @ se pehle ka hissa
domain = email[email.index('@')+1:]         # @ ke baad ka hissa
print(f"\nEmail   : {email}")
print(f"Username: {username}")
print(f"Domain  : {domain}")


# ==========================================
# SECTION 4: Case Methods
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 4: Case Methods")
print("=" * 45)

sentence = "hello world from python"
mixed    = "hElLo WoRlD"

print(f"Original   : '{sentence}'")
print(f"upper()    : '{sentence.upper()}'")      # HELLO WORLD FROM PYTHON
print(f"lower()    : '{sentence.lower()}'")      # hello world from python
print(f"title()    : '{sentence.title()}'")      # Hello World From Python
print(f"capitalize(): '{sentence.capitalize()}'") # Hello world from python

print(f"\nOriginal   : '{mixed}'")
print(f"swapcase() : '{mixed.swapcase()}'")      # HeLlO wOrLd


# ==========================================
# SECTION 5: Search Methods
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 5: Search Methods")
print("=" * 45)

sentence = "Python is great and Python is fun"
word_to_find = "Python"

# find() - index deta hai, nahi mila toh -1
print(f"String: '{sentence}'")
print(f"\nfind('Python')    : {sentence.find('Python')}")     # 0
print(f"find('Python', 5) : {sentence.find('Python', 5)}")   # 19 (5 se aage dhundho)
print(f"find('Java')      : {sentence.find('Java')}")         # -1 (nahi mila)

# index() - find ki tarah, lekin nahi mila toh Error
print(f"\nindex('great')   : {sentence.index('great')}")      # 10

# count() - kitni baar aaya
print(f"\ncount('Python')  : {sentence.count('Python')}")     # 2
print(f"count('is')      : {sentence.count('is')}")           # 2
print(f"count('z')       : {sentence.count('z')}")            # 0

# startswith() aur endswith()
print(f"\nstartswith('Python') : {sentence.startswith('Python')}") # True
print(f"startswith('Java')   : {sentence.startswith('Java')}")   # False
print(f"endswith('fun')      : {sentence.endswith('fun')}")       # True
print(f"endswith('great')    : {sentence.endswith('great')}")     # False

# in operator
print(f"\n'great' in sentence  : {'great' in sentence}")          # True
print(f"'Java' in sentence   : {'Java' in sentence}")             # False
print(f"'python' in sentence : {'python' in sentence}")           # False (case sensitive!)


# ==========================================
# SECTION 6: Modify Methods
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 6: Modify Methods")
print("=" * 45)

# strip() - spaces hatao
messy = "   Hello World   "
print(f"Original  : '{messy}'")
print(f"strip()   : '{messy.strip()}'")          # 'Hello World'
print(f"lstrip()  : '{messy.lstrip()}'")         # 'Hello World   '
print(f"rstrip()  : '{messy.rstrip()}'")         # '   Hello World'

# replace() - word badlo
story = "I love cats. Cats are cute. My cat is Tom."
print(f"\nOriginal  : '{story}'")
print(f"replace() : '{story.replace('cat', 'dog')}'")
# I love dogs. Cats are cute. My dog is Tom.
# Note: 'Cats' nahi badla kyunki case sensitive hai

# replace with count limit
print(f"replace(limit=1): '{story.replace('cat', 'dog', 1)}'")

# split() - string ko list mein todo
csv_data = "John,25,Developer,New York"
parts = csv_data.split(',')
print(f"\nOriginal        : '{csv_data}'")
print(f"split(',')      : {parts}")
print(f"Naam            : {parts[0]}")
print(f"Umar            : {parts[1]}")
print(f"Profession      : {parts[2]}")
print(f"City            : {parts[3]}")

# Sentence words mein split karna
sentence = "Python is very powerful"
words = sentence.split()   # Default space par split
print(f"\n'{sentence}'.split() = {words}")

# join() - list ko string mein jodo
fruits = ["apple", "banana", "cherry", "mango"]
joined1 = ", ".join(fruits)
joined2 = " | ".join(fruits)
joined3 = "-".join(fruits)
print(f"\nList    : {fruits}")
print(f"join(,) : {joined1}")
print(f"join(|) : {joined2}")
print(f"join(-) : {joined3}")


# ==========================================
# SECTION 7: Check Methods
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 7: Check Methods")
print("=" * 45)

test_values = ["Hello123", "12345", "Hello", "   ", "UPPER", "lower"]

for val in test_values:
    print(f"\nValue: '{val}'")
    print(f"  isdigit()  : {val.isdigit()}")    # Sirf numbers?
    print(f"  isalpha()  : {val.isalpha()}")    # Sirf letters?
    print(f"  isalnum()  : {val.isalnum()}")    # Letters ya numbers?
    print(f"  isspace()  : {val.isspace()}")    # Sirf spaces?
    print(f"  isupper()  : {val.isupper()}")    # Sab capital?
    print(f"  islower()  : {val.islower()}")    # Sab small?


# ==========================================
# SECTION 8: Alignment Methods
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 8: Alignment Methods")
print("=" * 45)

word = "Python"
print(f"Original    : '{word}'")
print(f"center(20)  : '{word.center(20)}'")        # Center mein
print(f"center(20,*): '{word.center(20, '*')}'")   # * se fill karo
print(f"ljust(20)   : '{word.ljust(20)}'")         # Left align
print(f"ljust(20,.) : '{word.ljust(20, '.')}'")    # . se fill
print(f"rjust(20)   : '{word.rjust(20)}'")         # Right align
print(f"rjust(20,.) : '{word.rjust(20, '.')}'")    # . se fill

# zfill - zeros bharo (numbers ke liye useful)
order_id = "42"
print(f"\nOrder ID    : '{order_id}'")
print(f"zfill(6)    : '{order_id.zfill(6)}'")      # '000042'


# ==========================================
# SECTION 9: String Concatenation & Repetition
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 9: Concatenation & Repetition")
print("=" * 45)

first_name = "John"
last_name  = "Smith"

# Concatenation (+)
full_name = first_name + " " + last_name
print(f"First: {first_name}, Last: {last_name}")
print(f"Full Name (+): {full_name}")

# Repetition (*)
line     = "-" * 30
stars    = "⭐" * 5
ha       = "Ha" * 4

print(f"Line     : {line}")
print(f"Stars    : {stars}")
print(f"Laughter : {ha}!")


# ==========================================
# SECTION 10: f-Strings (Formatted Strings)
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 10: f-Strings")
print("=" * 45)

name    = "Emma Watson"
age     = 33
height  = 5.6
country = "UK"
gpa     = 3.87654

# Basic f-string
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"Height  : {height}")
print(f"Country : {country}")

# f-string mein expressions
print(f"\nAge in 10 years : {age + 10}")
print(f"Is adult?       : {age >= 18}")
print(f"Name uppercase  : {name.upper()}")
print(f"Name length     : {len(name)}")

# f-string formatting
print(f"\nGPA             : {gpa}")
print(f"GPA (2 decimal) : {gpa:.2f}")     # 3.88
print(f"GPA (4 decimal) : {gpa:.4f}")     # 3.8765

# Number formatting
big_num = 1234567.89
print(f"\nBig number      : {big_num}")
print(f"With commas     : {big_num:,.2f}")  # 1,234,567.89

# Width formatting
print(f"\n{'Name':<15} {'Age':>5} {'GPA':>6}")
print(f"{'Emma':<15} {33:>5} {3.8:>6.1f}")
print(f"{'James':<15} {28:>5} {3.5:>6.1f}")
print(f"{'Sophia':<15} {22:>5} {4.0:>6.1f}")


# ==========================================
# SECTION 11: Escape Characters
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 11: Escape Characters")
print("=" * 45)

# \n - New line
print("Line 1\nLine 2\nLine 3")

# \t - Tab
print("\nName:\tJohn")
print("Age:\t25")
print("City:\tNew York")

# \\ - Backslash
print("\nFile path: C:\\Users\\John\\Documents")

# \' and \" - Quotes inside strings
print("\nShe said: \"Hello World!\"")
print("It\'s a beautiful day")

# \r - Carriage return
print("\nWith \\r: Hello\rWorld")  # World overwrites Hello

# Raw string (r"") - Escape characters ignore karo
raw = r"C:\new_folder\test"
print(f"\nRaw string: {raw}")


# ==========================================
# SECTION 12: Practical Projects
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 12: Practical Projects")
print("=" * 45)

# --- Project 1: Username Generator ---
print("-- Username Generator --")
full_name = "  Robert Johnson  "
year = 1995

clean_name = full_name.strip()
parts = clean_name.split()
username = (parts[0][0] + parts[1]).lower() + str(year)
print(f"Full Name : '{full_name}'")
print(f"Username  : {username}")     # rjohnson1995

# --- Project 2: Password Validator ---
print("\n-- Password Strength Checker --")
password = "Python@2024"

has_upper   = any(c.isupper() for c in password)
has_lower   = any(c.islower() for c in password)
has_digit   = any(c.isdigit() for c in password)
has_special = any(c in "!@#$%^&*" for c in password)
is_long     = len(password) >= 8

print(f"Password     : {password}")
print(f"Has Uppercase: {has_upper}")
print(f"Has Lowercase: {has_lower}")
print(f"Has Digit    : {has_digit}")
print(f"Has Special  : {has_special}")
print(f"Long enough  : {is_long}")
is_strong = has_upper and has_lower and has_digit and has_special and is_long
print(f"Is Strong?   : {is_strong}")

# --- Project 3: Sentence Analyzer ---
print("\n-- Sentence Analyzer --")
text = "Python programming is fun and Python is powerful"
words = text.split()

print(f"Text      : '{text}'")
print(f"Length    : {len(text)} characters")
print(f"Words     : {len(words)}")
print(f"'Python' count : {text.count('Python')}")
print(f"Starts with 'Python': {text.startswith('Python')}")
print(f"Ends with 'powerful': {text.endswith('powerful')}")
print(f"Reversed  : {text[::-1]}")