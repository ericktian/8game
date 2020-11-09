import sys


class Tree:
    __nodes = []
    __path = []
    __value = ""
    __side = 0

    def __init__(self, val):
        self.__value = val
        self.__side = len(val) ** .5
        print("init")
        #self.__path.append(val)
        #print(self.__path)
#ISSUE
    def add_node(self, node):
        self.__nodes.append(node)
        node.__path = []
        for i in range(0, len(self.__path)):
            node.__path.append(self.__path[i])
        node.__path.append(node.__value)
        print("addnode")

    def get_path(self):
        print("getpath")
        return self.__path

    def get_nodes(self):
        print("getnodes")
        return self.__nodes

    def get_val(self):
        print("getval")
        return self.__value

    def is_correct(self):
        print("iscorrect")
        if self.__value == "12345678_":
            return True
        else: return False

    def is_incorrect(self):
        print("isincorrect")
        if self.__value == "12345687_":
            return True
        else: return False

    def move(self):
        print("move")
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
        print("swap")
        t = list(self.__value)
        t[index1], t[index2] = t[index2], t[index1]
        self.__value = ''.join(t)

    def moveleft(self, gapindex):
        print("moveleft")
        st1 = self.__value
        #st[gapindex], st[gapindex+1] = st[gapindex+1], st[gapindex]
        t1 = list(st1)
        t1[int(gapindex)], t1[int(gapindex + 1)] = t1[int(gapindex + 1)], t1[int(gapindex)]
        self.add_node(Tree(''.join(t1)))

    def moveright(self, gapindex):
        print("moveright")
        st2 = self.__value
        #st[gapindex], st[gapindex-1] = st[gapindex-1], st[gapindex]
        t2 = list(st2)
        t2[int(gapindex)], t2[int(gapindex - 1)] = t2[int(gapindex - 1)], t2[int(gapindex)]
        self.add_node(Tree(''.join(t2)))

    def moveup(self, gapindex):
        print("moveup")
        st3 = self.__value
        t3 = list(st3)
        #st[int(gapindex)], st[int(gapindex)+int(self.__side)] = st[int(gapindex)+int(self.__side)], st[int(gapindex)]
        t3[int(gapindex)], t3[int(gapindex+self.__side)] = t3[int(gapindex+self.__side)], t3[int(gapindex)]
        self.add_node(Tree(''.join(t3)))

    def movedown(self, gapindex):
        print("movedown")
        st4 = self.__value
        t4 = list(st4)
        #st[gapindex], st[gapindex-self.__side] = st[gapindex-self.__side], st[gapindex]
        t4[int(gapindex)], t4[int(gapindex-self.__side)] = t4[int(gapindex-self.__side)], t4[int(gapindex)]
        self.add_node(Tree(''.join(t4)))

inp = sys.argv[1]
if(len(inp)==8):
    inp = (inp, "_")
elif(len(inp)<8):
    inp = (inp, "_", sys.argv[2])
inp = ''.join(inp)
#print(inp)
tree = Tree(inp)


arr = [tree]
#popped = arr.pop(0)
while len(arr[0].move()) == 0: #len(popped.move()) == 0:
    #print(popped.get_path())
    print(arr[0].get_path())
    for i in range(0, len(arr[0].get_nodes())): #range(0, len(popped.get_nodes())):
        print("1")
        arr.append(arr[0].get_nodes()[i]) #arr.append(popped.get_nodes()[i])
    print("2")
    arr.pop(0)
    #popped = arr.pop(0)
#print(len(popped.move()))
#print(len([]))
#print(popped.move())
#print(popped.get_path())
print(arr[0].get_path())