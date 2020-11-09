import sys


class Tree:
    __nodes = []
    __path = []
    __value = ""
    __side = 0

    def __init__(self, val):
        self.__value = val
        self.__side = len(val) ** .5
        #print("init")
        #self.__path.append(val)
        #print(self.__path)

    def add_node(self, node):
        self.__nodes.append(node)
        node.__path = []
        for i in range(0, len(self.__path)):
            node.__path.append(self.__path[i])
        node.__path.append(node.__value)
        #print("addnode")

    def get_path(self):
        return self.__path

    def get_nodes(self):
        return self.__nodes

    def get_val(self):
        return self.__value

    def is_correct(self):
        if self.__value == "12345678_":
            return True
        else: return False

    def is_incorrect(self):
        if self.__value == "12345687_":
            return True
        else: return False

    def move(self):
        if self.is_correct():
            # print("correct")
            return self.__path
        if self.is_incorrect():
            # print("incorrect")
            return self.__path
        index = self.__value.index("_")
        if index == 0:
            self.moveleft(0)
            self.moveup(0)
        elif index == 1:
            self.moveup(1)
            self.moveright(1)
            self.moveleft(1)
        elif index == 2:
            self.moveup(2)
            self.moveright(2)
        elif index == 3:
            self.moveleft(3)
            self.movedown(3)
            self.moveup(3)
        elif index == 4:
            self.moveright(4)
            self.moveleft(4)
            self.moveup(4)
            self.movedown(4)
        elif index == 5:
            self.moveright(5)
            self.movedown(5)
            self.moveup(5)
        elif index == 6:
            self.moveleft(6)
            self.movedown(6)
        elif index == 7:
            self.movedown(7)
            self.moveleft(7)
            self.moveright(7)
        elif index == 8:
            self.moveright(8)
            self.movedown(8)
        # hardcoded corners
        #if index == 0:
        #    self.moveleft(index)
        #    self.moveup(index)
        #if index == self.__side - 1:
        #    self.moveright(index)
        #    self.moveup(index)
        #if index == len(self.__value)-1:
        #    self.moveright(index)
        #    self.movedown(index)
        #if index == len(self.__value)-self.__side:
        #    self.moveleft(index)
        #    self.movedown(index)
        # edges
        #elif index % 3 == 0:
        #    self.moveup(index)
        #     self.movedown(index)
        #     self.moveleft(index)
        # elif index % 3 == self.__side - 1:
        #     self.moveup(index)
        #     self.movedown(index)
        #     self.moveright(index)
        # # centers
        # else:
        #     self.moveright(index)
        #     self.moveleft(index)
        #     self.moveup(index)
        #     self.movedown(index)
        # print("other")
        return []
        # recur no recurring nvm

    def swap(self, index1, index2):
        t = list(self.__value)
        t[index1], t[index2] = t[index2], t[index1]
        self.__value = ''.join(t)

    def moveleft(self, gapindex):
        st1 = self.__value
        #st[gapindex], st[gapindex+1] = st[gapindex+1], st[gapindex]
        t1 = list(st1)
        t1[int(gapindex)], t1[int(gapindex + 1)] = t1[int(gapindex + 1)], t1[int(gapindex)]
        self.add_node(Tree(''.join(t1)))

    def moveright(self, gapindex):
        st2 = self.__value
        #st[gapindex], st[gapindex-1] = st[gapindex-1], st[gapindex]
        t2 = list(st2)
        t2[int(gapindex)], t2[int(gapindex - 1)] = t2[int(gapindex - 1)], t2[int(gapindex)]
        self.add_node(Tree(''.join(t2)))

    def moveup(self, gapindex):
        st3 = self.__value
        t3 = list(st3)
        #st[int(gapindex)], st[int(gapindex)+int(self.__side)] = st[int(gapindex)+int(self.__side)], st[int(gapindex)]
        t3[int(gapindex)], t3[int(gapindex+self.__side)] = t3[int(gapindex+self.__side)], t3[int(gapindex)]
        self.add_node(Tree(''.join(t3)))

    def movedown(self, gapindex):
        st4 = self.__value
        t4 = list(st4)
        #st[gapindex], st[gapindex-self.__side] = st[gapindex-self.__side], st[gapindex]
        t4[int(gapindex)], t4[int(gapindex-self.__side)] = t4[int(gapindex-self.__side)], t4[int(gapindex)]
        self.add_node(Tree(''.join(t4)))
    def printcorrectly(self):
        #t = list(self.__path)
        #s = []
        #for i in range(0, int(self.__side)):
        #    for k in range(0, int(self.__side)):
        #        s.append(t[i*k])
        #    print(" ".join(s))
        #    print("\n")
        for i in range(0, len(self.__path)):
            print(self.__path[i][0], " ", self.__path[i][1], " ", self.__path[i][2])
            print(self.__path[i][3], " ", self.__path[i][4], " ", self.__path[i][5])
            print(self.__path[i][6], " ", self.__path[i][7], " ", self.__path[i][8])
            print("---------")

    def printonecorrectly(self, heresastring):
        t = list(heresastring)
        print(t[0], " ", t[1], " ", t[2])
        print(t[3], " ", t[4], " ", t[5])
        print(t[6], " ", t[7], " ", t[8])
        print("---------")


inp = sys.argv[1]
if(len(inp)==8):
    inp = (inp, "_")
elif(len(inp)<8):
    inp = (inp, "_", sys.argv[2])
inp = ''.join(inp)
#print(inp)
tree = Tree(inp)


arr = [tree]
print("")
if not tree.is_correct() and not tree.is_incorrect():
    popped = arr.pop(0)
#if(len(tree.move())==0): popped = arr.pop(0)
    while len(popped.move()) == 0:
        #print(popped.get_path())
        for i in range(0, len(popped.get_nodes())):
            arr.append(popped.get_nodes()[i])
        popped = arr.pop(0)
#print(len(popped.move()))
#print(len([]))
#print(popped.move())
    #print(inp)
    popped.printonecorrectly(inp)
    popped.printcorrectly()#print(popped.get_path())
    print(len(popped.get_path()))
else:
    print(tree.get_val())
    print("0")