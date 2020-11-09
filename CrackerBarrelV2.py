import sys
input = int(sys.argv[1])
listroot = []
for i in range(0, 15):
    if i == input:
        listroot.append('0')
    else:
        listroot.append('1')
root = ''.join(listroot)

parseMe = [(root, 0, 0)]
dictAlreadySeen = {root:""}
lookup = [[3, 4, 5], [6, 7, 8], [7, 8, 9], [10, 11, 12], [11, 12, 13], [12, 13, 14],
          [0, 1, 3], [1, 3, 6], [3, 6, 10], [2, 4, 7], [4, 7, 11], [5, 8, 12],
          [0, 2, 5], [2, 5, 9], [5, 9, 14], [1, 4, 8], [4, 8, 13], [3, 7, 12]]
keeplooping = True
path = []
counter = 1

#iterate
def neighbors(n):
    toret = []
    for i in lookup:
        if n[i[0]] == '0' and n[i[1]] == '1' and n[i[2]] == '1':
            toret.append((n[:i[0]] + '1' + n[i[0]+1:i[1]] + '0' + n[i[1]+1:i[2]] + '0' + n[i[2]+1:], i[2], i[0]))
        elif n[i[0]] == '1' and n[i[1]] == '1' and n[i[2]] == '0':
            toret.append((n[:i[0]] + '0' + n[i[0]+1:i[1]] + '0' + n[i[1]+1:i[2]] + '1' + n[i[2]+1:], i[0], i[2]))
    return toret
def finish():
    counter = 1
    pathlocation = newnode
    path.insert(0, pathlocation)
    while (dictAlreadySeen[pathlocation][0] != root):
        path.insert(0, dictAlreadySeen[pathlocation])
        pathlocation = dictAlreadySeen[pathlocation]
    print('----------')
    for i in range(0, len(path)):
        print(path[i][1], '-->', path[i][2], 'Step:', counter)
        print('----------')
        counter += 1
    exit()

while keeplooping and len(parseMe) > 0:
    node = parseMe.pop(0)
    for newnode in neighbors(node[0]):
        if newnode not in dictAlreadySeen:
            parseMe.append(newnode)
            dictAlreadySeen[newnode] = node
            if(newnode[0].count('1') == 1):
                finish()
                keeplooping = False
if(len(parseMe)==0): print("No possible solution")
else: print("Steps taken: ", len(path))