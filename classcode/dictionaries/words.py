

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

def build_word_lists_by_index(words):
    d={}
    words = words.split()
    for i in range(0,len(words)-2):
        d.setdefault(words[i],[])
        d[words[i]].append(words[i+1])
    return d

def build_word_lists(words):
    d={}
    words = words.split()
    prev = words[0]
    for nextword in words[1:]:
        d.setdefault(prev,[])
        d[prev].append(nextword)
        prev = nextword
    return d

filename="/home/zamansky/gh/fall-2018-127/classcode/dictionaries/moby-small.txt"

f = open(filename)
s = f.read()
#words_uncleaned = build_word_counts(s)
#print(words_uncleaned)
#print("-------------------")
cleaned_string = clean_data(s)
#words = build_word_counts(cleaned_string)
#vals = words.values()
#vals = sorted(vals)
#print('------')
#common_words = []



filename="/home/zamansky/gh/fall-2018-127/classcode/dictionaries/moby-small.txt"

f = open(filename)
s = f.read()
s = clean_data(s)
wl = build_word_lists(s)
#words_uncleaned = build_word_counts(s)
#print(words_uncleaned)
#print("-------------------")
cleaned_string = clean_data(s)
words = build_word_counts(cleaned_string)
vals = words.values()
vals = sorted(vals)
#print('------')
#common_words = []
#for k in words:
#    if words[k] > 1000:
#        common_words.append([k,words[k]])

#common_words = [ [k,words[k]] for k in words if words[
#for k in words:
#    if words[k] > 1000:
#        common_words.append([k,words[k]])

#common_words = [ [k,words[k]] for k in words if words[k] > 50 ]

    
