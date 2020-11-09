import sys
import time


ideal = "12345678 "

times = []
avgSteps= []

solTimes = []
solavgSteps= []


def displayBoard(eight):
    print("")
    print(eight[0] + " " + eight[1] + " " + eight[2])
    print(eight[3] + " " + eight[4] + " " + eight[5])
    print(eight[6] + " " + eight[7] + " " + eight[8])
    print("")


def swap(string, indexone, indextwo):
    l = list(string)
    l[indexone], l[indextwo] = l[indextwo], l[indexone]
    space = ""
    for i in l:
        space += i
    return space


def createDic(string,index):

    dict = {}
    dict[0] = [1, 3];dict[1] = [0, 2, 4];dict[2] = [1, 5];dict[3] = [0, 4, 6];dict[4] = [1, 3, 5, 7]; dict[5] = [2, 4, 8]; dict[6] = [3, 7]; dict[7] = [6, 4, 8]; dict[8] = [5, 7]
    myList = []
    for i in dict.get(index):
        inpt = swap(string, index, i)
        myList.append(inpt)
    return myList



def sdisplay(theEndDict, first):
    parent = theEndDict.get("12345678 ")
    a = []
    a.append(parent)
    a.append(ideal)
    while not(parent == first):
        parent = theEndDict.get(parent)
        a.insert(0 , parent)
    for i in a:
        displayBoard(i)
    steps = (len(a)-1)
    return steps

def findAvg(numbers):
    fsum = sum(numbers)
    length = (len(numbers)) + 1
    return (fsum/ length)

def compute(user):
    startTime = time.clock()
    user = user.replace("_", " ")

    times = []
    avgSteps= []
    counter = 0

    finalSet = {user}
    finalDict = {}
    boo = False

    while len(finalSet) != 0:
        temp = finalSet.pop()
        if temp == ideal:
            boo = True
    #       displayBoard(temp)
    #       if(user == ideal):
    #           print("Number of Steps: 0")
            break
        index = temp.index(' ')
        newDic = createDic(temp,index)
        if ideal in newDic:
            finalDict[ideal] = temp
            boo = True
            break
        for x in newDic:
            if x in finalDict:
                pass
            else:
                finalDict[x] = temp
                finalSet.add(x)
    toAdd = (sdisplay(finalDict, user))
    totalTime = (time.clock() - startTime)
    times.append(totalTime)

    if boo:
        solavgSteps.append(toAdd)
        solTimes.append(totalTime)

    if not(boo):
        avgSteps.append(toAdd)
        times.append(totalTime)

user = input("What number? ")


compute(user)

print("Average of steps of solvable combinations are: " + findAvg(solavgSteps))
print("Average of times of solvable combinations are: " + findAvg(solTimes))

print("Average of steps of unsolvable combinations are: " + findAvg(avgSteps))
print("Average of times of unsolvable combinations are: " + findAvg(times))


