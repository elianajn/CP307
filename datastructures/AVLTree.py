from . BinarySearchTree import *

class AVLTree(BinarySearchTree):

    def getNodeBalance(self, node):
        left = self.depthNode(node.left)
        right = self.depthNode(node.right)
        return left - right

    def depthNode(self, node):
        # from geeks for geeks
        # https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/
        # print("lord help me")
        if node == None:
            return 0

            # Get the depth of the left and right subtree
            # using recursion.
        print("here????")
        leftDepth = depthNode(node.left)
        print("here????")
        rightDepth = depthNode(node.right)

  # Choose the larger one and add the root to it.
        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1
        # print("doing this")
        # print(node)
        # if node is None:
        #     print("hello??")
        #     return 0
        # elif(node.left is None and node.right is None):
        #     return 1
        # else:
        #     left_subtree_depth += depthNode(node.left)
        #     right_subtree_depth += depthNode(node.right)
        #     if (left_subtree_depth > right_subtree_depth):
        #         return left_subtree_depth+1
        #     else:
        #         return right_subtree_depth+1

    def remove(self, key):
        removed = BinarySearchTree.delete(self, key)
        self.balanceTree(removed, remove=True)

    def insert(self, key):
        new_node = BinarySearchTree.put(self, key, None)
        self.balanceTree(new_node, remove=False)
        print("finishing balancing")

    def balanceTree(self, curr_node, remove=False):
        print("here")
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
                        gradchild = path[-2]

                if balance > 1:
                    if child.left == gradchild: # LEFT LEFT
                        if self.root == current:
                            self.root = child
                        if current.parent != None:
                            if current.parent.left == current:
                                current.parent.left = child
                            else:
                                current.parent.right = child
                        child.parent = current.parent
                        child.left = child.right
                        if current.left != None:
                            current.left.parent = current
                        child.right = current
                        current.parent = child
                        curr_node = child
                    else: # LEFT RIGHT
                        if self.root == curent:
                            self.root = grandchild
                        if current.parent != None:
                            if current.parent.left == current:
                                current.parent.left = grandchild
                            else:
                                current.parent.right = grandchild
                        grandchild.parent = current.parent
                        grandchild.left = child
                        child.parent = grandchild
                        grandchild.right = current
                        current.parent = grandchild
                        current.left = grandchild.right
                        if curent.left != None:
                            current.left.parent = current
                        child.right = grandchild.left
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
                        child.parent = curret.parent
                        current.right = child.left
                        if current.right != None:
                            current.right.parent = current
                        child.left = current
                        current.paret = child
                        curr_node = child
                    else: # RIGHT LEFT
                        if self.root == curent:
                            self.root = grandchild
                        if current.parent != None:
                            if current.parent.left == current:
                                current.parent.left = grandchild
                            else:
                                current.parent.right = grandchild
                        grandchild.parent = current.parent
                        grandchild.right = child
                        child.parent = grandchild
                        grandchild.left = current
                        current.parent = grandchild
                        current.right = grandchild.right
                        if curent.right != None:
                            current.right.parent = current
                        child.left = grandchild.left
                        if child.left != None:
                            child.left.parent = child
                        curr_node = grandchild
        path.append(curr_node)
        curr_node = curr_node.parent
