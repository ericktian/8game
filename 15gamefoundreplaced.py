import sys
#make root as string
root1 = sys.argv[1]
if(len(root1)==15):
    root1 = (root1, "_")
elif(len(root1)<15):
    root1 = (root1, "_", sys.argv[2])
root1 = ''.join(root1)
root1 = root1.replace('A', '1 ')
root1 = root1.replace('B', '2 ')
root1 = root1.replace('C', '3 ')
root1 = root1.replace('D', '4 ')
root1 = root1.replace('E', '5 ')
root1 = root1.replace('F', '6 ')
root1 = root1.replace('G', '7 ')
root1 = root1.replace('H', '8 ')
root1 = root1.replace('I', '9 ')
root1 = root1.replace('J', '10 ')
root1 = root1.replace('K', '11 ')
root1 = root1.replace('L', '12 ')
root1 = root1.replace('M', '13 ')
root1 = root1.replace('N', '14 ')
root1 = root1.replace('O', '15 ')
root = root1.split(' ')
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
    temp = root.replace('1', 'A')
    temp = root.replace('2', 'B')
    temp = root.replace('3', 'C')
    temp = root.replace('4', 'D')
    temp = root.replace('5', 'E')
    temp = root.replace('6', 'F')
    temp = root.replace('7', 'G')
    temp = root.replace('8', 'H')
    temp = root.replace('9', 'I')
    temp = root.replace('10', 'J')
    temp = root.replace('11', 'K')
    temp = root.replace('12', 'L')
    temp = root.replace('13', 'M')
    temp = root.replace('14', 'N')
    temp = root.replace('15', 'O')
    print('----------')
    print(temp[0], ' ', temp[1], ' ', temp[2], ' ', temp[3])
    print(temp[4], ' ', temp[5], ' ', temp[6], ' ', temp[7])
    print(temp[8], ' ', temp[9], ' ', temp[10], ' ', temp[11])
    print(temp[12], ' ', temp[13], ' ', temp[14], ' ', temp[15])
    print('----------')

#iterate
if root==['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','_']:
    printRoot(root)
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
                if newnode == ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','_']:
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