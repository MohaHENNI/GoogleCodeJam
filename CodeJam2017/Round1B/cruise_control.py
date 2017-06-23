import sys


def speed(D, speed_distance):
    times = []

    for i in range(len(speed_distance)):
        Di, S = speed_distance[i]

        times.append((D-Di)/S)

    slowest = max(times)

    _speed = D/slowest

    return _speed





f = open(sys.argv[1])

T = int(f.readline().strip())

for i in range(1, T+1):
    D, N = f.readline().strip().split()
    D, N = (int(D), int(N))
    speed_distance = []
    for j in range(N):
        Di, S = f.readline().strip().split()
        Di, S = (int(Di), int(S))
        speed_distance.append((Di, S))

    result = speed(D, speed_distance)

    print("Case #{0}: {1}".format(i, result))

f.close()