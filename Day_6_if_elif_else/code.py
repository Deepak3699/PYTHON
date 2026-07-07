# ============================================
# Day 6 - if / elif / else
# ============================================


# ==========================================
# SECTION 1: Simple if Statement
# ==========================================
print("=" * 45)
print("   SECTION 1: Simple if Statement")
print("=" * 45)

# Example 1: Basic if
temperature = 35

if temperature > 30:
    print("It's a hot day!")        # Yeh chalega
    print("Drink lots of water.")   # Yeh bhi chalega

# Example 2: Condition False hone par
score = 45

if score >= 50:
    print("You passed!")    # Yeh NAHI chalega (45 < 50)

print("Program continues...")  # Yeh hamesha chalta hai

# Example 3: Variable check karna
name = "Emma"

if name == "Emma":
    print(f"Hello, {name}! Welcome back.")

# Example 4: Multiple conditions
age = 25
has_license = True

if age >= 18 and has_license:
    print(f"Age {age} with license - You can drive!")


# ==========================================
# SECTION 2: if - else Statement
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 2: if - else Statement")
print("=" * 45)

# Example 1: Pass ya Fail
marks = 72

if marks >= 50:
    print(f"Marks: {marks} - PASSED ✓")
else:
    print(f"Marks: {marks} - FAILED ✗")

# Example 2: Even ya Odd
number = 17

if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")

# Example 3: Positive ya Negative
value = -8

if value >= 0:
    print(f"{value} is Positive (ya Zero)")
else:
    print(f"{value} is Negative")

# Example 4: String check
password = input("\nEnter password: ")

if password == "python123":
    print("Access Granted! ✓")
else:
    print("Wrong Password! Access Denied ✗")


# ==========================================
# SECTION 3: if - elif - else Statement
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 3: if - elif - else")
print("=" * 45)

# Example 1: Grade System
score = int(input("\nEnter your score (0-100): "))

if score >= 90:
    grade = "A"
    remark = "Excellent!"
elif score >= 80:
    grade = "B"
    remark = "Very Good!"
elif score >= 70:
    grade = "C"
    remark = "Good"
elif score >= 60:
    grade = "D"
    remark = "Satisfactory"
elif score >= 50:
    grade = "E"
    remark = "Needs Improvement"
else:
    grade = "F"
    remark = "Failed"

print(f"\nScore  : {score}")
print(f"Grade  : {grade}")
print(f"Remark : {remark}")

# Example 2: Day of Week
day_num = int(input("\nEnter day number (1-7): "))

if day_num == 1:
    day_name = "Monday"
elif day_num == 2:
    day_name = "Tuesday"
elif day_num == 3:
    day_name = "Wednesday"
elif day_num == 4:
    day_name = "Thursday"
elif day_num == 5:
    day_name = "Friday"
elif day_num == 6:
    day_name = "Saturday"
elif day_num == 7:
    day_name = "Sunday"
else:
    day_name = "Invalid! Enter 1-7"

print(f"Day {day_num} = {day_name}")

# Example 3: BMI Category
print("\n-- BMI Category --")
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi    = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
    advice   = "Eat more nutritious food"
elif bmi < 25:
    category = "Normal Weight"
    advice   = "Keep it up!"
elif bmi < 30:
    category = "Overweight"
    advice   = "Exercise regularly"
else:
    category = "Obese"
    advice   = "Consult a doctor"

print(f"\nBMI      : {bmi:.2f}")
print(f"Category : {category}")
print(f"Advice   : {advice}")


# ==========================================
# SECTION 4: Nested if
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 4: Nested if")
print("=" * 45)

# Example 1: Cinema Ticket System
age         = int(input("\nEnter your age: "))
has_ticket  = input("Do you have a ticket? (yes/no): ").lower()

if age >= 13:                           # Level 1
    if has_ticket == "yes":             # Level 2
        print("Welcome! Enjoy the movie 🎬")
    else:
        print("Please buy a ticket first.")
else:
    if has_ticket == "yes":             # Level 2
        print("Sorry, this movie is for 13+ only.")
    else:
        print("Too young AND no ticket. Cannot enter.")

# Example 2: Login System
print("\n-- Login System --")
username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "admin123":
        print("Welcome Admin! Full access granted.")
    elif password == "admin":
        print("Logged in but please change your password!")
    else:
        print("Wrong password for admin.")
else:
    if password == "user123":
        print(f"Welcome {username}! Limited access.")
    else:
        print("Invalid username or password.")


# ==========================================
# SECTION 5: Complex Conditions
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 5: Complex Conditions")
print("=" * 45)

# Example 1: Loan Eligibility
print("-- Loan Eligibility Checker --")
age           = int(input("Age: "))
monthly_income = float(input("Monthly income ($): "))
credit_score  = int(input("Credit score (300-850): "))
has_job       = input("Do you have a job? (yes/no): ").lower() == "yes"

# Multiple conditions with and / or
is_eligible = (
    age >= 21
    and monthly_income >= 3000
    and credit_score >= 650
    and has_job
)

if is_eligible:
    print("\n✓ Congratulations! You are eligible for a loan.")
    # Loan amount based on income
    if monthly_income >= 10000:
        max_loan = 100000
    elif monthly_income >= 5000:
        max_loan = 50000
    else:
        max_loan = 20000
    print(f"✓ Maximum loan amount: ${max_loan:,}")
else:
    print("\n✗ Sorry, you are not eligible.")
    # Reason batao
    if age < 21:
        print("  - Age must be 21 or above")
    if monthly_income < 3000:
        print("  - Income must be $3,000 or above")
    if credit_score < 650:
        print("  - Credit score must be 650 or above")
    if not has_job:
        print("  - Must be employed")


# ==========================================
# SECTION 6: in / not in Operator
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 6: in / not in Operator")
print("=" * 45)

# Example 1: Vowel check
letter = input("\nEnter a letter: ").lower()

if letter in "aeiou":
    print(f"'{letter}' is a VOWEL")
else:
    print(f"'{letter}' is a CONSONANT")

# Example 2: VIP List
vip_list = ["Emma", "James", "Sophia", "Oliver"]
visitor  = input("\nEnter your name: ")

if visitor in vip_list:
    print(f"Welcome, {visitor}! VIP access granted. 🌟")
else:
    print(f"Hello {visitor}. Standard access only.")

# Example 3: Banned words check
message      = input("\nEnter a message: ").lower()
banned_words = ["spam", "hack", "virus", "cheat"]
found_banned = False

for word in banned_words:
    if word in message:
        found_banned = True
        print(f"⚠ Warning: Message contains banned word '{word}'")

if not found_banned:
    print("✓ Message is clean!")


# ==========================================
# SECTION 7: Ternary (One Line if-else)
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 7: One Line if-else")
print("=" * 45)

# Format: value_if_true if condition else value_if_false

age    = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age} -> Status: {status}")

# Number positive check
num    = -5
result = "Positive" if num > 0 else "Negative or Zero"
print(f"{num} is: {result}")

# Even/Odd
n      = 42
parity = "Even" if n % 2 == 0 else "Odd"
print(f"{n} is: {parity}")

# Max of two numbers
a, b   = 15, 28
bigger = a if a > b else b
print(f"Bigger of {a} and {b} is: {bigger}")

# Grade (nested ternary - avoid karo, hard to read)
score  = 85
grade  = "A" if score >= 90 else "B" if score >= 80 else "C"
print(f"Score {score} -> Grade: {grade}")


# ==========================================
# SECTION 8: Practical Projects
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 8: Practical Projects")
print("=" * 45)

# --- Project 1: Simple ATM ---
print("-- ATM Machine --")
balance  = 5000.00
pin      = "1234"

entered_pin = input("\nEnter PIN: ")

if entered_pin == pin:
    print(f"Welcome! Your balance: ${balance:.2f}")
    action = input("Choose: (1) Withdraw  (2) Deposit  (3) Check Balance: ")

    if action == "1":
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= 0:
            print("Invalid amount!")
        elif amount > balance:
            print("Insufficient balance!")
        elif amount > 1000:
            print("Cannot withdraw more than $1000 at a time!")
        else:
            balance -= amount
            print(f"✓ Withdrawn: ${amount:.2f}")
            print(f"✓ New Balance: ${balance:.2f}")

    elif action == "2":
        amount = float(input("Enter amount to deposit: $"))
        if amount <= 0:
            print("Invalid amount!")
        else:
            balance += amount
            print(f"✓ Deposited: ${amount:.2f}")
            print(f"✓ New Balance: ${balance:.2f}")

    elif action == "3":
        print(f"Your Balance: ${balance:.2f}")

    else:
        print("Invalid option!")
else:
    print("Wrong PIN! Access Denied.")


# --- Project 2: Weather Advisor ---
print("\n-- Weather Advisor --")
temp     = float(input("\nCurrent temperature (°C): "))
is_raining = input("Is it raining? (yes/no): ").lower() == "yes"
is_windy   = input("Is it windy? (yes/no): ").lower() == "yes"

print("\nWeather Report:")
print("-" * 30)

if temp >= 35:
    print("🌡  Very Hot - Stay indoors if possible")
elif temp >= 25:
    print("☀  Warm - Light clothes recommended")
elif temp >= 15:
    print("🌤  Mild - A light jacket will do")
elif temp >= 5:
    print("🧥  Cold - Wear warm clothes")
else:
    print("🥶  Freezing - Heavy winter clothes!")

if is_raining:
    print("☔  Take an umbrella")
elif is_windy:
    print("💨  It's windy - Wear a windbreaker")
else:
    print("😊  Nice weather for a walk!")

if temp > 30 and is_raining:
    print("⚡  Possible thunderstorm - Be careful!")