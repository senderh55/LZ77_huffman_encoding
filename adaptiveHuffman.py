import math

class Node(object):
    def __init__(self, char=None, parent=None, weight=0):
        self.char = char
        self.parent = parent
        self.weight = weight
        self.left = None
        self.right = None

class AdaptiveHuffmanTree(object):
    def __init__(self):
        self.NYT = Node()  # NYT stands for "Not Yet Transmitted"
        self.root = self.NYT
        self.nodes = []
        self.seen = [None] * 256

    def get_code(self, char, node, code=''):
        if node.left is None and node.right is None:
            return code if node.char == char else ''
        else:
            temp = ''
            if node.left is not None:
                temp = self.get_code(char, node.left, code+'0')
            if not temp and node.right is not None:
                temp = self.get_code(char, node.right, code+'1')
            return temp

    def find_largest_node(self, weight):
        for node in reversed(self.nodes):
            if node.weight == weight:
                return node

    def swap_nodes(self, n1, n2):
        i1, i2 = self.nodes.index(n1), self.nodes.index(n2)
        self.nodes[i1], self.nodes[i2] = self.nodes[i2], self.nodes[i1]

        n1.parent, n2.parent = n2.parent, n1.parent

        if n1.parent.left is n2:
            n1.parent.left = n1
        else:
            n1.parent.right = n1

        if n2.parent.left is n1:
            n2.parent.left = n2
        else:
            n2.parent.right = n2

    def insert(self, char):
        node = self.seen[ord(char)]

        if node is None:
            spawn = Node(char=char, weight=1)
            internal = Node(parent=self.NYT.parent, weight=1)

            spawn.parent = internal
            internal.left = self.NYT
            internal.right = spawn

            if self.NYT.parent is not None:
                self.NYT.parent.left = internal
            else:
                self.root = internal

            self.nodes.insert(0, internal)
            self.nodes.insert(0, spawn)

            self.NYT.parent = internal
            self.seen[ord(char)] = spawn

            node = internal.parent

        while node is not None:
            largest = self.find_largest_node(node.weight)

            if node is not largest and largest is not node.parent and node is not largest.parent:
                self.swap_nodes(node, largest)

            node.weight = node.weight + 1
            node = node.parent

    def encode(self, text, m):
        result = ''
        
        e = int(math.log2(m))  # calculate e 
        r = m - 2**e  # calculate r
        print("m =",m, " e =",e," r =",r)
        for char in text:
            if self.seen[ord(char)]:
                result += self.get_code(char, self.root)
            else:
                result += self.get_code(None, self.root)  # NYT code
                k = int(char) + 1          
                print("k = ", k, " char = ", char)
                if 1 <= k <= 2*r:
                    result += bin(k - 1)[2:].zfill(e + 1)  # (e+1) bit binary representation of k-1
                else:
                    result += bin(k - r - 1)[2:].zfill(e)  # e-bit binary representation of k-r-1
        
            self.insert(char)
        
        return result
    














