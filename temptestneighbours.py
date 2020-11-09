# lookup = [[1,3], [0,2,4], [1,5], [0,4,6], [1,3,5,7], [2,4,8], [3,7], [4,6,8], [5,7]]
#
# def neighborsDifferByOne(node):
#     listt = list(node)
#     for i in range(0, len(listt)):
#         for j in range(0, len(lookup[i])):
#             if listt[i] != '_' and listt[lookup[i][j]] != '_':
#                 if abs(int(listt[i])-int(listt[lookup[i][j]])) <= 1:
#                     print(listt[i], listt[lookup[i][j]])
#                     print(i, lookup[i][j])
#                     return False
#     return True
# print(neighborsDifferByOne("48516372_"))

# def completelyDifferent(node):
#     root = list('12345678_')
#     for i in range(0, len(node)):
#         if node[i] != '_' and node[i] == root[i]:
#             return False
#     return True
# print(completelyDifferent('23456781_'))

# root = '12345678_'
# def allstates(myStr):
#     keeplooping = True
#     parseMe = [myStr]
#     dictAlreadySeen = {myStr: ""}
#     lookup = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 5, 8], [3, 7], [4, 6, 8], [5, 7]]
#     toret = []
#     counter = 1
#     while keeplooping and len(parseMe) > 0:
#         node = parseMe.pop(0)
#         gapindex = node.index('_')
#         for i in range(0, len(lookup[gapindex])):
#             t = list(node)
#             t[gapindex], t[lookup[gapindex][i]] = t[lookup[gapindex][i]], t[gapindex]
#             newnode = ''.join(t)
#             if newnode not in dictAlreadySeen:
#                 parseMe.append(newnode)
#                 dictAlreadySeen[newnode] = node
#                 if(newnode == '12345678_'):
#                     pathlocation = newnode
#                     toret.insert(0, pathlocation)
#                     while(dictAlreadySeen[pathlocation] != myStr):
#                         toret.insert(0, dictAlreadySeen[pathlocation])
#                         pathlocation = dictAlreadySeen[pathlocation]
#                     #print(toret)
#                     keeplooping = False
#     toret.insert(0, myStr)
#     return toret
# print(allstates('1_3426758'))

# lookup = [[1,4], [0,2,5], [1,3,6], [2,7], [0,5,8], [1,4,6,9], [2,5,7,10], [3,6,11], [4,9,12], [5,8,10,13], [6,9,11,14],
#           [7,10,15], [8,13], [9,12,14], [10,13,15], [11,14]]
# def neighbors(n):
#     toret = []
#     gapin = n.index('_')
#     for i in lookup[gapin]:
#         t = list(n)
#         t[gapin], t[i] = t[i], t[gapin]
#         toret.append(''.join(t))
#     return toret
# print(neighbors('ABCDEFGHIJKLMN_O'))

table = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3],
         [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]

def toNum(temp):
    liststring = list(temp)
    for i in range(0, len(liststring)):
        if liststring[i] == 'A': liststring[i] = 1
        if liststring[i] == 'B': liststring[i] = 2
        if liststring[i] == 'C': liststring[i] = 3
        if liststring[i] == 'D': liststring[i] = 4
        if liststring[i] == 'E': liststring[i] = 5
        if liststring[i] == 'F': liststring[i] = 6
        if liststring[i] == 'G': liststring[i] = 7
        if liststring[i] == 'H': liststring[i] = 8
        if liststring[i] == 'I': liststring[i] = 9
        if liststring[i] == 'J': liststring[i] = 10
        if liststring[i] == 'K': liststring[i] = 11
        if liststring[i] == 'L': liststring[i] = 12
        if liststring[i] == 'M': liststring[i] = 13
        if liststring[i] == 'N': liststring[i] = 14
        if liststring[i] == 'O': liststring[i] = 15
        if liststring[i] == '_': liststring[i] = 16
    return liststring
#manhattan distance/
def manhattan(list1):
    sum = 0
    list1 = toNum(list1)
    for i in range(0, len(list1)):
        if list1[i] != 16:
            sum += ((table[i][0]-table[int(list1[i])-1][0])**2)**.5 + ((table[i][1]-table[int(list1[i])-1][1])**2)**.5
    return sum
print(manhattan('MIEAOJFBNKGC_LHD'))