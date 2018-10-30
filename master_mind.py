'''
[B G Y G]
[R B R G]

Hits = 1
Pseudo Hits = 1
'''

def find_hits_pseudohits(secret, guess):
    if len(secret) != len(guess):
        print "The lenghts of secret and guess are not equal"
        return
    if secret is None or guess is None:
        print "Either secret or guess is None"
        return

    length = len(secret)

    hits = 0
    phits = 0
    visited = set()
    for i in range(0, length):
        if secret[i] == guess[i]:
            hits += 1
            continue
        else: 
            if guess[i] in visited:
                phits+=1
                visited.remove(guess[i])

        visited.add(secret[i])

    print 'Hits : ', hits
    print 'Pseudo hits :', phits
