# ============================================
# Day 3 - User Input & Type Casting
# ============================================

# ==========================================
# SECTION 1: Basic Input
# ==========================================
print("=" * 40)
print("SECTION 1: User Se Data Lena")
print("=" * 40)

# input("Message") - Message screen par show hoga
user_name = input("Apna naam type karein: ")
city = input("Apne city ka naam type karein: ")

print("\n--- Result ---")
print("Hello " + user_name + "! Welcome to Python.")
print("Oh, " + city + " ek bohot achi jagah hai!")

# Type check karke dekhte hain
print("user_name ka type:", type(user_name))


# ==========================================
# SECTION 2: The Input Problem (String Trap)
# ==========================================
print("\n" + "=" * 40)
print("SECTION 2: Input hamesha String hota hai")
print("=" * 40)

print("Let's add two numbers!")
num1 = input("Pehla number enter karein (e.g., 10): ")
num2 = input("Doosra number enter karein (e.g., 20): ")

result = num1 + num2
# Agar user 10 aur 20 daalega, output 1020 aayega, 30 nahi!
print("Bina convert kiye Result:", result) 


# ==========================================
# SECTION 3: Type Casting to int()
# ==========================================
print("\n" + "=" * 40)
print("SECTION 3: Text ko Integer mein badalna")
print("=" * 40)

# Upar wale problem ko solve karte hain
print("Ab sahi tarike se add karte hain!")

# Method 1: Do lines mein
val1_str = input("Enter Number A: ")
val1_int = int(val1_str)  # String se Integer ban gaya

# Method 2: Ek line mein (Recommended)
val2_int = int(input("Enter Number B: "))

correct_result = val1_int + val2_int
print("Sahi Result:", correct_result)


# ==========================================
# SECTION 4: Type Casting to float()
# ==========================================
print("\n" + "=" * 40)
print("SECTION 4: Decimal numbers ke liye float()")
print("=" * 40)

# Agar user se price ya weight lena ho toh float() use karein
price = float(input("Product ki price enter karein (e.g., 99.99): "))
quantity = int(input("Kitni items khareedni hain? "))

total_bill = price * quantity
print("Aapka Total Bill hua: $" + str(total_bill)) # str() use kiya print ke liye


# ==========================================
# SECTION 5: Different Conversions
# ==========================================
print("\n" + "=" * 40)
print("SECTION 5: Other Type Casts")
print("=" * 40)

# 1. Number se String
age = 25
# print("My age is " + age)  # Yeh ERROR dega (String aur Int direct add nahi hote)
print("My age is " + str(age)) # Yeh SAHI hai

# 2. String/Numbers se Boolean
print("\nbool() Conversion:")
print('bool("Alex")  ->', bool("Alex"))     # True (Kyunki string khaali nahi hai)
print('bool("")      ->', bool(""))         # False (Khaali string)
print('bool(1)       ->', bool(1))          # True
print('bool(0)       ->', bool(0))          # False

# 3. Float se Int (Decimal remove ho jayega)
gpa = 3.8
gpa_int = int(gpa)
print("\nFloat se Int:")
print(f"Original: {gpa}, Integer banne ke baad: {gpa_int}")


# ==========================================
# SECTION 6: Practical Example - Age Calculator
# ==========================================
print("\n" + "=" * 40)
print("SECTION 6: Mini Project - Age Calculator")
print("=" * 40)

current_year = 2024
birth_year = int(input("Aap kis saal mein paida hue thay? (e.g., 1995): "))

calculated_age = current_year - birth_year

print("\n--- Profile ---")
print("Current Year :", current_year)
print("Birth Year   :", birth_year)
print("Aapki umar   :", calculated_age, "saal hai!")