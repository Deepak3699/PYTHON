# Day 2 - Variables and Data Types

## Variable Kya Hota Hai?
- Variable ek box ki tarah hota hai
- Jisme hum data/information store karte hain
- Baad mein us data ko use kar sakte hain

## Real Life Example:
- Socho tumhare paas ek dabba hai
- Us dabba ka naam hai "name"
- Us mein tumne "Deepak" rakha
- Ab jab bhi "name" bulao, "Deepak" milega

## Variable Banane Ka Tarika:
variable_naam = value

## Variable Naming Rules:
✅ Sahi tarike:
- name = "Deepak"
- my_age = 20
- total_marks = 95
- _private = "hidden"
- name2 = "Kumar"

❌ Galat tarike:
- 2name = "Deepak"      # Number se shuru nahi ho sakta
- my-age = 20        # Hyphen use nahi hota
- my age = 20        # Space nahi hoti
- for = "Deepak"        # Python keywords use nahi hote

## Data Types Kya Hain?
- Python mein alag alag tarah ka data hota hai
- Har data ka ek type hota hai

### 1. int (Integer) - Pure Numbers
- Decimal point nahi hota
- Example: 5, 100, -20, 0

### 2. float (Floating Point) - Decimal Numbers  
- Decimal point hota hai
- Example: 3.14, -2.5, 100.0

### 3. str (String) - Text
- Quotes mein likha jata hai
- Single ya double quotes dono chalte hain
- Example: "Deepak", 'Hello', "123"

### 4. bool (Boolean) - True ya False
- Sirf do values hoti hain: True ya False
- Capital T aur F zaroor hona chahiye
- Example: True, False

### 5. NoneType - Koi Value Nahi
- None matlab khaali / koi value nahi
- Example: None

## type() Function:
- Kisi bhi variable ka type pata karne ke liye
- type(variable_naam) likhte hain

## Multiple Variables:
### Ek ek karke:
x = 10
y = 20
z = 30

### Ek saath (multiple assignment):
x, y, z = 10, 20, 30

### Sab mein same value:
x = y = z = 0

## Variable Ki Value Change Karna:
name = "Deepak"
print(name)   # Deepak
name = "Ahmed"
print(name)   # Ahmed

## Type Checking:
isinstance(value, type)  # True ya False return karta hai

## Aaj Hum Kya Seekha:
1. Variable kya hai aur kaise banate hain
2. Variable naming rules
3. 5 main data types (int, float, str, bool, None)
4. type() function
5. Multiple assignment
6. isinstance() function

## Kal Kya Seekhenge:
- User se input lena
- Type casting (ek type se doosre type mein convert karna)