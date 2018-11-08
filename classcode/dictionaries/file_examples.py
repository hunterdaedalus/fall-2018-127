

def build_word_counts(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d



#s = "one two three four five four six three seven three two three eight nine"
#d=build_word_counts(s)
#print(d)

# you should only need filename="macbeth.txt"
filename="/home/zamansky/gh/fall-2018-127/classcode/dictionaries/macbeth.txt"
f = open(filename)
# we can read the whole thing
s = f.read()
print(s)
f.close()
print("-------")
# or we can read a line at a time.
f = open(filename)
s = f.readline()
print(s)
s = f.readline()
print(s)
f.close()
print('------')
f = open(filename)
for line in f.readlines():
    print(line)


