# 📚 Python ke ALL Built-in Methods (Sab ke Sab!)

---

## 1️⃣ STRING METHODS (str)

### 🔹 Case Conversion
```python
text = "Hello World"
```
| Method | Example | Output |
|--------|---------|--------|
| `lower()` | `"HELLO".lower()` | `hello` |
| `upper()` | `"hello".upper()` | `HELLO` |
| `title()` | `"hello world".title()` | `Hello World` |
| `capitalize()` | `"hello world".capitalize()` | `Hello world` |
| `swapcase()` | `"Hello".swapcase()` | `hELLO` |
| `casefold()` | `"HELLO".casefold()` | `hello` (stronger than lower) |

---

### 🔹 Search & Find
| Method | Kaam | Example |
|--------|------|---------|
| `find()` | Position dhundta hai | `"hello".find("l")` → `2` |
| `rfind()` | Right se dhundta hai | `"hello".rfind("l")` → `3` |
| `index()` | Find jaisa (error deta hai) | `"hello".index("l")` → `2` |
| `rindex()` | Right se index | `"hello".rindex("l")` → `3` |
| `count()` | Kitni baar aaya | `"hello".count("l")` → `2` |

---

### 🔹 Check/Verify Methods (Returns True/False)
| Method | Kaam |
|--------|------|
| `startswith()` | Starting check |
| `endswith()` | Ending check |
| `isalpha()` | Sirf letters? |
| `isdigit()` | Sirf digits? |
| `isalnum()` | Letters + Digits? |
| `isnumeric()` | Numeric? |
| `isdecimal()` | Decimal? |
| `islower()` | Sab lowercase? |
| `isupper()` | Sab uppercase? |
| `istitle()` | Title case? |
| `isspace()` | Sirf spaces? |
| `isidentifier()` | Valid variable name? |
| `isprintable()` | Printable hai? |
| `isascii()` | ASCII characters? |

```python
print("hello".isalpha())      # True
print("123".isdigit())        # True
print("hello123".isalnum())   # True
print("Hello World".istitle()) # True
print("   ".isspace())        # True
```

---

### 🔹 Strip (Space Remove)
| Method | Kaam |
|--------|------|
| `strip()` | Dono taraf se space hatao |
| `lstrip()` | Left se space hatao |
| `rstrip()` | Right se space hatao |

```python
text = "  hello  "
print(text.strip())   # "hello"
print(text.lstrip())  # "hello  "
print(text.rstrip())  # "  hello"
```

---

### 🔹 Split & Join
| Method | Kaam |
|--------|------|
| `split()` | String → List |
| `rsplit()` | Right se split |
| `splitlines()` | Lines me split |
| `join()` | List → String |
| `partition()` | 3 parts me todo |
| `rpartition()` | Right se 3 parts |

```python
"a,b,c".split(",")          # ['a', 'b', 'c']
",".join(['a','b','c'])      # 'a,b,c'
"hello\nworld".splitlines()  # ['hello', 'world']
"hello world python".partition(" ")  # ('hello', ' ', 'world python')
```

---

### 🔹 Replace & Modify
| Method | Kaam |
|--------|------|
| `replace()` | Word replace karo |
| `center()` | Center me rakho |
| `ljust()` | Left align |
| `rjust()` | Right align |
| `zfill()` | Zeros add karo |
| `expandtabs()` | Tab size set karo |

```python
"hello".replace("l", "r")  # "herro"
"hi".center(10, "*")       # "****hi****"
"hi".ljust(10, "-")        # "hi--------"
"hi".rjust(10, "-")        # "--------hi"
"42".zfill(5)              # "00042"
```

---

### 🔹 Encoding & Formatting
| Method | Kaam |
|--------|------|
| `encode()` | String ko bytes me |
| `format()` | String formatting |
| `format_map()` | Dict se format |
| `maketrans()` | Translation table |
| `translate()` | Characters replace |

```python
"Hello {0}".format("World")  # "Hello World"
table = str.maketrans("abc", "xyz")
"abc".translate(table)  # "xyz"
```

---

## 2️⃣ LIST METHODS

```python
my_list = [1, 2, 3]
```

| Method | Kaam | Example |
|--------|------|---------|
| `append()` | End me add | `[1,2].append(3)` → `[1,2,3]` |
| `insert()` | Position pe add | `[1,3].insert(1,2)` → `[1,2,3]` |
| `extend()` | List merge | `[1,2].extend([3,4])` → `[1,2,3,4]` |
| `remove()` | Value se delete | `[1,2,3].remove(2)` → `[1,3]` |
| `pop()` | Index se delete | `[1,2,3].pop(1)` → `[1,3]` |
| `clear()` | Sab delete | `[1,2,3].clear()` → `[]` |
| `index()` | Position dhundo | `[1,2,3].index(2)` → `1` |
| `count()` | Kitni baar aaya | `[1,2,2].count(2)` → `2` |
| `sort()` | Sort karo | `[3,1,2].sort()` → `[1,2,3]` |
| `reverse()` | Ulta karo | `[1,2,3].reverse()` → `[3,2,1]` |
| `copy()` | Copy banao | `[1,2,3].copy()` → `[1,2,3]` |

```python
fruits = ["banana", "apple", "cherry"]
fruits.append("mango")
fruits.sort()
print(fruits)  # ['apple', 'banana', 'cherry', 'mango']
```

---

## 3️⃣ TUPLE METHODS

Tuple me sirf **2 methods** hain:

| Method | Kaam | Example |
|--------|------|---------|
| `count()` | Kitni baar aaya | `(1,2,2).count(2)` → `2` |
| `index()` | Position dhundo | `(1,2,3).index(2)` → `1` |

```python
t = (1, 2, 3, 2, 2)
print(t.count(2))  # 3
print(t.index(3))  # 2
```

---

## 4️⃣ DICTIONARY METHODS

```python
d = {"name": "Ali", "age": 20}
```

| Method | Kaam | Example |
|--------|------|---------|
| `get()` | Value lo | `d.get("name")` → `"Ali"` |
| `keys()` | Sab keys | `d.keys()` |
| `values()` | Sab values | `d.values()` |
| `items()` | Key-Value pairs | `d.items()` |
| `update()` | Add/Update karo | `d.update({"city":"Delhi"})` |
| `pop()` | Key se delete | `d.pop("age")` |
| `popitem()` | Last item delete | `d.popitem()` |
| `clear()` | Sab delete | `d.clear()` |
| `copy()` | Copy banao | `d.copy()` |
| `setdefault()` | Default set karo | `d.setdefault("city","Delhi")` |
| `fromkeys()` | New dict banao | `dict.fromkeys(["a","b"], 0)` |

```python
student = {"name": "Ali", "age": 20}
print(student.get("name"))        # Ali
print(student.keys())             # dict_keys(['name', 'age'])
student.update({"city": "Delhi"})
print(student)  # {'name': 'Ali', 'age': 20, 'city': 'Delhi'}
```

---

## 5️⃣ SET METHODS

```python
s = {1, 2, 3}
```

| Method | Kaam |
|--------|------|
| `add()` | Element add karo |
| `remove()` | Element delete (error deta) |
| `discard()` | Element delete (no error) |
| `pop()` | Random delete |
| `clear()` | Sab delete |
| `copy()` | Copy banao |
| `union()` | Dono sets jodo |
| `intersection()` | Common elements |
| `difference()` | Fark dhundo |
| `symmetric_difference()` | Uncommon elements |
| `update()` | Merge karo |
| `intersection_update()` | Common rakh do |
| `difference_update()` | Fark rakh do |
| `symmetric_difference_update()` | Uncommon rakh do |
| `issubset()` | Subset hai? |
| `issuperset()` | Superset hai? |
| `isdisjoint()` | Koi common nahi? |

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))            # {1, 2, 3, 4, 5}
print(a.intersection(b))     # {3}
print(a.difference(b))       # {1, 2}
print(a.issubset(b))         # False
```

---

## 6️⃣ FILE METHODS

```python
f = open("file.txt", "r")
```

| Method | Kaam |
|--------|------|
| `read()` | Pura file padho |
| `readline()` | Ek line padho |
| `readlines()` | Sab lines list me |
| `write()` | Likho |
| `writelines()` | Multiple lines likho |
| `close()` | File band karo |
| `seek()` | Position set karo |
| `tell()` | Current position |
| `flush()` | Buffer clear |
| `readable()` | Read ho sakta? |
| `writable()` | Write ho sakta? |
| `seekable()` | Seek ho sakta? |
| `truncate()` | File chhota karo |

---

# 🎯 COMPLETE SUMMARY TABLE

| Data Type | Total Methods |
|-----------|--------------|
| **String** | ~47 methods |
| **List** | 11 methods |
| **Tuple** | 2 methods |
| **Dictionary** | 11 methods |
| **Set** | 17 methods |
| **File** | ~13 methods |

---

Kya aapko kisi specific method ka **detailed explanation with examples** chahiye? Bolo main explain kar deta hoon! 😊