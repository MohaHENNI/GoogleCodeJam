import sys

def split_cake(cake):
    
    for i in range(len(cake)):
        for j in range(len(cake[i])):
            if cake[i][j] == '?':
                k = 0
                l = 0
                while k < len(cake[i]) and cake[i][k] == '?':
                    k+= 1
                if k < len(cake[i]):
                    cake[i][j] = cake[i][k]
                else:
                    while l < len(cake) and cake[l][j] == '?':
                        l += 1
                    if l < len(cake):
                        cake[i][j] = cake[l][j]
                    else:
                        n, m = (l, k)
                        while l < len(cake) and k < len(cake[i]) and cake[l][k] == '?':
                            k += 1
                            while k < len(cake[i]) and cake[l][k] == '?':
                                k += 1
                            if k < len(cake[i]):
                                cake[i][j] = cake[l][k]
                            else:
                                l += 1
                                k = m
    return cake   
        
        





f = open(sys.argv[1])
T = int(f.readline())

for i in range(T):
    R, C = f.readline().strip().split()
    R, C = (int(R), int(C))
    result = []
    for i in range(R):
        row = f.readline().strip().split()
        result.append([c for c in row])
    
        
    result = split_cake(result)

    print("Case #{0}:".format(i+1))
    for row in result:
        str_row = ""
        for c in row:
            str_row += c
        print(str_row)

f.close()