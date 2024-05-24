def Gale_Shapley(prefer_list):

    freeMan = list()
    freeWoman = list()
    tempMatch = dict()
    stableMatch = dict()

    n = len(prefer_list) // 2

    for i in range(n):
        
        #initialize TempMatch
        tempMatch[2*i+1] = 0
        tempMatch[2*i+2] = 0
        
        #odd integers as the man
        freeMan.append(2*i+1)
        #even integers as the woman 
        freeWoman.append(2*i+2)

    count = 0

    while len(freeMan):
        
        man = freeMan[0]
        unmatched_women_index = 0

        if man in stableMatch:
            
            prefer_women_list = prefer_list[man - 1]
            unmatched_women_index = prefer_women_list.index(stableMatch[man]) + 1

        for woman in prefer_list[man - 1][unmatched_women_index:n]:
            
            count += 1
            
            if  tempMatch[woman] == 0:
                tempMatch[man] = woman
                tempMatch[woman] = man
                freeMan.remove(man)
                stableMatch[man] = woman
                break

            else:
                if prefer_list[woman - 1].index(man) < prefer_list[woman - 1].index(tempMatch[woman]):

                    freeMan.remove(man)
                    freeMan.append(tempMatch[woman])
                    tempMatch[tempMatch[woman]] = 0
                    tempMatch[woman] = man
                    tempMatch[man] = woman
                    stableMatch[man] = woman
                    break
    
    return  stableMatch
 
if __name__ == "__main__":

    import sys

    prefer_list = []
    i = 0

    # for line in open(sys.argv[1], 'r'):
    for line in sys.stdin:

        if i < 4:
            i += 1
        else:
            line = line.strip().split(" ")
            line.pop(0)
            newline = [int(x) for x in line]
            prefer_list.append(newline)

    for m, w in (Gale_Shapley(prefer_list)).items():
        print(m,w)