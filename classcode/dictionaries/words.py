

def build_word_counts(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d



s = "one two three four five four six three seven three two three eight nine"
d=build_word_counts(s)
print(d)
