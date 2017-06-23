
def flip(plate, index):

    i = 0
    flips = 0
    while plate[i] == '+':
        i+=1
    if i > 0:
        #First flip
        flips += 1
        plate = '-'*i + plate[i:]
    #second flip
    flips += 1

    plate = plate[index::-1].replace('-', '*').replace('+', '-').replace('*', '+') + plate[index:]


    return (plate, flips)




f = open("B-large-practice.in")

T = int(f.readline())

for i in range(1, T+1):
    plate = f.readline()
    #plate = "--+-"
    flips = 0
    for j in range(len(plate)-1, -1, -1):

        if plate[j] == '-':
            (plate, numFlips) = flip(plate, j)
            flips += numFlips


    print("Case #{0}: ".format(i) + str(flips))
