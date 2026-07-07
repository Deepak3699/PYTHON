# Day 6 - if / elif / else (Conditions)

## Conditions Kya Hoti Hain?
- Real life mein hum har waqt decisions lete hain
- "Agar barish ho rahi hai toh chhata lo"
- "Agar score 90+ hai toh A grade, warna B grade"
- Python mein yahi kaam if/elif/else karta hai
- Program alag alag situations mein alag alag
  kaam karta hai

## if Statement:
- Sirf ek condition check karta hai
- Agar condition True hai toh andar ka code chalta hai
- Agar False hai toh kuch nahi hota

### Syntax:
if condition:
    # Yeh code tab chalta hai jab condition True ho
    # Indentation (4 spaces) ZAROORI hai!

### Example:
age = 20
if age >= 18:
    print("You are an adult")   # Yeh chalega

## if - else Statement:
- Agar condition True hai toh if wala code chale
- Agar condition False hai toh else wala code chale
- Dono mein se sirf EK hamesha chalta hai

### Syntax:
if condition:
    # True hone par
else:
    # False hone par

## if - elif - else Statement:
- Multiple conditions check karne ke liye
- elif = "else if" ka short form
- Jitni chahiye utni elif likh sakte hain
- Sirf PEHLI True condition ka code chalta hai
- Agar koi bhi True nahi toh else chalta hai

### Syntax:
if condition1:
    # condition1 True hone par
elif condition2:
    # condition2 True hone par
elif condition3:
    # condition3 True hone par
else:
    # Koi bhi True nahi hone par

## Indentation Kya Hai?
- Python mein spaces (4) bohot zaroori hain
- if ke andar ka code 4 spaces andar hona chahiye
- Bina indentation ke Error aayega!

### Sahi:
if True:
    print("Yeh sahi hai")   # 4 spaces andar

### Galat:
if True:
print("Yeh galat hai")   # Error! Indentation nahi

## Nested if (if ke andar if):
- Ek if ke andar doosra if likh sakte hain
- Har level par 4 spaces aur badhte hain

### Example:
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Show your ID")
else:
    print("Too young")

## Short Hand if (One Line):
- Chhoti condition ek line mein likh sakte hain
- x = "Adult" if age >= 18 else "Minor"

## Conditions mein kya use kar sakte hain?
- Comparison: ==, !=, >, <, >=, <=
- Logical   : and, or, not
- Membership: in, not in
- Identity  : is, is not

## Aaj Hum Kya Seekha:
1. if statement
2. if-else statement
3. if-elif-else statement
4. Nested if
5. One line if (Ternary)
6. Complex conditions (and, or, not)

## Kal Kya Seekhenge:
- while Loop
- Loop se repeat karna