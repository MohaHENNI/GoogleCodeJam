import sys

def minimum(first, second):
    min1 = len(set(first))
    min2 = len(set(second))

    return len(first) - max(min1, min2)













f = open(sys.argv[1])
T = int(f.readline())

for i in range(T):
    N = int(f.readline().strip())
    first, second = ([], [])

    for j in range(N):
        fi, s = f.readline().strip().split()
        first.append(fi)
        second.append(s)
    result = minimum(first, second)

    print("Case #{0}: {1}".format(i+1, result))
    

f.close()