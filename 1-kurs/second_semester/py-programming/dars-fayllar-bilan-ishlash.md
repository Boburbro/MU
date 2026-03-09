# Python'da Fayllar bilan Ishlash (File Management)

Ushbu darsda Python yordamida fayllarni ochish, o'qish, ularga ma'lumot yozish va fayllarni to'g'ri yopish usullarini o'rganamiz.

---

## 1. Faylni ochish rejimlari (File Modes)

Fayl bilan ishlash uchun avvalo uni kerakli rejimda ochib olishimiz kerak. Python-da quyidagi asosiy rejimlardan foydalaniladi (odatiy holatda `r` rejimi ishlaydi):

*   **`r` - Read (O'qish)**
    *   Faylni faqat o'qish uchun ochadi.
    *   **Qoida:** Agar fayl mavjud bo'lmasa, dastur xato (error) beradi.
*   **`w` - Write (Yozish)**
    *   Faylga ma'lumot yozish uchun ochadi.
    *   **Qoida:** Agar fayl mavjud bo'lsa, uning ichidagi eski ma'lumotlarni to'liq o'chirib, o'rniga yangisini yozadi. Agar fayl yo'q bo'lsa, yangi fayl yaratadi.
*   **`a` - Append (Qo'shish)**
    *   Faylning oxiriga yangi ma'lumot qo'shish uchun ochadi.
    *   **Qoida:** Qadimgi ma'lumotlar saqlanib qoladi. Agar fayl yo'q bo'lsa, yangisini yaratadi.
*   **`x` - Create (Yaratish)**
    *   Faqat yangi fayl yaratish uchun ishlatiladi.
    *   **Qoida:** Agar bunday nomli fayl oldindan mavjud bo'lsa, dastur xato (error) beradi.

---

## 2. Fayl ustida amallar (Metodlar)

Fayl obyekti yaratilgandan so'ng, u bilan turli amallarni bajarish mumkin:

*   **`file.read()`**
    *   Faylning barcha tarkibini bitta matn (string) ko'rinishida o'qib oladi.
*   **`file.readline()`**
    *   Fayldan faqatgina bitta qatorni o'qiydi. Har safar chaqirilganda keyingi qatorga o'tib ketadi.
*   **`file.write(text)`**
    *   Fayl ichiga ko'rsatilgan matnni yozadi.
*   **`file.close()`**
    *   Fayl bilan ishlab bo'lingach, xotirani bo'shatish va faylni tizimda yopish uchun ishlatiladi. Bu juda muhim qadam!

---

## 3. Avtomatik yopish: `with open(...)` 

Fayllar bilan ishlashda doim ham `close()` metodini yozishni esdan chiqarib qo'yishimiz mumkin. Bunga yo'l qo'ymaslik uchun `with` maxsus so'zidan foydalanish tavsiya etiladi.

```python
with open("fayl.txt", "r") as file:
    malumot = file.read()
    print(malumot)
# Kod bloki tugagandan so'ng (xatboshidan qaytganda), 
# fayl avtomatik ravishda yopiladi. file.close() yozish shart emas!
```

---

## 📚 Amaliy Masalalar (O'quvchilar uchun)

Quyidagi masalalarni o'tilgan mavzudan foydalanib Python-da dasturini tuzing:

**1-masala:**  
`"talabalar.txt"` nomli faylni yaratish rejimida (`x` yoki `w` bilan) oching va ichiga 3 ta do'stingizning ismini yozing.  
*(Yordam: Har bir ism yangi qatorda bo'lishi uchun yozuv oxiriga `\n` qo'shib yozing).*

**2-masala:**  
Birinchi masalada yaratilgan `"talabalar.txt"` faylini o'qish rejimida (`r`) oching. Faylning barcha tarkibini `read()` metodi yordamida o'qib, ekranga (konsolga) chiqaring. Shundan so'ng darhol faylni o'zingiz yoping.

**3-masala:**  
`"talabalar.txt"` faylini shunday ochingki, undagi eski ismlar o'chib ketmasin. Uning oxiriga yana ikkita yangi ism qo'shing (buning uchun `a` rejimidan foydalaning).

**4-masala:**  
`with open(...)` operatoridan foydalanib, `"talabalar.txt"` faylini o'qish uchun oching. Fayldagi barcha yozuvlarni birdaniga o'qimang. `readline()` metodini ikki marta chaqirish orqali faqat dastlabki 2 ta qatorni (birinchi 2 ta ismni) ekranga chiqaring. 

**5-masala:**  
Kodni shunday yozing: avval `"xabar.txt"` fayli bor-yo'qligini tekshirish ma'nosida `"x"` (yaratish) rejimida ochib unga "Salom" deb yozmoqchi bo'ling. Agar shu fayl oldindan yaratilgan bo'lsa (ya'ni dasturingiz xato - Error bersa), xatoni "try..except" yordamida ushlab qoling va dastur qulamay, foydalanuvchiga *"Bu fayl allaqachon mavjud"* degan xabarni chiqarsin. Agar mavjud bo'lmasa, uni bemalol yaratsin.
