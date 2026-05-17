# ```````````````````````````````````````````````````````````
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
# ````````````````````````````````````````````````````````````
def safe_convert(qiymat):
    try:
        return int(qiymat)
    except:
        return 0


print(safe_convert("11"))
print(safe_convert("abc"))
# ```````````````````````````````````````````````````````````
toza_sozlar = list(filter(lambda i: i % 2 == 0,[1, 2,3,4]))
print(toza_sozlar)

# ----------------------------------------------------------

sozlar = ['salom1', 'py3on', 'dunyo', 'k0d', 'imtihon']

toza_sozlar = list(filter(lambda soz: all(
  ch.isalpha() for ch in soz
), sozlar))

# salom
## s -> True
## a -> True
## l -> True
## o -> True
## m -> True
## 1 -> False
## [T,T,T,T,T,F]


print(toza_sozlar)

# ``````````````````````````````````````````````````````````



