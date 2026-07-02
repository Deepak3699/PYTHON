# ============================================
# Day 4 - Operators
# ============================================


# ==========================================
# SECTION 1: Arithmetic Operators
# ==========================================
print("=" * 45)
print("   SECTION 1: Arithmetic Operators")
print("=" * 45)

a = 17
b = 5

addition       = a + b    # 22
subtraction    = a - b    # 12
multiplication = a * b    # 85
division       = a / b    # 3.4 (hamesha float deta hai)
floor_division = a // b   # 3   (decimal part hata deta hai)
modulus        = a % b    # 2   (remainder / bacha hua)
exponent       = a ** b   # 1419857 (17 ki power 5)

print(f"a = {a}, b = {b}")
print("-" * 45)
print(f"Addition       : {a} + {b}  = {addition}")
print(f"Subtraction    : {a} - {b}  = {subtraction}")
print(f"Multiplication : {a} * {b}  = {multiplication}")
print(f"Division       : {a} / {b}  = {division}")
print(f"Floor Division : {a} // {b} = {floor_division}")
print(f"Modulus        : {a} % {b}  = {modulus}")
print(f"Exponent       : {a} ** {b} = {exponent}")


# ==========================================
# SECTION 2: Floor Division aur Modulus
#            Ki Deep Explanation
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 2: Floor Div & Modulus")
print("=" * 45)

# Floor Division Example
print("-- Floor Division (//) --")
print(f"10 // 3  = {10 // 3}")    # 3
print(f"20 // 6  = {20 // 6}")    # 3
print(f"15 // 4  = {15 // 4}")    # 3
print(f"7  // 2  = {7  // 2}")    # 3
print(f"-7 // 2  = {-7 // 2}")    # -4 (negative mein neeche jata hai)

# Modulus Example
print("\n-- Modulus (%) --")
print(f"10 % 3   = {10 % 3}")     # 1 (10 = 3*3 + 1)
print(f"20 % 6   = {20 % 6}")     # 2 (20 = 6*3 + 2)
print(f"15 % 5   = {15 % 5}")     # 0 (15 exactly 5 se divide hota hai)
print(f"7  % 2   = {7  % 2}")     # 1 (odd number)
print(f"8  % 2   = {8  % 2}")     # 0 (even number)

# Real Life Use: Even ya Odd check karna
number = 24
remainder = number % 2
print(f"\n{number} % 2 = {remainder}")
if remainder == 0:
    print(f"{number} is EVEN (Joft)")
else:
    print(f"{number} is ODD (Taaq)")

# Real Life Use: Seconds ko Minutes mein convert karna
total_seconds = 275
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"\n{total_seconds} seconds = {minutes} min {seconds} sec")


# ==========================================
# SECTION 3: Exponent (**) Deep Dive
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 3: Exponent (**)")
print("=" * 45)

print(f"2 ** 1  = {2 ** 1}")   # 2
print(f"2 ** 2  = {2 ** 2}")   # 4
print(f"2 ** 3  = {2 ** 3}")   # 8
print(f"2 ** 4  = {2 ** 4}")   # 16
print(f"2 ** 8  = {2 ** 8}")   # 256
print(f"2 ** 10 = {2 ** 10}")  # 1024
print(f"3 ** 3  = {3 ** 3}")   # 27
print(f"5 ** 4  = {5 ** 4}")   # 625

# Square Root (Square root bhi ** se hoti hai)
# Square root = ** (1/2)  ya  ** 0.5
print(f"\nSquare root of 25 = {25 ** 0.5}")   # 5.0
print(f"Square root of 81 = {81 ** 0.5}")   # 9.0
print(f"Square root of 144 = {144 ** 0.5}") # 12.0

# Cube root
print(f"\nCube root of 27  = {27 ** (1/3)}")  # 3.0
print(f"Cube root of 125 = {125 ** (1/3)}")  # 5.0


# ==========================================
# SECTION 4: Comparison Operators
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 4: Comparison Operators")
print("=" * 45)

x = 10
y = 20

print(f"x = {x}, y = {y}")
print("-" * 45)
print(f"x == y  (Equal?)              : {x == y}")
print(f"x != y  (Not Equal?)          : {x != y}")
print(f"x >  y  (Greater than?)       : {x > y}")
print(f"x <  y  (Less than?)          : {x < y}")
print(f"x >= y  (Greater or Equal?)   : {x >= y}")
print(f"x <= y  (Less or Equal?)      : {x <= y}")
print(f"x == 10 (x equals 10?)        : {x == 10}")

# Strings ko bhi compare kar sakte hain
print("\n-- String Comparison --")
name1 = "Alice"
name2 = "Bob"
name3 = "Alice"

print(f"'Alice' == 'Bob'   : {'Alice' == 'Bob'}")    # False
print(f"'Alice' == 'Alice' : {'Alice' == 'Alice'}")  # True
print(f"'Alice' != 'Bob'   : {'Alice' != 'Bob'}")    # True


# ==========================================
# SECTION 5: Logical Operators
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 5: Logical Operators")
print("=" * 45)

age = 22
has_license = True
has_car = False

print(f"age = {age}, has_license = {has_license}, has_car = {has_car}")
print("-" * 45)

# AND - Dono conditions poori honi chahiye
can_drive = (age >= 18) and (has_license == True)
print(f"\nCan drive? (age>=18 AND has_license): {can_drive}")

# OR - Koi ek condition poori ho
can_travel = has_license or has_car
print(f"Can travel? (has_license OR has_car): {can_travel}")

# NOT - Ulta kar do
is_minor = not (age >= 18)
print(f"Is minor? (NOT age>=18)             : {is_minor}")

# Complex Conditions
print("\n-- Complex Conditions --")
score = 75
attendance = 80

# Pass hone ke liye score >= 60 AND attendance >= 75 honi chahiye
is_pass = (score >= 60) and (attendance >= 75)
print(f"Score: {score}, Attendance: {attendance}%")
print(f"Passed? (score>=60 AND attend>=75)  : {is_pass}")

# Scholarship ke liye score >= 90 OR attendance == 100
scholarship = (score >= 90) or (attendance == 100)
print(f"Scholarship? (score>=90 OR att==100): {scholarship}")


# ==========================================
# SECTION 6: Truth Tables
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 6: Truth Tables")
print("=" * 45)

print("-- AND Truth Table --")
print(f"True  and True  = {True  and True}")   # True
print(f"True  and False = {True  and False}")  # False
print(f"False and True  = {False and True}")   # False
print(f"False and False = {False and False}")  # False

print("\n-- OR Truth Table --")
print(f"True  or True   = {True  or True}")    # True
print(f"True  or False  = {True  or False}")   # True
print(f"False or True   = {False or True}")    # True
print(f"False or False  = {False or False}")   # False

print("\n-- NOT Truth Table --")
print(f"not True  = {not True}")               # False
print(f"not False = {not False}")              # True


# ==========================================
# SECTION 7: Assignment Operators
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 7: Assignment Operators")
print("=" * 45)

score = 100
print(f"Starting score : {score}")

score += 25          # score = score + 25
print(f"After += 25    : {score}")   # 125

score -= 10          # score = score - 10
print(f"After -= 10    : {score}")   # 115

score *= 2           # score = score * 2
print(f"After *= 2     : {score}")   # 230

score //= 3          # score = score // 3
print(f"After //= 3    : {score}")   # 76

score %= 50          # score = score % 50
print(f"After %= 50    : {score}")   # 26

score **= 2          # score = score ** 2
print(f"After **= 2    : {score}")   # 676


# ==========================================
# SECTION 8: Operator Precedence (BODMAS)
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 8: Operator Precedence")
print("=" * 45)

# Python BODMAS follow karta hai
result1 = 2 + 3 * 4         # Pehle 3*4=12, phir 2+12=14
result2 = (2 + 3) * 4       # Pehle (2+3)=5, phir 5*4=20
result3 = 2 ** 3 + 1        # Pehle 2**3=8, phir 8+1=9
result4 = 10 - 4 / 2        # Pehle 4/2=2.0, phir 10-2.0=8.0
result5 = 10 % 3 + 1        # Pehle 10%3=1, phir 1+1=2

print(f"2 + 3 * 4     = {result1}  (Multiplication pehle)")
print(f"(2 + 3) * 4   = {result2}  (Brackets pehle)")
print(f"2 ** 3 + 1    = {result3}   (Exponent pehle)")
print(f"10 - 4 / 2    = {result4}  (Division pehle)")
print(f"10 % 3 + 1    = {result5}   (Modulus pehle)")


# ==========================================
# SECTION 9: Practical Projects
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 9: Practical Examples")
print("=" * 45)

# --- Project 1: Grade Calculator ---
print("-- Grade Calculator --")
marks_obtained = 78
total_marks    = 100

percentage = (marks_obtained / total_marks) * 100
is_passed  = percentage >= 50

print(f"Marks     : {marks_obtained}/{total_marks}")
print(f"Percentage: {percentage}%")
print(f"Passed?   : {is_passed}")

# --- Project 2: Circle Area ---
print("\n-- Circle Area Calculator --")
radius = 7
pi     = 3.14159

area        = pi * radius ** 2
circumference = 2 * pi * radius

print(f"Radius       : {radius}")
print(f"Area         : {area:.2f}")
print(f"Circumference: {circumference:.2f}")

# --- Project 3: Loan EMI Calculator ---
print("\n-- Simple Loan EMI Calculator --")
loan_amount     = 100000
annual_interest = 12     # 12% per year
months          = 24     # 2 saal

monthly_interest = annual_interest / 12 / 100
emi = (loan_amount * monthly_interest) / (1 - (1 + monthly_interest) ** (-months))

print(f"Loan Amount   : ${loan_amount}")
print(f"Interest Rate : {annual_interest}% per year")
print(f"Duration      : {months} months")
print(f"Monthly EMI   : ${emi:.2f}")
total_payment = emi * months
print(f"Total Payment : ${total_payment:.2f}")
print(f"Total Interest: ${(total_payment - loan_amount):.2f}")