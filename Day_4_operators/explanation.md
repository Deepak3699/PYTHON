# Day 4 - Operators

## Operator Kya Hota Hai?
- Operator ek symbol hai jo values par koi operation karta hai
- Jaise + ka matlab add karna, - ka matlab minus karna
- Jis value par operation hota hai usse "Operand" kehte hain
- Example: 10 + 5 mein `+` operator hai aur `10`, `5` operands hain

## Python Mein Kitne Tarah Ke Operators Hain?

### 1. Arithmetic Operators (Hisaab wale)
- Calculations ke liye use hote hain

| Operator | Naam            | Example  | Result |
|----------|-----------------|----------|--------|
| +        | Addition        | 10 + 3   | 13     |
| -        | Subtraction     | 10 - 3   | 7      |
| *        | Multiplication  | 10 * 3   | 30     |
| /        | Division        | 10 / 3   | 3.333  |
| //       | Floor Division  | 10 // 3  | 3      |
| %        | Modulus         | 10 % 3   | 1      |
| **       | Exponent        | 10 ** 3  | 1000   |

### Floor Division (//) Kya Hai?
- Normal division ke baad decimal part hata deta hai
- Sirf poora number (integer) deta hai
- Example: 10 // 3 = 3 (3.333 mein se .333 hat gaya)

### Modulus (%) Kya Hai?
- Division ke baad jo BACHA woh deta hai (remainder)
- Example: 10 % 3 = 1 (10 ko 3 se divide karo, 1 bachta hai)
- Use: Check karna k number even hai ya odd

### Exponent (**) Kya Hai?
- Power (quwwat) calculate karta hai
- Example: 2 ** 3 = 8 (2 ki power 3 = 2 x 2 x 2)

---

### 2. Comparison Operators (Tulna karne wale)
- Do values ko compare karte hain
- Result hamesha True ya False hota hai

| Operator | Naam                  | Example  | Result |
|----------|-----------------------|----------|--------|
| ==       | Equal to              | 5 == 5   | True   |
| !=       | Not Equal to          | 5 != 3   | True   |
| >        | Greater than          | 5 > 3    | True   |
| <        | Less than             | 5 < 3    | False  |
| >=       | Greater than or equal | 5 >= 5   | True   |
| <=       | Less than or equal    | 5 <= 3   | False  |

### Zaroori Baat:
- `=` aur `==` mein farq hai!
- `=`  matlab: value assign karna (x = 5)
- `==` matlab: check karna k equal hai ya nahi (x == 5)

---

### 3. Logical Operators (Shart wale)
- Multiple conditions ko ek saath check karte hain

| Operator | Matlab                          | Example           |
|----------|---------------------------------|-------------------|
| and      | Dono shart poori ho             | True and True     |
| or       | Koi ek shart poori ho           | True or False     |
| not      | Ulta kar do (True->False)       | not True          |

### and Operator:
- Sirf True deta hai jab DONO conditions True hon
- True and True   = True
- True and False  = False
- False and True  = False
- False and False = False

### or Operator:
- True deta hai jab KISI EK condition True ho
- True or True    = True
- True or False   = True
- False or True   = True
- False or False  = False

### not Operator:
- Value ko ulta kar deta hai
- not True  = False
- not False = True

---

### 4. Assignment Operators (Value dene wale)
- Variable mein value store karte hain

| Operator | Example   | Matlab            |
|----------|-----------|-------------------|
| =        | x = 10    | x mein 10 rakho   |
| +=       | x += 5    | x = x + 5        |
| -=       | x -= 5    | x = x - 5        |
| *=       | x *= 5    | x = x * 5        |
| /=       | x /= 5    | x = x / 5        |
| //=      | x //= 5   | x = x // 5       |
| %=       | x %= 5    | x = x % 5        |
| **=      | x **= 5   | x = x ** 5       |

---

## Operator Precedence (Konsa Pehle Chalta Hai?)
- Jaise Math mein BODMAS hota hai, Python mein bhi order hota hai
- ** (Exponent)     - Sabse pehle
- * / // %          - Doosre
- + -               - Teesre
- Comparison        - Chaauthe
- Logical (not, and, or) - Sabse baad

## Aaj Hum Kya Seekha:
1. Arithmetic Operators (+, -, *, /, //, %, **)
2. Comparison Operators (==, !=, >, <, >=, <=)
3. Logical Operators (and, or, not)
4. Assignment Operators (=, +=, -= etc.)
5. Operator Precedence (BODMAS)

## Kal Kya Seekhenge:
- Strings (Text) ke saath kaam karna
- String Methods (upper, lower, replace, etc.)