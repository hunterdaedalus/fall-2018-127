import random
names=['lisa','bart','marge','homer','maggie','barney','moe','carl','smithers']


def generate_votes(name,number_votes):
    votes=[]
    for i in range(number_votes):
        votes.append(random.choice(names))
    return votes

def winner(names,votes):
    tallies = {}
    for n in names:
        tallies[n]=0
    print(tallies)

    for vote in votes:
        tallies[vote] = tallies[vote]+1

    max_vote_count = max(tallies.values())
    print(tallies)
    print(max_vote_count)

    winners=[]
    for k,v in tallies.items():
        if v == max_vote_count:
            winners.append(k)
    print(winners)
votes = generate_votes(names,30)   
winner(names,votes)
