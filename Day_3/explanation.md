# Day 3 - User Input and Type Casting

## User Input Kya Hota Hai?
- Ab tak hum code mein khud values likh rahe the (Hardcoded)
- Lekin real programs mein user khud data enter karta hai
- Python mein `input()` function use hota hai user se data lene ke liye
- Jab `input()` chalta hai, program ruk jata hai aur user ke type karne ka wait karta hai

## input() Ka Basic Use:
name = input("Apna naam likhein: ")
print("Hello", name)

### Zaroori Baat:
- `input()` function hamesha data ko **String (str)** format mein leta hai
- Chahe aap number likhein ya text, Python usko text (string) hi samjhega

## The Problem (Masla Kya Hai?)
Agar hum user se 2 numbers lein aur unko add karein:
num1 = input("Pehla number: ") # User ne 10 likha
num2 = input("Doosra number: ") # User ne 20 likha
print(num1 + num2) 
# Output aayega: 1020 (Kyunki yeh text ko jod raha hai, numbers ko nahi!)

## Type Casting Kya Hai?
- Ek data type ko doosre data type mein convert karne ko Type Casting kehte hain
- Upar wale masle ko hal karne ke liye humein string ko number mein badalna hoga

### 1. int() - String ya Float ko Integer mein badalna
number = int("50")  # Ab yeh text nahi, pure number hai

### 2. float() - String ya Int ko Decimal Number mein badalna
price = float("99.5") # Ab yeh decimal number hai

### 3. str() - Kisi bhi cheez ko String (Text) mein badalna
age = str(25) # Ab 25 number nahi, text ban gaya hai

### 4. bool() - Kisi cheez ko True ya False mein badalna
- Khali string `""` ya number `0` hamesha `False` hota hai
- Baaki har cheez `True` hoti hai

## Type Casting Ke Saath Sahi Addition:
num1 = int(input("Pehla number: "))  # Input lete hi int mein convert
num2 = int(input("Doosra number: "))
print(num1 + num2) 
# Output aayega: 30 (Bilkul sahi!)

## Aaj Hum Kya Seekha:
1. `input()` function se user se data lena
2. Input hamesha string hota hai
3. Type casting kya hoti hai
4. `int()`, `float()`, `str()`, aur `bool()` functions
5. User input se simple calculator banana

## Kal Kya Seekhenge:
- Arithmetic Operators (+, -, *, /, //, %, **)
- Numbers ke saath advanced calculations