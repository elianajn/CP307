from . BinarySearchTree import *

class AVLTree(BinarySearchTree):

    def getNodeBalance(self, node):
        left = self.depthNode(node.left)
        right = self.depthNode(node.right)
        return left - right

    def depthNode(self, node):
        # from geeks for geeks
        # https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/
        if node == None:
            return 0
        leftDepth = self.depthNode(node.left)
        rightDepth = self.depthNode(node.right)
        return max(leftDepth, rightDepth)+1

    def remove(self, key):
        removed = BinarySearchTree.delete(self, key)
        self.balanceTree(removed, remove=True)

    def insert(self, key):
        new_node = BinarySearchTree.put(self, key, None)
        self.balanceTree(new_node, remove=False)

    def balanceTree(self, curr_node, remove=False):
        path = []
        while curr_node != None:
            balance = self.getNodeBalance(curr_node)
            if len(path) > 1:
                if remove:
                    current = curr_node
                    left_child_height = self.depthNode(current.left)
                    right_child_height = self.depthNode(current.right)
                    if left_child_height > right_child_height:
                        child = current.left
                    else:
                        child = current.right

                    left_grandchild_height = self.depthNode(child.left)
                    right_grandchild_height = self.depthNode(child.right)
                    if left_grandchild_height > right_grandchild_height:
                        grandchild = child.left
                    else:
                        grandchild = child.right

                else:
                        current = curr_node
                        child = path[-1]
                        grandchild = path[-2]

                if balance > 1:
                    if child.left == grandchild: # LEFT LEFT
                        if self.root == current:
                            self.root = child
                        if current.parent != None:
                            if current.parent.left == current:
                                current.parent.left = child
                            else:
                                current.parent.right = child
                        child.parent = current.parent
                        current.left = child.right
                        if current.left != None:
                            current.left.parent = current
                        child.right = current
                        current.parent = child
                        curr_node = child
                    else: # LEFT RIGHT
                        w = child.left
                        x = grandchild.left
                        y = grandchild.right
                        z = current.right
                        p = current.parent

                        if self.root == current:
                            self.root = grandchild
                        if p != None:
                            if p.left == current:
                                p.left = grandchild
                            else:
                                p.right = grandchild
                        grandchild.parent = p
                        grandchild.left = child
                        child.parent = grandchild
                        grandchild.right = current
                        current.parent = grandchild
                        current.left = y
                        if current.left != None:
                            current.left.parent = current
                        child.right = x
                        if child.right != None:
                            child.right.parent = child
                        curr_node = grandchild
                elif balance < -1:
                    if child.right == grandchild: # RIGHT RIGHT
                        if self.root == current:
                            self.root = child
                        if current.parent != None:
                            if current.parent.left == current:
                                current.parent.left = child
                            else:
                                current.parent.right = child
                        child.parent = current.parent
                        current.right = child.left
                        if current.right != None:
                            current.right.parent = current
                        child.left = current
                        current.paret = child
                        curr_node = child
                    else: # RIGHT LEFT
                        w = child.left
                        x = grandchild.left
                        y = grandchild.right
                        z = current.right
                        p = current.parent

                        if self.root == current:
                            self.root = grandchild
                        if p != None:
                            if p.left == current:
                                p.left = grandchild
                            else:
                                p.right = grandchild
                        grandchild.parent = p
                        grandchild.right = child
                        child.parent = grandchild
                        grandchild.left = current
                        current.parent = grandchild
                        current.right = y
                        if current.right != None:
                            current.right.parent = current
                        child.left = x
                        if child.left != None:
                            child.left.parent = child
                        curr_node = grandchild
            path.append(curr_node)
            curr_node = curr_node.parent
