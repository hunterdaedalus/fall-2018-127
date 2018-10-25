

def compress_word(word):
    vowels="aeiouAEIOU"
    if len(word)==0:
        return ""
    first = word[0]
    rest = word[1:]
    new_rest=""
    for letter in rest:
        if letter not in vowels:
            new_rest = new_rest + letter

    return first + new_rest

def compress_sentence(sentence):
    result = []
    for word in sentence.split():
        result.append(compress_word(word))
    return " ".join(result)

print("Testing compress_word")

print('apple',compress_word("apple"))
print("I",compress_word("I"))
print("struggle",compress_word("struggle"))
print("UPPER",compress_word("UPPER"))
print("EMPTY STRING",compress_word(""))

print("Testing compress_sentence")
s = "When shall we three meet again in thunder lightening or rain"
print(s)
print(compress_sentence(s))
