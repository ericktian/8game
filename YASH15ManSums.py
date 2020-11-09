# Yash Shekar
import time
starttime = time.time()

def swap(pzl, pos1, pos2):

    if pos1 > pos2: pos1, pos2 = pos2, pos1  # next line demands pos1 <= pos2
    return pzl[:pos1] + pzl[pos2] + pzl[pos1 + 1:pos2] + pzl[pos1] + pzl[pos2 + 1:]

def child(stat):
    moves = [[1,4],[0,2,5],[1,3,6],[2,7],[0,5,8],[1,4,6,9],[2,5,7,10],[3,6,11],[4,9,12],[5,8,10,13],[6,9,11,14],
             [7,10,15],[8,13],[9,12,14],[10,13,15],[11,14]]
    pos = stat.find('-')
    return swap(stat, pos, int(moves[pos][0]))
def manD(pzl):
    d = {'1':(0,0),'2':(0,1),'3':(0,2),'4':(0,3),'5':(1,0),'6':(1,1),'7':(1,2),'8':(1,3),'9':(2,0),'a':(2,1),'b':(2,2),'c':(2,3),'d':(3,1),'e':(3,2),'f':(3,3)}
    d2 = {}
    for i in range(0, 16):
        d2[pzl[i]] = i
    return sum([abs(d2[i] // 4 - d[i][1]) + abs(d2[i] % 4 - d[i][0]) for i in pzl if i != "-"])
def compute():
    total = 0
    count = 0
    root = "123456789abcdef-"
    while (time.time()-starttime) < 15:
        total += manD(root)
        count += 1
        root = child(root)
    print("n: ", count, " time: 15 seconds")
    print("avg manD: ", total/count, "n/time: ", count/15)
compute()

# n = 554662
# time: 15 seconds
# Average Manhattan Distance: 5.499967547803887
# n/time: 36977.46666666667

