import sys
#make root as string
import queue as Q #q = Q.PriorityQueue()
root = sys.argv[1]
if(len(root)==15):
    root = (root, "_")
elif(len(root)<15):
    root = (root, "_", sys.argv[2])
root = ''.join(root)
#print(root)

#create parseMe queue, dictionary dictAlreadySeen, list lookup, boolean endloop, list path, int counter
parseMe = [root]
dictAlreadySeen = {root:""}
lookup = [[1,4], [0,2,5], [1,3,6], [2,7], [0,5,8], [1,4,6,9], [2,5,7,10], [3,6,11], [4,9,12], [5,8,10,13], [6,9,11,14],
          [7,10,15], [8,13], [9,12,14], [10,13,15], [11,14]]
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
print(templiststring)
if inversionCt(liststring)%2 != distanceRows(templiststring)%2:#(4 - (root.index('_')+1 // 4)) % 2:
    print("unsolvable")
else: print("solvable")

if root=='ABCDEFGHIJKLMNO_':
    printRoot(root)
    print('Steps taken: 0')
else:
    notin = 0
    #count = 0
    while keeplooping and len(parseMe) > 0:# and count <10:
        #count += 1
        #print(len(parseMe))
        node = parseMe.pop(0)
        gapindex = node.index('_')
        for i in range(0, len(lookup[gapindex])):
            t = list(node)
            t[gapindex], t[lookup[gapindex][i]] = t[lookup[gapindex][i]], t[gapindex]
            newnode = ''.join(t)
            #print(newnode)
            if newnode not in dictAlreadySeen:
                parseMe.append(newnode)
                dictAlreadySeen[newnode] = node
                notin+=1
                #print(notin)
                if newnode == 'ABCDEFGHIJKLMNO_':
                    print("done")
                    pathlocation = newnode
                    path.insert(0, pathlocation)
                    while(dictAlreadySeen[pathlocation] != root):
                        path.insert(0, dictAlreadySeen[pathlocation])
                        pathlocation = dictAlreadySeen[pathlocation]
                    printRoot(root)
                    for i in range(0, len(path)):
                        printRoot(path[i])
                        print('Step ', counter)
                        counter += 1
                    keeplooping = False
    if(len(parseMe)==0): print("No possible solution")
    else: print("Steps taken: ", len(path))