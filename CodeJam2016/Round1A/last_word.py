import sys

def last_word(S):
    word = S[0]
    for letter in S[1:]:
        if word[0] > letter:
            word = word + letter
        else:
            word = letter + word
    
    return word
        


f = open(sys.argv[1])
T = int(f.readline())

for i in range(T):
    S = f.readline().strip()
    result = last_word(S)

    print("Case #{0}: {1}".format(i+1, result))
    

f.close()
