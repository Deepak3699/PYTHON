# ============================================
# Day 7 - while Loop
# ============================================


# ==========================================
# SECTION 1: Basic while Loop
# ==========================================
print("=" * 45)
print("   SECTION 1: Basic while Loop")
print("=" * 45)

# Example 1: 1 se 5 tak print karo
print("-- Counting 1 to 5 --")
count = 1                    # Counter variable
while count <= 5:            # Condition
    print(f"Count: {count}") # Kaam karo
    count += 1               # Counter update karo (ZAROORI!)

print("Loop finished!\n")

# Example 2: Count down
print("-- Countdown --")
countdown = 10
while countdown >= 1:
    print(f"{countdown}...")
    countdown -= 1
print("🚀 Liftoff!\n")

# Example 3: Even numbers 2 se 20 tak
print("-- Even Numbers (2 to 20) --")
num = 2
while num <= 20:
    print(num, end=" ")
    num += 2
print()  # New line


# ==========================================
# SECTION 2: while Loop Visualization
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 2: Loop Visualization")
print("=" * 45)

# Step by step dekhte hain kya ho raha hai
print("-- Step by Step --")
i = 1
while i <= 5:
    print(f"  i={i} | Condition: {i} <= 5 is {i <= 5} | Printing: {i}")
    i += 1
print(f"  i={i} | Condition: {i} <= 5 is {i <= 5} | Loop ENDS")

# Multiplication table
print("\n-- Multiplication Table of 7 --")
multiplier = 1
while multiplier <= 10:
    result = 7 * multiplier
    print(f"  7 x {multiplier:2} = {result:3}")
    multiplier += 1


# ==========================================
# SECTION 3: while Loop with User Input
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 3: while with User Input")
print("=" * 45)

# Example 1: Password checker
print("-- Password Checker --")
correct_password = "python123"
attempts         = 0
max_attempts     = 3

while attempts < max_attempts:
    password = input(f"Enter password (Attempt {attempts + 1}/{max_attempts}): ")
    attempts += 1

    if password == correct_password:
        print("✓ Access Granted! Welcome!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"✗ Wrong password! {remaining} attempts left.")
        else:
            print("✗ Account locked! Too many wrong attempts.")


# Example 2: Number input validator
print("\n-- Age Input Validator --")
while True:
    try:
        age = int(input("Enter your age (1-120): "))
        if 1 <= age <= 120:
            print(f"✓ Valid age: {age}")
            break
        else:
            print("✗ Age must be between 1 and 120!")
    except ValueError:
        print("✗ Please enter a number only!")


# ==========================================
# SECTION 4: break Statement
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 4: break Statement")
print("=" * 45)

# Example 1: Simple break
print("-- Simple break --")
number = 0
while True:                  # Infinite loop
    number += 1
    print(f"Number: {number}")
    if number == 5:
        print("break executed!")
        break                # Loop band karo
print("After loop\n")

# Example 2: Search karna aur break
print("-- Search with break --")
fruits     = ["apple", "mango", "banana", "grape", "kiwi"]
search     = "banana"
found      = False
index      = 0

while index < len(fruits):
    print(f"  Checking: {fruits[index]}")
    if fruits[index] == search:
        found = True
        break
    index += 1

if found:
    print(f"✓ '{search}' found at index {index}!")
else:
    print(f"✗ '{search}' not found.")

# Example 3: First negative number dhundho
print("\n-- Find First Negative --")
numbers = [5, 12, 8, -3, 7, -9, 4]
i       = 0

while i < len(numbers):
    if numbers[i] < 0:
        print(f"First negative number: {numbers[i]} at index {i}")
        break
    i += 1


# ==========================================
# SECTION 5: continue Statement
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 5: continue Statement")
print("=" * 45)

# Example 1: Odd numbers print karo (even skip)
print("-- Odd Numbers only (skip evens) --")
num = 0
while num < 15:
    num += 1
    if num % 2 == 0:    # Even hai?
        continue        # Skip karo, agla number dekho
    print(num, end=" ") # Sirf odd print hoga
print()

# Example 2: Skip specific value
print("\n-- Skip number 5 --")
n = 0
while n < 10:
    n += 1
    if n == 5:
        print(f"  Skipping {n}!")
        continue
    print(f"  Number: {n}")

# Example 3: Valid input lena (empty skip karo)
print("\n-- Skip Empty Input --")
collected = []
print("Enter 3 valid names (empty input will be skipped):")

while len(collected) < 3:
    name = input(f"  Name {len(collected) + 1}: ").strip()
    if name == "":          # Empty input?
        print("  ⚠ Empty input! Try again.")
        continue            # Skip karo
    collected.append(name)

print(f"✓ Collected names: {collected}")


# ==========================================
# SECTION 6: while - else
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 6: while - else")
print("=" * 45)

# Example 1: Normal completion - else chalta hai
print("-- Normal Completion --")
count = 1
while count <= 3:
    print(f"  Count: {count}")
    count += 1
else:
    print("✓ else: Loop completed normally!")

# Example 2: break se - else nahi chalta
print("\n-- Break - else nahi chalta --")
count = 1
while count <= 5:
    print(f"  Count: {count}")
    if count == 3:
        print("  break!")
        break
    count += 1
else:
    print("This will NOT print (break used)")

print("After loop")

# Example 3: Prime number check (while-else ka best use)
print("\n-- Prime Number Check --")
num     = int(input("Enter a number to check if prime: "))
divisor = 2

if num < 2:
    print(f"{num} is NOT prime")
else:
    while divisor <= num // 2:
        if num % divisor == 0:
            print(f"{num} is NOT prime (divisible by {divisor})")
            break
        divisor += 1
    else:
        print(f"{num} IS prime! ✓")


# ==========================================
# SECTION 7: Nested while Loops
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 7: Nested while Loops")
print("=" * 45)

# Example 1: Multiplication table (all)
print("-- Multiplication Table (1-5) --")
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(f"{i*j:4}", end="")
        j += 1
    print()  # New line after each row
    i += 1

# Example 2: Pattern printing
print("\n-- Star Pattern --")
rows = 5
i    = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

# Example 3: Reverse pattern
print("\n-- Reverse Star Pattern --")
rows = 5
i    = rows
while i >= 1:
    j = 1
    while j <= i:
        print("★", end=" ")
        j += 1
    print()
    i -= 1


# ==========================================
# SECTION 8: Common while Loop Patterns
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 8: Common Patterns")
print("=" * 45)

# Pattern 1: Sum calculator
print("-- Sum of 1 to 100 --")
total = 0
i     = 1
while i <= 100:
    total += i
    i     += 1
print(f"Sum of 1 to 100 = {total}")  # 5050

# Pattern 2: Factorial
print("\n-- Factorial Calculator --")
n           = int(input("Enter n for n! : "))
factorial   = 1
counter     = 1
original_n  = n

while counter <= n:
    factorial *= counter
    counter   += 1

print(f"{original_n}! = {factorial}")

# Pattern 3: Digits sum
print("\n-- Sum of Digits --")
number     = int(input("Enter a number: "))
digit_sum  = 0
temp       = abs(number)    # Negative handle karo

while temp > 0:
    digit      = temp % 10   # Last digit nikalo
    digit_sum += digit       # Sum mein add karo
    temp      //= 10         # Last digit hatao
    
print(f"Sum of digits of {number} = {digit_sum}")

# Pattern 4: Reverse a number
print("\n-- Reverse a Number --")
number   = int(input("Enter a number to reverse: "))
reversed_num = 0
temp     = abs(number)

while temp > 0:
    digit        = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp        //= 10

print(f"Reversed: {reversed_num}")


# ==========================================
# SECTION 9: Practical Projects
# ==========================================
print("\n" + "=" * 45)
print("   SECTION 9: Practical Projects")
print("=" * 45)

# --- Project 1: Number Guessing Game ---
print("-- Number Guessing Game --")
import random
secret_number = random.randint(1, 100)
attempts      = 0
max_attempts  = 7

print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts.\n")

while attempts < max_attempts:
    try:
        guess    = int(input(f"Attempt {attempts+1}/{max_attempts} - Your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"🎉 Correct! The number was {secret_number}!")
            print(f"   You got it in {attempts} attempts!")
            break
        elif guess < secret_number:
            diff = secret_number - guess
            if diff <= 5:
                print("   📈 Too Low! But Very Close!")
            else:
                print("   📈 Too Low!")
        else:
            diff = guess - secret_number
            if diff <= 5:
                print("   📉 Too High! But Very Close!")
            else:
                print("   📉 Too High!")
    except ValueError:
        print(" enter ")
        
print(f"\n💀 Game Over! The number was {secret_number}")


# --- Project 2: Simple Menu System ---
print("\n-- Simple Calculator Menu --")
while True:
    print("\n" + "=" * 30)
    print("    CALCULATOR MENU")
    print("=" * 30)
    print("  1. Add")
    print("  2. Subtract")
    print("  3. Multiply")
    print("  4. Divide")
    print("  5. Exit")
    print("=" * 30)

    choice = input("Choose option (1-5): ")

    if choice == "5":
        print("Goodbye! 👋")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("⚠ Invalid option! Try again.")
        continue

    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print(f"Result: {a} + {b} = {a + b}")
    elif choice == "2":
        print(f"Result: {a} - {b} = {a - b}")
    elif choice == "3":
        print(f"Result: {a} * {b} = {a * b}")
    elif choice == "4":
        if b == 0:
            print("⚠ Cannot divide by zero!")
        else:
            print(f"Result: {a} / {b} = {a / b:.4f}")