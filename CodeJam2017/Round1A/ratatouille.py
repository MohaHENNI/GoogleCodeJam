import sys

def num_kits(required_amount, packages):
    result = []

    for i in range(len(packages)):
        line = []
        for j in range(len(packages[i])):
            num = packages[i][j] // required_amount[i]
            element = []
            k= 0
            while  0.9 * (num+k)* required_amount[i] <= packages[i][j] <= 1.1 * (num+k) * required_amount[i]:
                element.append(num+k)
                k += 1
            k = 1
            while 0.9 * (num-k) * required_amount[i] <= packages[i][j] <= 1.1 * (num-k) *required_amount[i]:
                element.append(num-k)
                k += 1

            line.append(element)

        result.append(line)

    count = 0
    for i in range (len(line)):
        for j in range(1, len(packages)):
            for k in range(len(line)):
                if set(result[j][k]).intersection(set(result[0][i])) != set():
                    count += 1
                    result[j][k] = set()
                    break
    
    return count

f = open(sys.argv[1])
T = int(f.readline())

for i in range(T):
    N, P = f.readline().strip().split()
    N, P = (int(N), int(P))
    required_amount = f.readline().strip().split()

    for j in range(len(required_amount)):
        required_amount[j] = int(required_amount[j])

    matrix  = []
    for j in range(N):
        row = f.readline().strip().split()
        for k in range(P):
            row[k] = int(row[k])

        matrix.append(row)    

    result = num_kits(required_amount, matrix)
    if result > -1:
        print("Case #{0}: {1}".format(i+1, result))
    else:
        print("Case #{0}: IMPOSSIBLE".format(i+1))

f.close()