import sys


class Tree:
    __nodes = []
    path = []
    __value = ""
    __side = 0

    def __init__(self, val):
        self.__value = val
        self.__side = len(val) ** .5
        self.path.append(val)

    def add_node(self, node):
        self.__nodes.append(node)
        node.__path.insert(1, self.path)

    def get_path(self):
        return self.path

    def get_nodes(self):
        return self.__nodes

    def is_correct(self):
        if self.__value == "12345678_":
            return True
        return False

    def is_incorrect(self):
        if self.__value == "12345687_":
            return True
        return False

    def move(self):
        if self.is_correct:
            return self.path
        if self.is_incorrect:
            return self.path
        index = self.__value.index("_")
        # hardcoded corners
        if index == 0:
            self.moveleft(index)
            self.moveup(index)
        if index == self.__side - 1:
            self.moveright(index)
            self.moveup(index)
        if index == len(self.__value)-1:
            self.moveright(index)
            self.movedown(index)
        if index == len(self.__value)-self.__side:
            self.moveleft(index)
            self.movedown(index)
        # edges
        elif index % 3 == 0:
            self.moveup(index)
            self.movedown(index)
            self.moveleft(index)
        elif index % 3 == self.__side - 1:
            self.moveup(index)
            self.movedown(index)
            self.moveright(index)
        # centers
        else:
            self.moveright(index)
            self.moveleft(index)
            self.moveup(index)
            self.movedown(index)
        return []
        # recur no recurring nvm

    def moveleft(self, gapindex):
        st = self.__value
        st[gapindex], st[gapindex+1] = st[gapindex+1], st[gapindex]
        self.add_node(Tree(st))

    def moveright(self, gapindex):
        st = self.__value
        st[gapindex], st[gapindex-1] = st[gapindex-1], st[gapindex]
        self.add_node(Tree(st))

    def moveup(self, gapindex):
        st = self.__value
        st[gapindex], st[gapindex+self.__side] = st[gapindex+self.__side], st[gapindex]
        self.add_node(Tree(st))

    def movedown(self, gapindex):
        st = self.__value
        st[gapindex], st[gapindex-self.__side] = st[gapindex-self.__side], st[gapindex]
        self.add_node(Tree(st))

inp = sys.argv[1]
tree = Tree(inp)
arr = [tree]
popped = arr.pop(0)
while popped.move() == []:
    for i in range(0, len(popped.get_nodes())):
        arr.append(popped.get_nodes()[i])
print(popped.get_path)
