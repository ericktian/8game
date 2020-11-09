import sys
input = int(sys.argv[1])
root = []
for i in range(0, 15):
    if i == input:
        root.append(-1)
    else:
        root.append(i)
print(root)

#create parseMe queue, dictionary dictAlreadySeen, list lookup, boolean endloop, list path, int counter
parseMe = [root]
dictAlreadySeen = {root:""}
lookup = [[3, 4, 5], [6, 7, 8], [7, 8, 9], [10, 11, 12], [11, 12, 13], [12, 13, 14],
          [0, 1, 3], [1, 3, 6], [3, 6, 10], [2, 4, 7], [4, 7, 11], [5, 8, 12],
          [0, 2, 5], [2, 5, 9], [5, 9, 14], [1, 4, 8], [4, 8, 13], [3, 7, 12]]
keeplooping = True
path = []
counter = 1

#iterate
def finish():
    counter = 0
    pathlocation = newnode
    path.insert(0, pathlocation)
    while (dictAlreadySeen[pathlocation] != root):
        path.insert(0, dictAlreadySeen[pathlocation])
        pathlocation = dictAlreadySeen[pathlocation]
    print('----------')
    print(root[0], ' ', root[1], ' ', root[2])
    print(root[3], ' ', root[4], ' ', root[5])
    print(root[6], ' ', root[7], ' ', root[8])
    print('----------')
    for i in range(0, len(path)):
        print(path[i][0], ' ', path[i][1], ' ', path[i][2])
        print(path[i][3], ' ', path[i][4], ' ', path[i][5], ' Step ', counter)
        print(path[i][6], ' ', path[i][7], ' ', path[i][8])
        print('----------')
        counter += 1
    return counter

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
                counter = finish()
                keeplooping = False
if(len(parseMe)==0): print("No possible solution")
else: print("Steps taken: ", len(path))