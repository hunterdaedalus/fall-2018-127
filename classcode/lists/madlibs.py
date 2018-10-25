import random

NOUNS=["dog","boy","girl","hammer","frog","boat"]
VERBS=['ate','slept','walked','bludgeoned']


s="<NOUN> <VERB> the <NOUN> with an enthusiasm unknown to mankind."

def madlibify(sentence,nouns,verbs):
    result=[]
    for word in sentence.split():
        if word == '<NOUN>':
            result.append(random.choice(nouns))
        elif word == '<VERB>':
            result.append(random.choice(verbs))
        else:
            result.append(word)
    return " ".join(result)


madlibify(s,NOUNS,VERBS)
