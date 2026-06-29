# ============================================
# Day 1 - Python Introduction
# ============================================
# Yeh file Day 1 ke saare concepts dikhati hai
# ============================================


# ----- SECTION 1: Hello World -----

print("Hello, World!")  # Sabse pehla program

print("Mera naam Python hai!")  # Koi bhi text print kar sakte hain


# ----- SECTION 2: print() ke different uses -----

# Sirf ek cheez print karna
print("Namaste!")

# Ek saath kai cheezein print karna (comma se alag karo)
print("Mera naam", "Deepak", "hai")

# Numbers bhi print ho sakte hain
print(100)
print(3.14)

# Numbers aur text saath mein
print("Meri umar hai", 20, "saal")


# ----- SECTION 3: Blank Lines print karna -----

print("Pehli line")
print()  # Yeh blank line print karega
print("Teesri line")


# ----- SECTION 4: Comments -----

# Yeh ek single line comment hai
# Python in lines ko ignore karta hai
# Sirf programmer ke notes ke liye hain

"""
This is a multi-line comment
using triple quotes.
It won't run because it's not assigned.

"""

print('''
         hello 
         how are you 
         using this you can write multiple lines ''')



print("Comments code ko samajhne mein help karte hain")

# Aap comment ko code ke saath bhi likh sakte hain:
print("Hello")  # Yeh Hello print karega


# ----- SECTION 5: Special Characters in print -----

# \n - New Line (naya line shuru karna)
print("Pehli Line\nDoosri Line\nTeesri Line")

# \t - Tab (space dene ke liye)
print("Name:\tDeep")
print("Age:\t20")

# Asterisks se design banana
print("*" * 30)  # 30 baar * print hoga
print("*   Python Full Course   *")
print("*" * 30)


# ----- SECTION 6: sep aur end parameter -----

# sep = separator (items ke beech kya aaye)
print("Deep", "ak", "kumar", sep="-")
# Output: Deep-ak-kumar

print("2024", "01", "15", sep="/")
# Output: 2024/01/15

# end = line ke ant mein kya aaye (default hai \n yaani new line)
print("Hello ", end="")  # Line nahi badlega
print("World!")  # Isi line mein print hoga
# Output: Hello World!


# ----- SECTION 7: Program Information Print Karna -----

print("=" * 40)
print("      PYTHON FULL COURSE")
print("      By: [Aapka Naam]")
print("      Day: 1 - Introduction")
print("=" * 40)
print()
print("Python Version: 3.x")
print("Topic: Hello World aur Print Function")
print("=" * 40)
