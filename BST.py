
class Node:
    def __init__(self, val, p = None):
        self.l = None
        self.r = None
        self.p = p
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def _find_1(self, val, node, parent = None):

        if(val == node.v):
            print("get it !!!!!!!")
            print('val_1 = ', val)
            print(node)
            print(parent)
            return (node, parent)

        elif(val < node.v and node.l != None):
            return self._find_1(val, node.l, node)
        elif(val > node.v and node.r != None):
            return self._find_1(val, node.r, node)


    # del node in BST
    def deleteNode(self, val):
        node = None
        parent = None
        ret_val = None
        print('val = ', val)
        if(self.root != None):
            ret_val_1 = self._find_1(val, self.root)
            #print('mgwognwo',ret_val_1)
            node = ret_val_1[0]
            parent = ret_val_1[1]
            #int('test', node.v)
            #print('test', parent.v)
            if node != None:

                if node.l == None and node.r == None:
                    if node is parent.l:
                        parent.l = None
                        del node
                    else:
                        parent.r = None
                        del node
                elif (node.l == None and node.r != None):
                    if node is parent.r:
                        parent.r = node.r
                        del node
                    else:
                        parent.l = node.r
                        del node
                elif (node.l != None and node.r == None):
                    if node is parent.l:
                        parent.l = node.l
                        del node
                    else:
                        parent.r = node.l
                        del node
                else:
                    val_node = node
                    parent = node
                    node = node.r
                    while node.l != None:
                        parent = node
                        node = node.l
                    val_node.v = node.v
                    parent.l = None
                    del node




            


    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)


tree = Tree()
tree.add(28)
tree.add(15)
tree.add(40)
tree.add(10)
tree.add(16)
tree.add(30)
tree.add(50)
tree.add(29)
tree.add(35)
tree.add(41)
tree.add(51)
tree.printTree()
tree.deleteNode(28)
tree.printTree()