
def digits(N):
    digs = []
    if N == 0:
        return [0]
    while N > 0:
        digs += [N%10]
        N = N//10
    return digs

def lastNum(N):
    if N == 0:
        return "INSOMNIA"
    else:
        i = 2
        digs = digits(N)
        while len(digs) < 10:
            digs += digits(N*i)
            digs = list(set(digs))
            i += 1

        return (i-1)*N


f = open("A-large-practice.in")
count = 0
T = int(f.readline())

for i in range(1, T+1):
    N = int(f.readline())
    print("Case #{0}: ".format(i) + str(lastNum(N)))
