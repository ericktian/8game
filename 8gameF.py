lookup = [[1,3], [0,2,4], [1,5], [0,4,6], [1,3,5,7], [2,4,8], [3,7], [4,6,8], [5,7]]
path = []
counter = 1
states = []
root = '1234567_8'
def numstates(steps):
    pathlen = -1
    count = 0
    parseMe1 = [root]
    dictAlreadySeen1 = {root: ""}
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
                if pathlen == steps:
                    states.append(newnode)
                    count += 1
                pathlen = -1
    print(steps, ': ', count)
    print(states)
numstates(31)