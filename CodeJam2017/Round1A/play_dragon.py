import sys


def play_turns(C, Ad, Hd, Ak, Hk, B, D):

    if Hd < 0:
        return 10000000000000000 #lose
    #Win
    if Ad - Hk >= 0:
        return 0
    
    if Hd - Ak <= 0:
        #Cure or Debuff
        if (Ak - D) - Hd >= 0:
            #Cure
            if C - Ak <= Hd: #lost
                return False
            Hd = C
            Hd -= Ak
            n = play_turns(C, Ad, Hd, Ak, Hk, B, D)
            if n >= 0:
                return n + 1
            else:
                return -1
        else:
            #Cure or debuff
            cure = play_turns(C, Ad, C - Ak, Ak, Hk,B, D)
            #Debuff
            if D > 0:
                debuf = play_turns(C, Ad, Hd - Ak+D, Ak-D, Hk, B, D)
                return 1 + min(cure, debuf)
            else:
                return 1 + cure

    # try debuf
    if D > 0:
        debuf = play_turns(C, Ad, Hd - Ak + D, Ak-D, Hk, B, D)
    else:
        debuf = 10000000000000000

    #Try Attack
    attack = play_turns(C, Ad, Hd-Ak, Ak, Hk -Ad, B, D)
    #Try Buff
    if B > 0:
        buf = play_turns(C, Ad+B, Hd-Ak, Ak, Hk, B, D)
    else:
        buf = 10000000000000000
    
    return 1 + min(buf, attack, debuf)



f = open(sys.argv[1])
T = int(f.readline())

for i in range(T):
    Hd, Ad, Hk, Ak, B, D = f.readline().strip().split()

    Hd, Ad, Hk, Ak, B, D = (int(Hd), int(Ad), int(Hk), int(Ak), int(B), int(D))
    
    result = play_turns(Hd, Ad, Hd, Ak, Hk, B, D)

    if result > -1:
        print("Case #{0}: {1}".format(i+1, result))
    else:
        print("Case #{0}: IMPOSSIBLE".format(i+1))

f.close()