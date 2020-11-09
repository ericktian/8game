
lookup = [[1,3], [0,2,4], [1,5], [0,4,6], [1,3,5,7], [2,4,8], [3,7], [4,6,8], [5,7]]
path = []
counter = 1
#steps = []
states = []

root = '1234_6758'
def inversionCt(myStr):
    return len([1 for i in range(len(myStr)-1) for j in range(i+1,len(myStr)) if myStr[i]>myStr[j]])

def allstates(myStr):
    keeplooping = True
    parseMe = [myStr]
    dictAlreadySeen = {myStr: ""}
    lookup = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 5, 8], [3, 7], [4, 6, 8], [5, 7]]
    toret = []
    counter = 1
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
                if(newnode == root):
                    pathlocation = newnode
                    toret.insert(0, pathlocation)
                    while(dictAlreadySeen[pathlocation] != myStr):
                        toret.insert(0, dictAlreadySeen[pathlocation])
                        pathlocation = dictAlreadySeen[pathlocation]
                    #print(toret)
                    keeplooping = False
    toret.insert(0, myStr)
    return toret
def inversionCountLessThanFive(node):
    listpath = allstates(node)
    for i in range(1, len(listpath)):
        if abs(inversionCt(listpath[i]) - inversionCt(listpath[i-1])) > 4:
            return False
    return True
def numstates():
    pathlen = -1
    count = 0
    tempnode = ''
    parseMe1 = [root]
    dictAlreadySeen1 = {root: ""}
    #states = []
    while len(parseMe1) > 0:
        if len(parseMe1) == 1: print(parseMe1[0])
        node = parseMe1.pop(0)
        gapindex = node.index('_')
        for i in range(0, len(lookup[gapindex])):
            t = list(node)
            t[gapindex], t[lookup[gapindex][i]] = t[lookup[gapindex][i]], t[gapindex]
            newnode = ''.join(t)
            if newnode not in dictAlreadySeen1:
                if inversionCountLessThanFive(newnode): parseMe1.append(newnode)
                dictAlreadySeen1[newnode] = node
                tempnode = newnode
                while tempnode in dictAlreadySeen1:
                    pathlen += 1
                    tempnode = dictAlreadySeen1[tempnode]
                pathlen = -1
    #print("Number of states requiring ", steps, " step(s): ", count)
    #print(steps, ': ', count)
    #print(len(states))
    #print(states)
    #print(states)
numstates()
#numstates()