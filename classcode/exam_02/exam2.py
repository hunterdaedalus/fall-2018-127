
def make_acronym(line):
    result = ""
    for word in line.split():
        result = result + word[0]
    return result

def rle1(line):
    encoded = []
    i = 0
    while i < len(line)-1:
        next_letter = i+1
        while next_letter < len(line) and line[next_letter] == line[i]:
            next_letter = next_letter + 1
        encoded.append([ next_letter - i,line[i]])
        i = next_letter
    if i == len(line)-1:
        encoded.append( [1, line[i]])
    return encoded

def rle2(line):
    encoded = []
    count = 1
    prevchar = line[0]
    for c in line[1:]:
        if c==prevchar:
            count = count + 1
        else:
            encoded.append([count,prevchar])
            count = 1
            prevchar = c
    encoded.append([count,prevchar])
    return encoded

def decode(encoded):
    result = ""
    for item in encoded:
        result = result + item[0] * item[1]
    return result

composite_scores = {('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T') :     1 ,
                    ('D', 'G')                         :     2 ,
                    ('B', 'C', 'M', 'P')                   :     3 ,
                    ('F', 'H', 'V', 'W', 'Y')                :     4 ,
                    ('K')                           :     5 ,
                    ('J','X')                         :     8 ,
                    ('Q', 'Z')                         :    10}



def score1(word,scores):
    score = 0
    for letter in word:
        for k in scores:
            if letter in k:
                score = score + scores[k]
    return score
                
def score2(word,scores_raw):
    scores = {}
    for k in scores_raw:
        for letter in k:
            scores[letter] = scores_raw[k]
    score = 0
    for letter in word:
        score = score + scores[letter]
    return score
    
