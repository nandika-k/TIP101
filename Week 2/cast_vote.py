def cast_vote (votes, candidate):
    #vote_dict = {}

    if candidate not in votes:
        votes[candidate] = 1
    else:
        votes[candidate] += 1
    return votes

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)