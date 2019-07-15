#!/usr/bin/env python3


class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    def __repr__(self):
        return 'Node({})'.format(self.get_value())
    
    def __str__(self):
        return 'Node({})'.format(self.get_value())
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

    def pre_order(self, node):
        if node:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)
    
    def in_order(self, node):
        if node:
            self.pre_order(node.left)
            print(node.value)
            self.pre_order(node.right)
    
    def post_order(self, node):
        if node:
            self.pre_order(node.left)
            self.pre_order(node.right)
            print(node.value)
            


if __name__ == '__main__':
    tree = Tree('apple')
    tree.get_root().set_left_child(Node('banana'))
    tree.get_root().set_right_child(Node('cherry'))
    tree.get_root().get_left_child().set_left_child(Node('dates'))
    print(tree)
