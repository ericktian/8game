root = "12345678_"
parseMe = [root]
dictAlreadySeen = {root:""}
lookup = [[1,3], [0,2,4], [1,5], [0,4,6], [1,3,5,7], [2,5,8], [3,7], [4,6,8], [5,7]]
last = ""
while len(parseMe) > 0:
    node = parseMe.pop(0)
    gapindex = node.index('_')
    for i in range(0, len(lookup[gapindex])):
        t = list(node)
        t[gapindex], t[lookup[gapindex][i]] = t[lookup[gapindex][i]], t[gapindex]
        newnode = ''.join(t)
        if newnode not in dictAlreadySeen:
            parseMe.append(newnode)
            dictAlreadySeen[newnode] = node
            last = newnode
counter = 0
print(last)