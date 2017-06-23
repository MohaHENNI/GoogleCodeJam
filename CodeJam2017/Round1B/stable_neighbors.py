import sys


def minim_time(matrix, city, horses, horse=(0,0)):
    if city > 0:
        horse = (horse[0] - matrix[city-1][city], horse[1])
    
    if city == len(horses)-1:
        return 0.0
    if horse[0] < matrix[city][city+1]:
        return minim_time(matrix, city+1, horses, horses[city]) + matrix[city][city+1]/horses[city][1]
    elif horse[0] <= horses[city][0] and horse[1] <= horses[city][1]:
        return minim_time(matrix, city+1, horses, horses[city]) + matrix[city][city+1]/horses[city][1]
    else:
    
        #switch horse
        time1 = minim_time(matrix, city+1, horses, horses[city]) + matrix[city][city+1]/horses[city][1]
        #don't switch horse
        time2 = minim_time(matrix, city+1, horses, horse) + matrix[city][city+1]/horse[1]

        return min(time1, time2) 
               
                


f = open(sys.argv[1])

T = int(f.readline().strip())

for i in range(1, T+1):
    N, Q = f.readline().strip().split()
    N, Q = (int(N), int(Q))
    
    horses = []
    for j in range(N):
        Ei, Si = f.readline().strip().split()
        Ei, Si = (int(Ei), int(Si))
        horses.append((Ei,Si))
    matrix = []
    for j in range(N):
        line = f.readline().strip().split()
        line = [int(n) for n in line]
        matrix.append(line)

    destinations =[]
    for j in range(Q):
        Uj, Vj = f.readline().strip().split()
        Uj, Vj = (int(Uj), int(Vj))
        destinations.append((Uj, Vj))
    
        

    result = minim_time(matrix, 0, horses)

    print("Case #{0}: {1}".format(i, result))

f.close()