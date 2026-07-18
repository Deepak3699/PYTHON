# Day 7 - while Loop

## Loop Kya Hota Hai?
- Loop ka matlab hai kisi kaam ko baar baar karna
- Real life example:
  * "Jab tak bhook lagi hai, khate raho"
  * "Jab tak password galat hai, dobara poocho"
  * "1 se 10 tak gino"
- Bina loop ke hume ek hi code 100 baar likhna padta
- Loop se hum ek baar likhte hain aur wo baar baar chalta hai

## while Loop Kya Hai?
- while loop tab tak chalta rehta hai jab tak condition True ho
- Jaise hi condition False hoti hai, loop band ho jata hai
- "Jab tak (while) yeh sach hai, yeh karo"

## while Loop Ki Syntax:
while condition:
    # Yeh code baar baar chalta hai
    # Jab tak condition True hai
    # Indentation (4 spaces) zaroori hai!

## Simple Example:
count = 1
while count <= 5:
    print(count)    # 1, 2, 3, 4, 5
    count += 1      # Har baar 1 badha do
                    # Warna loop kabhi band nahi hoga!

## Infinite Loop (Khatra!):
- Agar condition kabhi False na ho toh loop forever chalta hai
- Isko Infinite Loop kehte hain
- CTRL + C dabao loop band karne ke liye

### Infinite Loop Ka Example (Galat):
count = 1
while count <= 5:
    print(count)
    # count += 1 bhool gaye!
    # count kabhi nahi badhega
    # Loop forever chalega!

## break Statement:
- Loop ko forcefully band karne ke liye
- Jab bhi break mile, loop turant band ho jata hai
- Chahe condition True hi kyon na ho

### Example:
count = 0
while True:          # Hamesha True
    count += 1
    if count == 5:
        break        # count 5 hote hi band ho jao
print("Loop ended at:", count)

## continue Statement:
- Current iteration skip karne ke liye
- continue ke baad ka code us baar nahi chalta
- Loop agli iteration par chala jata hai

### Example:
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue     # Even numbers skip karo
    print(num)       # Sirf odd numbers print honge

## while - else:
- while ke saath else bhi likh sakte hain
- else ka code tab chalta hai jab loop normally
  khatam ho (break se nahi)

### Example:
count = 1
while count <= 3:
    print(count)
    count += 1
else:
    print("Loop finished normally!")

## Loop Counter (Counter Variable):
- Loop mein aksar ek variable hota hai jo count karta hai
- Isko counter/iterator variable kehte hain
- Har loop mein update karna zaroori hai

## Common Patterns:

### 1. Count Up:
i = 1
while i <= 10:
    print(i)
    i += 1

### 2. Count Down:
i = 10
while i >= 1:
    print(i)
    i -= 1

### 3. User Input Loop:
while True:
    answer = input("Continue? (yes/no): ")
    if answer == "no":
        break

### 4. Sum Calculator:
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
# total = 1+2+3+...+100 = 5050

## Aaj Hum Kya Seekha:
1. Loop kya hota hai aur kyun zaroori hai
2. while loop ki syntax
3. Infinite loop aur usse bachna
4. break - loop band karna
5. continue - iteration skip karna
6. while-else
7. Common loop patterns

## Kal Kya Seekhenge:
- for Loop
- range() function
- for loop ke saath strings aur lists