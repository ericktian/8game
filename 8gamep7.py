#import sys
import time
import random
# #make root as string
# root = sys.argv[1]
# if(len(root)==8):
#     root = (root, "_")
# elif(len(root)<8):
#     root = (root, "_", sys.argv[2])
# root = ''.join(root)
def run(root):
    #create parseMe queue, dictionary dictAlreadySeen, list lookup, boolean endloop, list path, int counter
    parseMe = [root]
    dictAlreadySeen = {root:""}
    lookup = [[1,3], [0,2,4], [1,5], [0,4,6], [1,3,5,7], [2,5,8], [3,7], [4,6,8], [5,7]]
    keeplooping = True
    path = []
    counter = 1

    #iterate
    start = time.time()
    if(root=='12345678_'):
        print('----------')
        print(root[0], ' ', root[1], ' ', root[2])
        print(root[3], ' ', root[4], ' ', root[5])
        print(root[6], ' ', root[7], ' ', root[8])
        print('----------')
        print('Steps taken: 0')
    else:
        while keeplooping and len(parseMe) > 0:
            node = parseMe.pop(0)
            gapindex = node.index('_')
            for i in range(0, len(lookup[gapindex])):
                t = list(node)
                t[gapindex], t[lookup[gapindex][i]] = t[lookup[gapindex][i]], t[gapindex]
                newnode = ''.join(t)
                if newnode not in dictAlreadySeen:
                    parseMe.append(newnode)
                    dictAlreadySeen[newnode] = node
                    if(newnode == '12345678_'):
                        pathlocation = newnode
                        path.insert(0, pathlocation)
                        while(dictAlreadySeen[pathlocation] != root):
                            path.insert(0, dictAlreadySeen[pathlocation])
                            pathlocation = dictAlreadySeen[pathlocation]
                            counter += 1
                        keeplooping = False
        #if(len(parseMe)==0): print("No possible solution")
        #else: print("Steps taken: ", len(path))
    end = time.time()
    return [end-start, len(path)]
sum = 0
sumpath = 0
numpaths = 0
for i in range(0, 1000):
    randomroot = ""
    for x in range(0, 9):
        rand = 0
        while str(rand) in randomroot:
            rand = random.randint(0, 8)
        randomroot = randomroot + str(rand)
    # print(randomroot)
    # randomroot.replace("9", "_")
    # print(randomroot)
    # print(sum)
    #print(randomroot.replace("9", "_"))
    ret = run(randomroot.replace("0", "_"))
    sum += ret[0]
    if(ret[1]!= 0):
        sumpath += ret[1]
        numpaths += 1
print(" Average sum: ", sum/1000, "\n", "Average steps of solvable puzzles: ", sumpath/numpaths, "Number of solvable puzzles: ", numpaths)