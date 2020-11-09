import sys
class Tree:
    def __init__(self, val):
        self.__value = val
        self.__side = len(val)**.5
        self.__nodes = []
        self.__path = []
        self.__path.append(val)
def add_node(self, node):
    self.__nodes.append(node)
    node.__path.insert(1, self.__path)
def is_correct(self):
    if self.__value=="12345678_":
        return True
    return False
def is_incorrect(self):
    if self.__value=="12345687_":
        return True
    return False
def move(self):
    if(self.is_correct):
        return self.__path
    if(self.is_incorrect):
        return self.__path
    index = self.__value.index("_")
    #hardcoded corners
    if index == 0:
        self.moveLeft(index)
        self.moveUp(index)
    if index == self.__side - 1:
        self.moveRight(index)
        self.moveUp(index)
    if index == len(self.__value)-1:
        self.moveRight(index)
        self.moveDown(index)
    if index == len(self.__value)-self.__side:
        self.moveLeft(index)
        self.moveDown(index)
    #edges
    elif index%3==0:
        self.moveUp(index)
        self.moveDown(index)
        self.moveLeft(index)
    elif index%3==self.__side - 1:
        self.moveUp(index)
        self.moveDown(index)
        self.moveRight(index)
    #centers
    else:
        self.moveRight(index)
        self.moveLeft(index)
        self.moveUp(index)
        self.moveDown(index)
    return []
    #recur no recurring nvm
def moveLeft(self, gapindex):
    str = self.__value
    str[gapindex], str[gapindex+1] = str[gapindex+1], str[gapindex]
    self.add_node(Tree(str))
def moveRight(self, gapindex):
    str = self.__value
    str[gapindex], str[gapindex-1] = str[gapindex-1], str[gapindex]
    self.add_node(Tree(str))
def moveUp(self, gapindex):
    str = self.__value
    str[gapindex], str[gapindex+self.__side] = str[gapindex+self.__side], str[gapindex]
    self.add_node(Tree(str))
def moveDown(self, gapindex):
    str = self.__value
    str[gapindex], str[gapindex-self.__side] = str[gapindex-self.__side], str[gapindex]
    self.add_node(Tree(str))
input = "542_78136"
tree = Tree(input)
arr = [tree]
popped = arr.pop(0)
while(popped.move() == []):
    for i in range(0, len(popped.__nodes)):
        arr.append(popped.__nodes[i])
    #for i in range(0,len(popped.get_nodes())):
    #    arr.append(popped.get_nodes()[i])
#print(popped.get_path)