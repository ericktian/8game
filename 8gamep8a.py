root = "12345678_"

#create parseMe queue, dictionary dictAlreadySeen, list lookup, boolean endloop, list path, int counter
parseMe = [root]
dictAlreadySeen = {root:""}
lookup = [[1,3], [0,2,4], [1,5], [0,4,6], [1,3,5,7], [2,5,8], [3,7], [4,6,8], [5,7]]
states = [root]
it = 0

while len(parseMe) > 0:
    node = parseMe.pop(0)
    gapindex = node.index('_')
    second = False
    count = 0
    for i in range(0, len(lookup[gapindex])):
        if count < 2:
            t = list(node)
            t[gapindex], t[lookup[gapindex][i]] = t[lookup[gapindex][i]], t[gapindex]
            newnode = ''.join(t)
            if newnode not in dictAlreadySeen:
                dictAlreadySeen[newnode] = node
                count += 1
                if not second:
                    parseMe.append(newnode)
                    second = True
                elif(second):
                    states.append(newnode)
                    second = False
    it += 1
print(len(states))
print(states)