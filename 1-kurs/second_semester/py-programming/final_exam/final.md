# 1-Bo'lim
#### 1–10-savollar 2 balldan, 11–15-savollar 3 balldan baholanadi.
## 1-savol  (2 ball)

```python
def qoshish(a, b):
    return a + b

print(qoshish(3, 4)) # 7
print(qoshish(10, -2)) # 8

# Qo'shish funksiyasi ikki sonni qabul qiladi va ularni qo'shib natijani qaytaradi.
# Misol uchun, qoshish(3, 4) chaqirilganda, u 3 va 4 ni qo'shadi
# va 7 ni qaytaradi.
# Shuningdek, qoshish(10, -2) chaqirilganda, u 10 va -2 ni qo'shadi
# va 8 ni qaytaradi.

# Функция сложения принимает два числа и возвращает результат их сложения.
# Например, при вызове qoshish(3, 4) она складывает 3 и 4
# и возвращает 7.
# Также при вызове qoshish(10, -2) она складывает 10 и -2
# и возвращает 8.

```

## 2-savol (2 ball)

```python
def salomlash(ism, xabar='Salom'):
    return f'{xabar}, {ism}!'

print(salomlash('Ali')) # Salom, Ali!
print(salomlash('Vali', 'Assalomu alaykum')) # Assalomu alaykum, Vali!

# salomlash funksiyasi ism va (ixtiyoriy) xabarni qabul qiladi
# va salomlashuv matnini qaytaradi. Agar xabar berilmasa, 
# standart qiymat 'Salom' bo'ladi. Misol uchun, salomlash('Ali')
# chaqirilganda 'Salom, Ali!' qaytaradi, salomlash('Vali', 'Assalomu alaykum')
# esa 'Assalomu alaykum, Vali!' qaytaradi.

# Функция salomlash принимает имя и (необязательное) сообщение
# и возвращает строку приветствия. Если сообщение не передано,
# используется значение по умолчанию 'Salom'. Например,
# salomlash('Ali') возвращает 'Salom, Ali!', а salomlash('Vali', 'Assalomu alaykum')
# возвращает 'Assalomu alaykum, Vali!'.
```

## 3-savol (2 ball)

```python
ikkilash = lambda x: x * 2
print(ikkilash(5)) # 10
print(ikkilash(0)) # 0

# ikkilash — lambda (anonim) funksiya bo'lib, bitta sonni qabul qiladi
# va uni 2 ga ko'paytirib natijani qaytaradi. Misol uchun,
# ikkilash(5) 10 ni, ikkilash(0) esa 0 ni qaytaradi.

# ikkilash — это лямбда (анонимная функция), которая принимает
# одно число и возвращает результат умножения на 2.
# Например, ikkilash(5) возвращает 10, а ikkilash(0) возвращает 0.
```

## 4-savol (2 ball)

```python
sonlar = [1, 2, 3, 4]
natija = list(map(lambda x: x ** 2, sonlar))
print(natija)  # [1, 4, 9, 16]

# Bu yerda `map()` funksiyasi ro'yxatdagi har bir elementga
# lambda funksiyani qo'llaydi. Lambda `x ** 2` har bir sonni
# kvadratga oshiradi va natijada [1, 4, 9, 16] ro'yxati hosil bo'ladi.

# Здесь функция `map()` применяет лямбда-функцию к каждому элементу
# списка. Лямбда `x ** 2` возводит каждое число в квадрат,
# и в результате получается список [1, 4, 9, 16].
```

## 5-savol (2 ball)

```python
sonlar = [1, 2, 3, 4, 5, 6]
juft = list(filter(lambda x: x % 2 == 0, sonlar))
print(juft)      # [2, 4, 6]
print(len(juft)) # 3

# Bu yerda `filter()` funksiyasi ro'yxatdagi elementlarni shart bo'yicha saralaydi.
# Lambda `x % 2 == 0` faqat juft sonlarni qoldiradi,
# natijada [2, 4, 6] chiqadi va ularning soni 3 bo'ladi.

# Здесь функция `filter()` отбирает элементы списка по условию.
# Лямбда `x % 2 == 0` оставляет только чётные числа, поэтому
# получается [2, 4, 6], а их количество равно 3.
```

## 6-savol (2 ball)

```python
try:
    x = int('abc')
except ValueError:
    print("Noto'g'ri son")

print('Tugadi')

# Bu yerda `int('abc')` son ko'rinishiga o'tmaydi, shuning uchun
# `ValueError` xatosi ushlanadi va "Noto'g'ri son" chiqadi.
# Keyin dastur davom etib, "Tugadi" ni chiqaradi.

# Здесь `int('abc')` нельзя преобразовать в число, поэтому
# возникает `ValueError`, и печатается "Noto'g'ri son".
# Затем программа продолжает работу и выводит "Tugadi".
```

## 7-savol (2 ball)

```python
def bolish(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Xato'

print(bolish(10, 2))  # 5.0
print(bolish(7, 0))   # Xato

# bolish funksiyasi a ni b ga bo'ladi. Agar b 0 bo'lsa,
# `ZeroDivisionError` xatosi yuz beradi va funksiya 'Xato' qaytaradi.

# Функция bolish делит a на b. Если b равно 0, возникает
# `ZeroDivisionError`, и функция возвращает строку 'Xato'.
```

## 8-savol (2 ball)

```python
try:
    natija = 10 / 2
    print(natija)  # 5.0
except ZeroDivisionError:
    print('Xato')
finally:
    print('Har doim ishlaydi')

# `try` blokida bo'lish bajariladi. Xato bo'lmasa natija chiqadi,
# xato bo'lsa `except` ishlaydi. `finally` esa har doim
# (xato bo'lsa ham bo'lmasa ham) bajariladi.

# В блоке `try` выполняется деление. Если ошибки нет — выводится результат,
# если ошибка есть — срабатывает `except`. Блок `finally` выполняется всегда.
```

## 9-savol (2 ball)

```python
matn = 'Men mushuk va mushuk sevaman'
yangi = matn.replace('mushuk', 'it')
print(yangi)  # Men it va it sevaman
print(matn.replace('Men', 'Siz', 1))  # Siz mushuk va mushuk sevaman

# `replace()` metodi matndagi so'zlarni almashtiradi. Birinchi holatda
# 'mushuk' so'zi hammasi 'it' ga almashadi. Ikkinchisida `1` berilgani
# uchun faqat birinchi 'Men' so'zi 'Siz' ga almashadi.

# Метод `replace()` заменяет слова в строке. В первом случае все вхождения
# 'mushuk' заменяются на 'it'. Во втором случае из-за параметра `1`
# заменяется только первое вхождение 'Men' на 'Siz'.
```

## 10-savol (2 ball)

```python
sozlar = ['salom', 'dunyo2', 'Python', '123']
for s in sozlar:
    print(s.isalpha())

# `isalpha()` metodi satr faqat harflardan iborat bo'lsa `True`,
# aks holda `False` qaytaradi. Shuning uchun: 'salom' -> True,
# 'dunyo2' -> False, 'Python' -> True, '123' -> False.

# Метод `isalpha()` возвращает `True`, если строка состоит
# только из букв, иначе `False`. Поэтому: 'salom' -> True,
# 'dunyo2' -> False, 'Python' -> True, '123' -> False.
```

## 11-savol (3 ball)

```python
sonlar = [1, 3, 5, 7, 8]
print(any(n % 2 == 0 for n in sonlar))  # True
print(any(n > 100 for n in sonlar))     # False

# `any()` funksiyasi ichidagi shartlardan hech bo'lmaganda bittasi
# `True` bo'lsa `True` qaytaradi. Bu yerda ro'yxatda juft son (8) borligi 
# uchun birinchi `any(...)` True bo'ladi. Ikkinchisida esa 100 dan
# katta son yo'q, shuning uchun False.

# Функция `any()` возвращает `True`, если хотя бы одно условие
# внутри даёт `True`. Здесь в списке есть чётное число (8),
# поэтому первый `any(...)` — True. Во втором случае чисел
# больше 100 нет, поэтому False.
```

## 12-savol (3 ball)

```python
sonlar = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in sonlar))  # True

sonlar2 = [2, 4, 5, 8]
print(all(n % 2 == 0 for n in sonlar2)) # False

# `all()` funksiyasi ichidagi hamma shartlar `True` bo'lsa
# `True` qaytaradi, aks holda `False`. Birinchi ro'yxatdagi
# hamma sonlar juft — True. Ikkinchisida 5 toq bo'lgani uchun — False.

# Функция `all()` возвращает `True`, только если все условия
# дают `True`, иначе `False`. В первом списке все числа
# чётные — True. Во втором есть нечётное число 5 — поэтому False.
```

## 13-savol (3 ball)

```python
s = 'Salom, Dunyo!'
tozalangan = s.replace(',', '').replace('!', '')
print(tozalangan)  # Salom Dunyo
print(tozalangan.replace(' ', '').isalpha())  # True

# Avval `replace()` yordamida vergul va undov belgisi olib tashlanadi.
# Keyin bo'sh joylar ham olib tashlanib, `isalpha()` bilan
# faqat harflardan iboratligi tekshiriladi.

# Сначала с помощью `replace()` удаляются запятая и восклицательный знак.
# Затем удаляются пробелы и с помощью `isalpha()` проверяется,
# что остались только буквы.
```

## 14-savol (3 ball)

```python
def xavfsiz_ildiz(n):
    try:
        if n < 0:
            raise ValueError('Manfiy son')
        return n ** 0.5
    except ValueError as e:
        return str(e)

print(xavfsiz_ildiz(9))   # 3.0
print(xavfsiz_ildiz(-4))  # Manfiy son

# Funksiya manfiy son uchun `ValueError` xatosini ataylab
# chiqaradi (`raise`). Xato `except` da ushlanib, xabar matn
# ko'rinishida qaytariladi. Musbat sonlarda esa kvadrat ildiz hisoblanadi.

# Для отрицательного числа функция специально вызывает ошибку
# `ValueError` (через `raise`). Ошибка перехватывается в `except`,
# и её сообщение возвращается как строка. Для положительных 
# чисел вычисляется квадратный корень.
```

## 15-savol (3 ball)

```python
sozlar = ['olma', 'ban4na', 'gilos', 'uzum2']
toza_mi = lambda s: all(c.isalpha() for c in s)

print(list(filter(toza_mi, sozlar)))      # ['olma', 'gilos']
print(any(toza_mi(s) for s in sozlar))    # True

# `toza_mi` lambda har bir so'zdagi barcha belgilar harf ekanini
# `all(...)` orqali tekshiradi. `filter()` faqat toza (faqat harfli)
# so'zlarni qoldiradi. `any(...)` esa ro'yxatda hech bo'lmaganda
# bitta toza so'z borligini tekshiradi.

# Лямбда `toza_mi` проверяет с помощью `all(...)`, что все символы
# в слове являются буквами. `filter()` оставляет только «чистые»
# слова (только буквы). `any(...)` проверяет, есть ли хотя бы
# одно такое слово в списке.
```

# 2-Bo'lim - Kod yozing
#### Har bir topshiriq talabini qanoatlantiradigan Python kodi yozing. Berilgan qatorlardan foydalaning.

## 1-savol  (5 ball)
### `count_vowels(matn)` nomli funksiya yozing. U satrni qabul qilib, undagi unli harflar (a, e, i, o, u — katta-kichik farqsiz) sonini qaytarsin. Funksiya ichida `any()` yoki `lambda` dan foydalaning.
### Misol: `count_vowels('Salom Dunyo')` → 4

```python
def count_vowels(matn):
    count = 0
    vowels = "aeoui"


    for ch in matn:
        if ch.lower() in vowels:
            count += 1 

    return count

counter = lambda matn: len([
    ch for ch in matn if ch.lower() in "aeoui"
])


print(count_vowels("Salom DunyO"))
print(counter("Salom DunyO"))

# count_vowels(matn) funksiyasi matndagi unli harflar sonini sanaydi (a, e, i, o, u).
# Bu yerda `ch.lower()` orqali harfni kichik qilib olib, unli harflar
# ro'yxatida bor-yo'qligini tekshiramiz.
# `counter` esa lambda yordamida unli harflarni ajratib, ularning
# sonini `len()` bilan topadi.

# Функция count_vowels(matn) считает количество гласных букв в строке (a, e, i, o, u).
# С помощью `ch.lower()` переводим символ в нижний регистр и
# проверяем, является ли он гласной.
# `counter` — это лямбда, которая собирает гласные и считает 
# их количество через `len()`.

```

## 2-savol  (5 ball)
### `safe_convert(qiymat)` nomli funksiya yozing. U `try/except` yordamida qiymatni butun songa o'tkazishga harakat qilsin. Agar o'tkazib bo'lmasa, `0` qaytarsin.
### Misol: `safe_convert('42')` → 42    |    `safe_convert('abc')` → 0

```python
def safe_convert(qiymat):
    try:
        return int(qiymat)
    except (ValueError, TypeError):
        return 0


print(safe_convert('42'))
print(safe_convert('abc'))

# safe_convert(qiymat) qiymatni `int()` orqali butun songa o'tkazadi.
# Agar qiymat son bo'lmasa (yoki noto'g'ri tur bo'lsa),
# xato ushlanadi va 0 qaytariladi.

# safe_convert(qiymat) пытается преобразовать значение
# в целое число через `int()`.
# Если значение нельзя преобразовать (или передан неверный тип),
# ошибка перехватывается и возвращается 0.
```

## 3-savol  (5 ball)
### `lambda` va `all()` yordamida quyidagi ro'yxatdan faqat barcha belgilari harf bo'lgan so'zlarni filtrlang. Natijani `toza_sozlar` o'zgaruvchisiga saqlang va chop eting.
### `sozlar = ['salom', 'py3on', 'dunyo', 'k0d', 'imtihon']`
### Kutilgan natija: `['salom', 'dunyo', 'imtihon']`

### 1) `filter()` ishlashiga sodda misol (final.py dagi example)

```python
toza_sonlar = list(filter(lambda i: i % 2 == 0, [1, 2, 3, 4]))
print(toza_sonlar)  # [2, 4]

# Batafsil (UZ):
# `filter(funksiya, iterable)` — 2 ta argument qabul qiladi:
#   1) funksiya (yoki lambda): har bir element uchun True/False qaytaradi
#   2) iterable: ro'yxat/tuple/str kabi elementlar ketma-ketligi
# `filter(...)` o'zi natijani ro'yxat qilib bermaydi, iterator
# qaytaradi, shuning uchun `list(...)` bilan ro'yxatga aylantirdik.
# Bu misolda lambda `i % 2 == 0` — son juft bo'lsa True, aks holda False.
# filter qanday ishlaydi:
#   i=1  -> 1%2==0 False -> tashlab yuboradi
#   i=2  -> 2%2==0 True  -> qoldiradi
#   i=3  -> 3%2==0 False -> tashlab yuboradi
#   i=4  -> 4%2==0 True  -> qoldiradi
# Natija: [2, 4]

# Подробно (RU):
# `filter(функция, iterable)` принимает 2 аргумента:
#   1) функция (или лямбда): для каждого элемента возвращает True/False
#   2) iterable: последовательность элементов (list/tuple/строка и т.д.)
# `filter(...)` возвращает итератор, поэтому мы оборачиваем
# в `list(...)`, чтобы получить список.
# В примере лямбда `i % 2 == 0` — True для чётных чисел, иначе False.
# Как работает filter:
#   i=1  -> False -> отбрасывает
#   i=2  -> True  -> оставляет
#   i=3  -> False -> отбрасывает
#   i=4  -> True  -> оставляет
# Результат: [2, 4]
```

### 2) Asosiy vazifa: so'zlarni filtrlash (lambda + `all()`)

```python
sozlar = ['salom', 'py3on', 'dunyo', 'k0d', 'imtihon']

toza_sozlar = list(filter(lambda soz: all(
    ch.isalpha() for ch in soz
), sozlar))

print(toza_sozlar)  # ['salom', 'dunyo', 'imtihon']

# `filter()` ro'yxatdagi elementlarni shart bo'yicha tanlab beradi.
# Bu yerda `all(ch.isalpha() for ch in soz)` — so'z ichidagi
# hamma belgilar harf bo'lsa True bo'ladi.
# Shuning uchun ichida raqam bor so'zlar ('py3on', 'k0d') tashlab yuboriladi.

# `filter()` отбирает элементы списка по условию.
# Здесь `all(ch.isalpha() for ch in soz)` возвращает True, только если
# все символы в слове — буквы.
# Поэтому слова с цифрами ('py3on', 'k0d') отфильтровываются.
```