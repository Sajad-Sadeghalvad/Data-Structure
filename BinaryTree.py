class Node:
    def __init__(self, data= None):
        self.left = None
        self.right = None
        self.data = data

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def get_data(self):
        return self.data
    
class BinaryTree:
    def __init__(self):
        self.x = []

    def inorder(self, root):
        if root:
            self.inorder(root.get_left())
            self.x.append(root.get_data())
            self.inorder(root.get_right())
        return self.x
    
    def numbers_of_nodes(self, root):
        left_nodes = 0
        right_nodes = 0

        if root.get_left():
            left_nodes = self.numbers_of_nodes(root.get_left())
        if root.get_right():
            right_nodes = self.numbers_of_nodes(root.get_right())

        return left_nodes + right_nodes + 1
    
    def count_leaves(self, root):
        if root == None:
            return 0
        if root.get_left() is None and root.get_right() is None:
            return 1
        return self.count_leaves(root.get_left()) + self.count_leaves(root.get_right())    
    
    def count_nodes1D(self, root):
        if root is None:
            return 0
        if root.get_left() is not None and root.get_right() is None:
            return 1 + self.count_nodes1D(root.get_left())
        if root.get_right() is not None and root.get_left() is None:
            return 1 + self.count_nodes1D(root.get_right())
        if root.get_right() is None and root.get_left() is None:
            return 0
        return self.count_nodes1D(root.get_left()) + self.count_nodes1D(root.get_right())
    
    def count_nodes2D(self, root):
        if root is None:
            return 0
        if root.get_right() is None and root.get_left() is not None:
            return self.count_nodes1D(root.get_left())
        if root.get_right() is not None and root.get_left() is None:
            return self.count_nodes1D(root.get_right())
        if root.get_right() is None and root.get_left() is None:
            return 0
        return 1 + self.count_nodes2D(root.get_right()) + self.count_nodes2D(root.get_left())
    
    def find_max(self, root):
        if root is None:
            return float('-inf')
        return max(self.find_max(root.get_left()), self.find_max(root.get_right()), root.get_data())
    
    def sum_nodes_values(self, root):
        if root is None:
            return 0
        return self.sum_nodes_values(root.get_left()) + self.sum_nodes_values(root.get_right()) + root.get_data()
    
    def count_height(self, root):
        if root is None:
            return 0
        return 1 + max(self.count_height(root.get_left()), self.count_height(root.get_right())) 

r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)

bt = BinaryTree()
# x = bt.inorder(r)
# print(x)

# y = bt.numbers_of_nodes(r)
# print(y)

# print(bt.count_leaves(r))
# print(bt.count_nodes1D(r))
# print(bt.count_nodes2D(r))
# print(bt.find_max(r))
# print(bt.sum_nodes_values(r))
print(bt.count_height(r))