sozlar = ["olma", "apelsin", "banan"]

result = {}

for word in sozlar:
    words = result.get(word[-1], [])
    words.append(word)
    result[word[-1]] = words

print(result)