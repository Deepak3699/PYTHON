# Day 5 - Strings and String Methods

## String Kya Hoti Hai?
- String ek sequence of characters (letters, numbers, symbols) hoti hai
- Quotes ke andar likhi jati hai
- Single (' '), Double (" "), ya Triple (''' ''' / """ """) quotes use hoti hain
- Python mein strings bohot powerful hain

## String Banane Ke Tarike:
name1 = 'John'           # Single quotes
name2 = "Sarah"          # Double quotes
para  = """Yeh ek        # Triple quotes (multiple lines)
multi line
string hai"""

## String Indexing (Har Character Ka Number):
- Har character ka ek index (number) hota hai
- Index 0 se shuru hota hai (left se right)
- Negative index bhi hota hai (-1 se shuru, right se left)

String  :  P  y  t  h  o  n
Index   :  0  1  2  3  4  5
Neg Idx : -6 -5 -4 -3 -2 -1

name = "Python"
name[0]   = 'P'   (pehla character)
name[5]   = 'n'   (chatha character)
name[-1]  = 'n'   (aakhri character)
name[-6]  = 'P'   (pehla character, ulti taraf se)

## String Slicing (Hissa Nikalna):
- String ka koi bhi hissa nikal sakte hain
- Format: string[start : stop : step]
- start: kahan se shuru (include)
- stop:  kahan tak (exclude - yeh index nahi aata)
- step:  kitne jump karke (default 1)

name = "Python"
name[0:3]   = "Pyt"   (0,1,2 - index 3 nahi)
name[2:5]   = "tho"   (2,3,4)
name[::2]   = "Pto"   (0,2,4 - har doosra)
name[::-1]  = "nohtyP" (ulta string)

## String Methods (Built-in Functions):

### Case Methods:
- upper()     : Sab capital kar do - "hello" -> "HELLO"
- lower()     : Sab small kar do   - "HELLO" -> "hello"
- title()     : Har word capital   - "hello world" -> "Hello World"
- capitalize(): Sirf pehla capital - "hello world" -> "Hello world"
- swapcase()  : Ulta kar do        - "Hello" -> "hELLO"

### Search Methods:
- find(x)    : x kahan hai? Index deta hai, nahi mila toh -1
- index(x)   : x kahan hai? Nahi mila toh Error deta hai
- count(x)   : x kitni baar aaya?
- startswith(x): x se shuru hai? True/False
- endswith(x): x par khatam? True/False
- in operator: x hai andar? True/False

### Modify Methods:
- strip()    : Dono taraf se spaces hatao
- lstrip()   : Left side se spaces hatao
- rstrip()   : Right side se spaces hatao
- replace(a,b): a ko b se badal do
- split(x)   : x par split karo, list banao
- join(list) : List ko string mein jodo

### Check Methods:
- isdigit()  : Sirf numbers hain? True/False
- isalpha()  : Sirf letters hain? True/False
- isalnum()  : Letters ya numbers? True/False
- isspace()  : Sirf spaces hain? True/False
- isupper()  : Sab capital? True/False
- islower()  : Sab small? True/False

### Other Methods:
- len()      : String ki length (kitne characters)
- zfill(n)   : Left mein zeros bharo
- center(n)  : Center mein rakho
- ljust(n)   : Left align karo
- rjust(n)   : Right align karo

## String Concatenation (Jodna):
- + operator se strings jod sakte hain
- "Hello" + " " + "World" = "Hello World"

## String Repetition (Repeat Karna):
- * operator se string repeat hoti hai
- "Ha" * 3 = "HaHaHa"

## f-String (Formatted String):
- f"" likhte hain aur {} mein variable dalete hain
- Sabse easy aur modern tarika hai
- name = "John"
- f"Hello {name}" = "Hello John"
- f"2 + 2 = {2+2}" = "2 + 2 = 4"

## Escape Characters:
- \n  : New line (naya line)
- \t  : Tab (space)
- \\  : Backslash
- \'  : Single quote
- \"  : Double quote

## Aaj Hum Kya Seekha:
1. String kya hai aur kaise banate hain
2. String indexing aur slicing
3. String methods (upper, lower, find, replace, etc.)
4. String concatenation aur repetition
5. f-Strings (formatted strings)
6. Escape characters

## Kal Kya Seekhenge:
- if / elif / else (Conditions)
- Program different decisions lena seekhega