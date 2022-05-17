class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None
#here we will going to make a rapper class
class Tree:
    def __init__(self,root,name=''):
        self.root = root
        self.name = name
        

#here we have defined the root node of the tree, which is equal to 10
node = Node(10)
#here we have defined the first children of the root node value 10 in our tree
node.left = Node(5)
node.right = Node(15)
#now we will further keep defining the tree structure as have to built it further.
node.left.left = Node(2)
node.left.right = Node(7)

#defining the right nodes of the trees
node.right.left = Node(13)
node.right.right = Node(20)
#now we will going to print some nodes of the trees and see what are the values that are present in them
print(node.right.data)
print(node.right.right.data)


#now we will extenstiate the new class of the tree that we have just made, for making the root node of the tree
#we will be calling the class that we have just made.
myTree = Tree(node,'Essex tree')
print(myTree.name)
print(myTree.root.left.data)
print(myTree.root.right.right.data)
