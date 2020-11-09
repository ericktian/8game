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
#manhattan distance
def manhattan(list1):
    sum = 0
    list1 = toNum(list1)
    for i in range(0, len(list1)):
        if list1[i] != '_':
            sum += ((table[i][0]-table[int(list1[i])-1][0])**2)**.5 + ((table[i][1]-table[int(list1[i])-1][1])**2)**.5
    return sum
def manhattaninout(listin, listout):
    listout = list(listout)
    listin = list(listin)

node = ''