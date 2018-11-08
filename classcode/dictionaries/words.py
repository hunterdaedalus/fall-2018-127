

def build_word_counts(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d

def clean_data(s):
    result=""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result = result + letter.lower()
        else:
            result = result + " "
    return result

filename="/home/zamansky/gh/fall-2018-127/classcode/dictionaries/macbeth.txt"
f = open(filename)
s = f.read()
words_uncleaned = build_word_counts(s)
print(words_uncleaned)
cleaned_string = clean_data(s)
print("-------------------")
words = build_word_counts(cleaned_string)
print(words)
