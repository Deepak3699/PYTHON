# ============================================
# Day 2 - Variables and Data Types
# ============================================


# ==========================================
# SECTION 1: Variable Banana (Creating Variables)
# ==========================================

# Variable = Value
name = "Deepak"        # String variable
age = 20                  # Integer variable
height = 5.8              # Float variable
is_student = True         # Boolean variable
middle_name = None        # None variable

print("=" * 40)
print("SECTION 1: Variables")
print("=" * 40)
print("Naam:", name)
print("Umar:", age)
print("Qad:", height)
print("Student hai?", is_student)
print("Middle Name:", middle_name)


# ==========================================
# SECTION 2: Data Types - int (Integer)
# ==========================================

print("\n" + "=" * 40)
print("SECTION 2: int (Integer)")
print("=" * 40)

positive_number = 100       # Positive integer
negative_number = -50       # Negative integer
zero = 0                    # Zero
big_number = 1000000        # Bara number
binary_num = 0b1010         # Binary (0b se shuru)
octal_num = 0o17            # Octal (0o se shuru)
hex_num = 0xFF              # Hexadecimal (0x se shuru)

print("Positive:", positive_number)
print("Negative:", negative_number)
print("Zero:", zero)
print("Bara Number:", big_number)
print("Binary 0b1010:", binary_num)       # 10
print("Octal 0o17:", octal_num)           # 15
print("Hex 0xFF:", hex_num)               # 255

# Type check
print("Type:", type(positive_number))     # <class 'int'>
print(type(name))                         # <class 'str'>

# ==========================================
# SECTION 3: Data Types - float
# ==========================================

print("\n" + "=" * 40)
print("SECTION 3: float (Decimal Numbers)")
print("=" * 40)

pi = 3.14159              # Pi ki value
temperature = -10.5       # Negative float
price = 99.99             # Price
scientific = 1.5e3        # Scientific notation (1500.0)
scientific2 = 2.5e-2      # Scientific notation (0.025)

print("Pi:", pi)
print("Temperature:", temperature)
print("Price:", price)
print("Scientific 1.5e3:", scientific)    # 1500.0
print("Scientific 2.5e-2:", scientific2)  # 0.025
print("Type:", type(pi))                  # <class 'float'>


# ==========================================
# SECTION 4: Data Types - str (String)
# ==========================================

print("\n" + "=" * 40)
print("SECTION 4: str (String / Text)")
print("=" * 40)

# Different ways to write strings
single_quote = 'Hello'              # Single quotes
double_quote = "World"              # Double quotes
triple_quote = """Yeh ek
multi-line
string hai"""                       # Triple quotes - multiple lines

# String with numbers (number nahi hai yeh!)
phone = "0300-1234567"
postal_code = "54000"

print("Single Quote:", single_quote)
print("Double Quote:", double_quote)
print("Triple Quote String:")
print(triple_quote)
print("Phone:", phone)
print("Type of phone:", type(phone))   # <class 'str'>
print("Type of '123':", type("123"))   # str hai, int nahi!


# ==========================================
# SECTION 5: Data Types - bool (Boolean)
# ==========================================

print("\n" + "=" * 40)
print("SECTION 5: bool (Boolean)")
print("=" * 40)

is_raining = True
is_sunny = False
has_job = True
is_married = False

print("Barish ho rahi hai?", is_raining)
print("Dhoop hai?", is_sunny)
print("Job hai?", has_job)
print("Shadi hui?", is_married)
print("Type:", type(is_raining))      # <class 'bool'>

# Boolean ki value numbers mein
print("\nBoolean as Numbers:")
print("True ki value:", int(True))    # 1
print("False ki value:", int(False))  # 0


# ==========================================
# SECTION 6: Data Types - None
# ==========================================

print("\n" + "=" * 40)
print("SECTION 6: NoneType")
print("=" * 40)

result = None
user_input = None
pending_task = None

print("Result:", result)
print("User Input:", user_input)
print("Type:", type(result))          # <class 'NoneType'>

# None check karna
print("Result None hai?", result is None)   # True
print("Result None hai?", result == None)   # True (dono chalte hain)


# ==========================================
# SECTION 7: type() Function
# ==========================================

print("\n" + "=" * 40)
print("SECTION 7: type() Function")
print("=" * 40)

# Alag alag values ka type check karna
print("type(100)    :", type(100))
print("type(3.14)   :", type(3.14))
print("type('Deep')  :", type("Deep"))
print("type(True)   :", type(True))
print("type(None)   :", type(None))

# Variables ka type check
x = 42
y = "Python"
z = 3.14

print("\nVariables ke types:")
print(f"x = {x}, type = {type(x)}") # using f string      x = 42 , type = <class 'int'>
print(f"y = {y}, type = {type(y)}")
print(f"z = {z}, type = {type(z)}")


# ==========================================
# SECTION 8: Multiple Assignment
# ==========================================

print("\n" + "=" * 40)
print("SECTION 8: Multiple Assignment")
print("=" * 40)

# Method 1: Ek ek karke
a = 10
b = 20
c = 30
print("Method 1:", a, b, c)

# Method 2: Ek line mein multiple variables
x, y, z = 100, 200, 300
print("Method 2:", x, y, z)

# Method 3: Sab mein same value
p = q = r = 0
print("Method 3:", p, q, r)

# Method 4: String unpack karna
first, second, third = "ABC"
print("Method 4 (String unpack):", first, second, third)

# Swap karna (values exchange karna) - Python ka special trick!
num1 = 5
num2 = 10
print("\nPehle:", num1, num2)  # 5 10 
num1, num2 = num2, num1          # Swap!
print("Baad mein:", num1, num2)  # 10 5


# ==========================================
# SECTION 9: Variable Ki Value Change Karna
# ==========================================

print("\n" + "=" * 40)
print("SECTION 9: Variable Update Karna")
print("=" * 40)

# Variable ki value change ho sakti hai
score = 0
print("Shuruaat:", score)

score = 10
print("Pehle kaam ke baad:", score)

score = 50
print("Doosre kaam ke baad:", score)

score = 100
print("Final score:", score)

# Ek interesting cheez - type bhi change ho sakti hai!
data = 100           # int
print("\nData (int):", data, type(data))

data = "Sab Data"   # ab string ban gaya
print("Data (str):", data, type(data))

data = 3.14         # ab float ban gaya
print("Data (float):", data, type(data))


# ==========================================
# SECTION 10: isinstance() Function
# ==========================================

print("\n" + "=" * 40)
print("SECTION 10: isinstance() Function")
print("=" * 40)

name = "Deep"
age = 20
gpa = 3.8
is_pass = True

# isinstance(variable, DataType) - True ya False deta hai
print("name string hai?", isinstance(name, str))    # True
print("age integer hai?", isinstance(age, int))     # True
print("gpa float hai?", isinstance(gpa, float))     # True
print("is_pass bool hai?", isinstance(is_pass, bool)) # True

# Wrong type check
print("\nWrong type checks:")
print("name integer hai?", isinstance(name, int))   # False
print("age string hai?", isinstance(age, str))      # False


# ==========================================
# SECTION 11: Practical Example - Student Record
# ==========================================

print("\n" + "=" * 40)
print("SECTION 11: Student Record")
print("=" * 40)

# Student ki information variables mein store karna
student_name = "Deep"
student_age = 19
student_gpa = 3.75
student_roll = "CS-2024-001"
is_scholarship = True
failed_subjects = None

# Achi tarah se print karna
print("╔" + "=" * 35 + "=╗")
print("║      STUDENT RECORD CARD           ║")
print("╠" + "═" * 35 + "=╣")
print(f"║ Naam    : {student_name:<24} ║")
print(f"║ Umar    : {student_age:<24} ║")
print(f"║ GPA     : {student_gpa:<24} ║")
print(f"║ Roll No : {student_roll:<24} ║")
print(f"║ Scholarship: {str(is_scholarship):<21} ║")
print(f"║ Failed  : {str(failed_subjects):<24} ║")
print("╚" + "═" * 35 + "╝")

print("\nData Types of Variables:")
print(f"  student_name  -> {type(student_name)}")
print(f"  student_age   -> {type(student_age)}")
print(f"  student_gpa   -> {type(student_gpa)}")
print(f"  student_roll  -> {type(student_roll)}")
print(f"  is_scholarship-> {type(is_scholarship)}")
print(f"  failed_subjects->{type(failed_subjects)}")