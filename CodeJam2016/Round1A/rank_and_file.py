import sys
import numpy as np

class specialList(object):
    def __init__(self, l):
        self.l = l
    def __str__(self):
        result = ""
        for num in self.l:
            result = result + " " + str(num)
        return result

def missing_paper(papers):
    pep = []
    for line in papers:
        for num in line:
            pep.append(num)
    papers = pep
    elements = set(papers)
    missing = []
    for element in elements:
        if papers.count(element) % 2 != 0:
            missing.append(element)
    
    return sorted(missing)


f = open(sys.argv[1])
T = int(f.readline())

for i in range(T):
    N = int(f.readline().strip())
    papers = []
    for j in range(2*N-1):
        line = f.readline().strip().split()
        papers.append([int(elem) for elem in line])

    result = specialList(missing_paper(papers))

    print("Case #{0}: {1}".format(i+1, result))
    

f.close()
   