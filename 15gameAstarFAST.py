import sys
import time
#make root as string
import queue as Q #q = Q.PriorityQueue()
root = sys.argv[1]
if(len(root)==15):
    root = (root, "_")
elif(len(root)<15):
    root = (root, "_", sys.argv[2])
root = ''.join(root)
#root = 'EKJ_IONDCBHLGMAF'

SOLVEDSTATE = 'ABCDEFGHIJKLMNO_'

#print(root)
lookup = [[1,4], [0,2,5], [1,3,6], [2,7], [0,5,8], [1,4,6,9], [2,5,7,10], [3,6,11], [4,9,12], [5,8,10,13], [6,9,11,14],
     	[7,10,15], [8,13], [9,12,14], [10,13,15], [11,14]]
def toABC(myStr):
    liststring = list(myStr)
    for i in range(0, len(liststring)):
        if liststring[i] == '1': liststring[i] = 'A'
        if liststring[i] == '2': liststring[i] = 'B'
        if liststring[i] == '3': liststring[i] = 'C'
        if liststring[i] == '4': liststring[i] = 'D'
        if liststring[i] == '5': liststring[i] = 'E'
        if liststring[i] == '6': liststring[i] = 'F'
        if liststring[i] == '7': liststring[i] = 'G'
        if liststring[i] == '8': liststring[i] = 'H'
        if liststring[i] == '9': liststring[i] = 'I'
        if liststring[i] == 'A': liststring[i] = 'J'
        if liststring[i] == 'B': liststring[i] = 'K'
        if liststring[i] == 'C': liststring[i] = 'L'
        if liststring[i] == 'D': liststring[i] = 'M'
        if liststring[i] == 'E': liststring[i] = 'N'
        if liststring[i] == 'F': liststring[i] = 'O'
    return ''.join(liststring)

if '1' in root:
   root = toABC(root)

table = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3],
    	[2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]

def toNum(temp):
    liststring = list(temp)
    for i in range(0, len(liststring)):
        if liststring[i] == 'A': liststring[i] = 1
        if liststring[i] == 'B': liststring[i] = 2
        if liststring[i] == 'C': liststring[i] = 3
        if liststring[i] == 'D': liststring[i] = 4
        if liststring[i] == 'E': liststring[i] = 5
        if liststring[i] == 'F': liststring[i] = 6
        if liststring[i] == 'G': liststring[i] = 7
        if liststring[i] == 'H': liststring[i] = 8
        if liststring[i] == 'I': liststring[i] = 9
        if liststring[i] == 'J': liststring[i] = 10
        if liststring[i] == 'K': liststring[i] = 11
        if liststring[i] == 'L': liststring[i] = 12
        if liststring[i] == 'M': liststring[i] = 13
        if liststring[i] == 'N': liststring[i] = 14
        if liststring[i] == 'O': liststring[i] = 15
        if liststring[i] == '_': liststring[i] = 16
    return liststring
#manhattan distance/
def manhattan(list1):
    sum = 0
    list1 = toNum(list1)
    for i in range(0, len(list1)):
        if list1[i] != 16:
            sum += abs(table[i][0]-table[list1[i]-1][0]) + abs(table[i][1]-table[list1[i]-1][1])
    return sum

#create parseMe queue, dictionary dictAlreadySeen, list lookup, boolean endloop, list path, int counter
parseMe = Q.PriorityQueue()#[root]
tup = (manhattan(root), root)
parseMe.put(tup)
dictAlreadySeen = {root:""}
keeplooping = True
path = []
counter = 1

    #print method
def printRoot(root):
    temp = root
    print('----------')
    print(temp[0], ' ', temp[1], ' ', temp[2], ' ', temp[3])
    print(temp[4], ' ', temp[5], ' ', temp[6], ' ', temp[7])
    print(temp[8], ' ', temp[9], ' ', temp[10], ' ', temp[11])
    print(temp[12], ' ', temp[13], ' ', temp[14], ' ', temp[15])
    print('----------')
def inversionCt(myStr):
    #return len([1 for i in range(len(myStr)-1) for j in range(i+1,len(myStr)) if myStr[i]>myStr[j])]):
    return len([1 for i in range(len(myStr)-1) for j in range(i+1,len(myStr)) if myStr[i]>myStr[j]])
    #return sum(myStr[i]>myStr[j] for i in range(len(myStr)-1) for j in range(i+1,len(myStr)))
    #instead of x%2 use x&1


def distanceRows(myStr):
    gapin = myStr.index('_')
    if gapin < 4:
        return 3
    elif gapin < 8:
        return 2
    elif gapin <12:
        return 1
    return 0

def neighbors(n):
    toret = []
    gapin = n.index('_')
    for i in lookup[gapin]:
        t = list(n)
        t[gapin], t[i] = t[i], t[gapin]
        toret.append(''.join(t))
    return toret

def is_in_queue(x, q):
    with q.mutex:
        return x in q.queue

def finish(dictAlreadySeen, numImp, numRem, numClosedSet, runTime, size):
    path = []
    counter = 1
    pathlocation = SOLVEDSTATE
    path.insert(0, pathlocation)
    while (dictAlreadySeen[pathlocation] != root):
        path.insert(0, dictAlreadySeen[pathlocation])
        pathlocation = dictAlreadySeen[pathlocation]
    print('---------------')
    print(root[0], ' ', root[1], ' ', root[2], ' ', root[3])
    print(root[4], ' ', root[5], ' ', root[6], ' ', root[7])
    print(root[8], ' ', root[9], ' ', root[10], ' ', root[11])
    print(root[12], ' ', root[13], ' ', root[14], ' ', root[15])
    print('---------------')
    for i in range(0, len(path)):
        print(path[i][0], ' ', path[i][1], ' ', path[i][2], ' ', path[i][3])
        print(path[i][4], ' ', path[i][5], ' ', path[i][6], ' ', path[i][7], ' Step ', counter)
        print(path[i][8], ' ', path[i][9], ' ', path[i][10], ' ', path[i][11])
        print(path[i][12], ' ', path[i][13], ' ', path[i][14], ' ', path[i][15])
        print('---------------')
        counter += 1

    print('Shortest path length: ', counter-1)
    print('Number of times an item in openSet was improved:', numImp)
    print('Number of times an item in openSet was removed:', numRem)
    print('Number of elements in openSet when goal was reached:', size)
    print('Number of elements in closedSet when goal was reached:', numClosedSet)
    print('Run time: ', runTime)

#iterate
liststring = list(root)
templiststring = list(root)
for i in liststring:
    if i == 'A': i = 1
    if i == 'B': i = 2
    if i == 'C': i = 3
    if i == 'D': i = 4
    if i == 'E': i = 5
    if i == 'F': i = 6
    if i == 'G': i = 7
    if i == 'H': i = 8
    if i == 'I': i = 9
    if i == 'J': i = 10
    if i == 'K': i = 11
    if i == 'L': i = 12
    if i == 'M': i = 13
    if i == 'N': i = 14
    if i == 'O': i = 15
    if i == '_': liststring.remove(i)
#print(templiststring)
statesremoved = 0
starttime = time.time()
if inversionCt(liststring)%2 != distanceRows(templiststring)%2:#(4 - (root.index('_')+1 // 4)) % 2:
    print("unsolvable")
    print('Run time: ', time.time()-starttime)


else:

    openSet = Q.PriorityQueue()
    tuproot = (manhattan(root), root)
    openSet.put(tuproot)
    closedSet = set()
    alreadySeen = {root:root}
    pathlens = {root:0}

    numTimesImproved = 0
    numTimesRemoved = 0

    notdone = True

    while notdone and openSet.qsize()>0:
        current = openSet.get(0)[1]
        numTimesRemoved += 1
        if current == SOLVEDSTATE:
            notdone = False
            finish(alreadySeen, numTimesImproved, numTimesRemoved, len(closedSet), time.time()-starttime, openSet.qsize())
            continue
        closedSet.add(current)
        for n in neighbors(current):
            newpathlencount = pathlens[current] + 1
            if not n in pathlens or newpathlencount < pathlens[n]:
                if n in pathlens:
                    numTimesImproved += 1
                alreadySeen[n] = current
                pathlens[n] = newpathlencount
                openSet.put((manhattan(n) + pathlens[current], n))