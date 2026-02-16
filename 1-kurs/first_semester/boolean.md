# Python: Boolean va if/elif/else — sodda qo‘llanma

Bu qo‘llanma IT Foundation o‘quvchilari uchun Python’dagi Boolean (mantiqiy qiymatlar) va if/elif/else shart operatorlarini sodda, tushunarli misollar bilan tushuntiradi.

---

## 1) Boolean nima?

- Boolean — mantiqiy qiymat: faqat ikki xil bo‘ladi: `True` va `False`
- Eslatma: Harflar katta bilan yoziladi (`True`, `False`) — kichik (`true`, `false`) xato!

```python
is_student = True
has_paid = False

print(type(is_student))  # <class 'bool'>
```

### Truthy va Falsy
- Quyidagilar `False` (falsy) hisoblanadi: `0`, `0.0`, `""` (bo‘sh string), `[]`, `{}`, `set()`, `None`
- Boshqa hamma qiymatlar odatda `True` (truthy) hisoblanadi.

```python
print(bool(0))      # False
print(bool("hi"))   # True
print(bool([]))     # False
```

---

## 2) Taqqoslash operatorlari

- `==` teng
- `!=` teng emas
- `>` katta
- `<` kichik
- `>=` katta yoki teng
- `<=` kichik yoki teng

```python
a = 5
b = 7
print(a == b)  # False
print(a < b)   # True
print(a != b)  # True
```

Zanjirli taqqoslash (qulay):
```python
age = 22
print(18 <= age <= 30)  # True
```

---

## 3) Mantiqiy operatorlar: and, or, not

- `and` — ikkisi ham True bo‘lsa True
- `or` — kamida bittasi True bo‘lsa True
- `not` — qiymatni teskarisiga aylantiradi

```python
is_logged_in = True
has_access = False

print(is_logged_in and has_access)  # False
print(is_logged_in or has_access)   # True
print(not has_access)               # True
```

---

## 4) if / elif / else sintaksisi

Asosiy tuzilma:
```python
if shart:
    # agar shart True bo‘lsa shu joy ishlaydi
elif boshqa_shart:
    # agar birinchi shart False, bu True bo‘lsa ishlaydi
else:
    # yuqoridagilar False bo‘lsa ishlaydi
```

- Har bir satr oxirida `:` bo‘lishi shart.
- Ichkariga kirgan kod 4 ta bo‘sh joy (yoki 1 tab) bilan bo‘shliq (indentation) qilinadi.

Misol:
```python
harorat = 28

if harorat >= 30:
    print("Issiq!")
elif harorat >= 20:
    print("Yoqimli ob-havo")
else:
    print("Salqin")
```

---

## 5) Amaliy misollar

### a) Baholash (reyting)
```python
ball = 83

if ball >= 90:
    print("A")
elif ball >= 80:
    print("B")
elif ball >= 70:
    print("C")
elif ball >= 60:
    print("D")
else:
    print("F")
```

### b) Foydalanuvchi yoshi
```python
age = 16

if age < 13:
    print("Bola")
elif 13 <= age < 18:
    print("O‘smir")
else:
    print("Katta")
```

### c) Parol tekshirish
```python
password = "secret123"

if not password:
    print("Parol bo‘sh bo‘lmasin!")
elif len(password) < 8:
    print("Parol kamida 8 ta belgidan iborat bo‘lsin.")
else:
    print("Parol qabul qilindi.")
```

### d) Ro‘yxatda bor-yo‘qligini tekshirish
```python
students = ["Ali", "Laylo", "Bek"]
name = "Laylo"

if name in students:
    print("Topildi")
else:
    print("Topilmadi")
```

### e) Ichma-ich if o‘rniga and/or ishlatish
```python
age = 25
is_student = True

# Yomon usul (keraksiz ichma-ich)
if age >= 18:
    if is_student:
        print("Talaba uchun chegirma bor")

# Yaxshi usul
if age >= 18 and is_student:
    print("Talaba uchun chegirma bor")
```

---

## 6) Ternary (bitta satrda shartli qiymat)

```python
age = 20
status = "Balog‘atga yetgan" if age >= 18 else "Hali balog‘atga yetmagan"
print(status)
```

---

## 7) Tez-tez uchraydigan xatolar va yechimlar

- `=` va `==` ni adashtirmang:
  - `=` qiymat berish
  - `==` taqqoslash
- `True`/`False` katta harflar bilan yoziladi.
- `:` ni unutish xatosi ko‘p bo‘ladi.
- Indentation (ichki bo‘shliq) mos bo‘lishi kerak (odatda 4 bo‘sh joy).
- `input()` har doim `str` qaytaradi, raqam kerak bo‘lsa `int()` yoki `float()` qiling:
  ```python
  age = int(input("Yoshingiz: "))
  ```
- Oqimli sonlarni (float) solishtirishda ehtiyot bo‘ling:
  ```python
  a = 0.1 + 0.2  # 0.30000000000000004
  print(abs(a - 0.3) < 1e-9)  # True
  ```

---

## 8) Mini mashqlar

1) Berilgan son juftmi yoki toqmi?
- Kirish: `n = 17`
- Chiqish: `Toq`

2) Foydalanuvchi kiritgan parol bo‘sh emas va uzunligi kamida 8 bo‘lsin.
- Kirish: `password = "hello123"`
- Chiqish: `Parol kamida 8 ta belgidan iborat bo‘lsin.`

3) Haroratga qarab:
- `>= 30`: "Issiq"
- `20..29`: "Yoqimli"
- `< 20`: "Salqin"

4) Istalgan ism ro‘yxatda bormi?
- `names = ["Aziz", "Madina", "Javlon"]`, `qidir = "Javlon"`
- Chiqish: `Topildi`

5) Uchburchak tomonlari berilgan: `a, b, c`. Uchburchak bo‘lish sharti — har ikkitasining yig‘indisi uchinchisidan katta.
- Chiqish: "Uchburchak" yoki "Uchburchak emas"

6) Ball → harfli baho (A/B/C/D/F) ni chiqarish.

---

## 9) Mashqlar yechimlari (namuna)

```python
# 1) Juft/toq
n = 17
if n % 2 == 0:
    print("Juft")
else:
    print("Toq")
```

```python
# 2) Parol tekshirish
password = "hello123"
if not password:
    print("Parol bo‘sh bo‘lmasin!")
elif len(password) < 8:
    print("Parol kamida 8 ta belgidan iborat bo‘lsin.")
else:
    print("Parol qabul qilindi.")
```

```python
# 3) Harorat
t = 25
if t >= 30:
    print("Issiq")
elif t >= 20:
    print("Yoqimli")
else:
    print("Salqin")
```

```python
# 4) Ro‘yxatda bor-yo‘q
names = ["Aziz", "Madina", "Javlon"]
qidir = "Javlon"
if qidir in names:
    print("Topildi")
else:
    print("Topilmadi")
```

```python
# 5) Uchburchak sharti
a, b, c = 3, 4, 5
if a + b > c and a + c > b and b + c > a:
    print("Uchburchak")
else:
    print("Uchburchak emas")
```

```python
# 6) Ball -> harf
ball = 83
if ball >= 90:
    print("A")
elif ball >= 80:
    print("B")
elif ball >= 70:
    print("C")
elif ball >= 60:
    print("D")
else:
    print("F")
```

---

## 10) Qisqa “cheat sheet”

- Boolean: `True`, `False`
- Taqqoslash: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Mantiqiy: `and`, `or`, `not`
- Shartlar:
  ```python
  if shart:
      ...
  elif boshqa_shart:
      ...
  else:
      ...
  ```
- Ternary: `x if shart else y`
- Falsy: `0, 0.0, "", [], {}, set(), None`

Omad! Ko‘proq mashq qilsangiz, if/else va booleanlar juda oson bo‘lib qoladi.