#Solution to http://rosalind.info/problems/ba9c/
class SuffixTree:
    number = 0
    def __init__(self):
        self.root = self.Node()
    def create(self,word):
        N = {}
        Leaves = []
        InterNodes = []
        length = len(word)
        for x in range(length):
            curr = self.root
            for y in range(x, length):
                currSym = word[y]
                if(curr.hasLabel(currSym)):
                    curr = curr.lastEdge(currSym).node
                else:
                    newN = self.Node()
                    N[newN.num] = newN
                    curr.e[currSym] = self.Edge(newN, y)
                    curr = newN
                    InterNodes.append(newN)

        return Leaves, InterNodes, N

    def printEdges(self):
        return [ 
        ''.join(x[:-1]) 
        for x in self.root.printEdges(acc = [])
        ]


    class Node:
        def __init__(self):
            self.e = {}
            self.label = None  
            self.sym = None
            self.num = SuffixTree.number
            SuffixTree.number += 1

        def hasLabel(self,sym):
            return sym in self.e

        def isLeaf(self):
            if len(self.e) == 0:
                return True
            else:
                return false

        def setLabel(self,x):
            self.label = x

        def lastEdge(self,sym):
            return self.e[sym]

        def printEdges(self, p = [],acc = []):
            if len(self.e) == 0:
                acc.append(p + [self.sym])
            elif len(self.e)==1:
                for sym,edge in self.e.items():
                    edge.node.printEdges(p + [sym], acc = acc)                
            else:
                if len(p) > 0:
                    acc.append(p + [self.sym])
                for sym,edge in self.e.items():
                    edge.node.printEdges([sym], acc = acc)
            return acc

    class Edge:
        def __init__(self,node,pos):
            self.node = node
            self.position = pos

f2 = open("BA9C/output", "w")
with open('BA9C/input', 'r') as file:
    data = file.read().replace('\n', '')
suffTree = SuffixTree()
suffTree.create(data)
ans = suffTree.printEdges()
for x in ans:
    f2.write(x + "\n")

f2.close
