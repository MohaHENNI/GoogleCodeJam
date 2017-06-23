import sys 

def extract(number, S):

    for letter in number:
       #extract the letter
        S1, S2 = S.split(letter, 1)
        S = S1 + S2
        
    return S

def extract_obvious(S):

    phone_number = []

    #extract zeros
    num = S.count("Z")
    for i in range(num):
        S = extract("ZERO", S)
        phone_number.append(0)
    
    #extract twos
    num = S.count("W")
    for i in range(num):
        S = extract("TWO", S)
        phone_number.append(2)
    
    #extract fours
    num = S.count("U")
    for i in range(num):
        S = extract("FOUR", S)
        phone_number.append(4)

    #extract sixes
    num = S.count("X")
    for i in range(num):
        S = extract("SIX", S)
        phone_number.append(6) 
    
    #extract eights
    num = S.count("G")
    for i in range(num):
        S = extract("EIGHT", S)
        phone_number.append(8)

    #extract threes
    num = S.count("H")
    for i in range(num):
        S = extract("THREE", S)
        phone_number.append(3)

    #extract sevens
    num = S.count("S")
    for i in range(num):
        S = extract("SEVEN", S)
        phone_number.append(7)
    
    #extract fives
    num = S.count("V")
    for i in range(num):
        S = extract("FIVE", S)
        phone_number.append(5)

    #extract nines
    num = S.count("I")
    for i in range(num):
        S = extract("NINE", S)
        phone_number.append(9)

    #extract ones
    num = S.count("O")
    for i in range(num):
        S = extract("ONE", S)
        phone_number.append(1)

    phone_number = sorted(phone_number)
    result = ""
    for i in range(len(phone_number)):
        result += str(phone_number[i])

    return result

f = open(sys.argv[1])
T = int(f.readline())

for i in range(T):
    S = f.readline().strip()

    result = extract_obvious(S)

    print("Case #{0}: {1}".format(i+1, result))
    

f.close()
   



















