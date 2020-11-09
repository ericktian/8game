import sys
#make root as string
root = sys.argv[1]
if(len(root)==8):
    root = (root, "_")
elif(len(root)<8):
    root = (root, "_", sys.argv[2])
root = ''.join(root)

#create parseMe queue, dictionary dictAlreadySeen, list lookup, boolean endloop, list path, int counter
parseMe = [root]
dictAlreadySeen = {root:""}
lookup = [[1,3], [0,2,4], [1,5], [0,4,6], [1,3,5,7], [2,5,8], [3,7], [4,6,8], [5,7]]
keeplooping = True
path = []
counter = 1

#iterate
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
                    keeplooping = False
    if(len(parseMe)==0): print("No possible solution")
    else: print("Steps taken: ", len(path))