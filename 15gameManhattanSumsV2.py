import time
root = 'MIEAOJFBNKGC_LHD'
lookup = [[1,4], [0,2,5], [1,3,6], [2,7], [0,5,8], [1,4,6,9], [2,5,7,10], [3,6,11], [4,9,12], [5,8,10,13], [6,9,11,14],
     	[7,10,15], [8,13], [9,12,14], [10,13,15], [11,14]]
table = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3],
    	[2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]
def toNum(temp):
    liststring = list(temp)
    for i in range(0, len(liststring)):
        if liststring[i] == 'A': liststring[i] = 1
        elif liststring[i] == 'B': liststring[i] = 2
        elif liststring[i] == 'C': liststring[i] = 3
        elif liststring[i] == 'D': liststring[i] = 4
        elif liststring[i] == 'E': liststring[i] = 5
        elif liststring[i] == 'F': liststring[i] = 6
        elif liststring[i] == 'G': liststring[i] = 7
        elif liststring[i] == 'H': liststring[i] = 8
        elif liststring[i] == 'I': liststring[i] = 9
        elif liststring[i] == 'J': liststring[i] = 10
        elif liststring[i] == 'K': liststring[i] = 11
        elif liststring[i] == 'L': liststring[i] = 12
        elif liststring[i] == 'M': liststring[i] = 13
        elif liststring[i] == 'N': liststring[i] = 14
        elif liststring[i] == 'O': liststring[i] = 15
        elif liststring[i] == '_': liststring[i] = 16
    return liststring
def manhattan(list1):
    sum = 0
    list1 = toNum(list1)
    for i in range(0, len(list1)):
        if list1[i] != 16:
            sum += abs(table[i][0]-table[list1[i]-1][0]) + abs(table[i][1]-table[list1[i]-1][1])
    return sum
def distanceRows(myStr):
    gapin = myStr.index('_')
    if gapin < 4:
        return 3
    elif gapin < 8:
        return 2
    elif gapin <12:
        return 1
    return 0
udrl = 0
def neighbors(n, curman):
    toret = []
    count = 0
    gapin = n.index('_')
    t = []
    sums = 0
    u = 0
    for i in lookup[gapin]:
        count =+ 1
        t = list(n)
        move = gapin-i
        if move == 4: curman += 3
        elif move == -4: curman += -3
        elif move == -1: curman += -1
        elif move == 1: curman += 1
        t[gapin], t[i] = t[i], t[gapin]
        #toret.append(''.join(t))

        sums += curman
        #mansum += curman
        #parse.add(''.join(t))
    return [''.join(t), sums, count]
    #return toret
parseMe = set()
parseMe.add(root)
starttime = time.time()
counter = 0
manhattansum = 0
currmand = manhattan(root)
#udrl = 0 # 1 = up, 2 = down, 3 = right, 4 = left
while time.time()-starttime < 15:
    current = parseMe.pop()
    updates = neighbors(current, currmand)
    parseMe.add(updates[0])
    manhattansum += updates[1]
    counter += updates[2]
    # for n in neighbors(current):
    #     counter += 1
    #     if udrl == 1: currmand += 3
    #     elif udrl == 2: currmand += -3
    #     elif udrl == 3: currmand += -1
    #     elif udrl == 4: currmand += 1
    #     manhattansum += currmand
    #     parseMe.add(n)

print(counter, ' states in 15 seconds')
print('sum of manhattan/n: ', manhattansum/counter)
print('n/time: ', counter/15)
print('manhattan sum: ', manhattansum)
# n = 761215
# time = 15 seconds
# sum of manhattan distances / n = 13.903973253285866
# n / time = 10583913