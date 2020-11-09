
lookup = [[1,3], [0,2,4], [1,5], [0,4,6], [1,3,5,7], [2,4,8], [3,7], [4,6,8], [5,7]]
path = []
counter = 1
steps = []
states = []

root = '12345678_'
def isOneAway(to, fr):
    gapindex = to.index('_')
    for i in range(0, len(lookup[gapindex])):
        if fr.index('_') == lookup[gapindex][i]:
            return True
    return False
def numstates():
    pathlen = -1
    count = 0
    tempnode = ''
    parseMe1 = [root]
    dictAlreadySeen1 = {root: ""}
    #states = []
    while len(parseMe1) > 0:
        node = parseMe1.pop(0)
        gapindex = node.index('_')
        for i in range(0, len(lookup[gapindex])):
            t = list(node)
            t[gapindex], t[lookup[gapindex][i]] = t[lookup[gapindex][i]], t[gapindex]
            newnode = ''.join(t)
            if newnode not in dictAlreadySeen1:
                parseMe1.append(newnode)
                dictAlreadySeen1[newnode] = node
                tempnode = newnode
                while tempnode in dictAlreadySeen1:
                    pathlen += 1
                    tempnode = dictAlreadySeen1[tempnode]
                #print(len(states))
                if pathlen not in steps:# and (len(states) > 0 or not isOneAway(newnode, states[-1])):
                    if len(states) > 0:
                        if isOneAway(newnode, states[-1]):
                            count += 1
                            steps.append(pathlen)
                            states.append(newnode)
                    else:
                        count += 1
                        steps.append(pathlen)
                        states.append(newnode)
                    #states.append(newnode)
                #elif pathlen > steps:
                    #return
                pathlen = -1
    #print("Number of states requiring ", steps, " step(s): ", count)
    #print(steps, ': ', count)
    states.insert(0, root)
    print(len(states))
    print(states)
    #print(states)
#for i in range(1, 32):
#    numstates(i)
numstates()