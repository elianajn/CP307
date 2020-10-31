from PIL import Image, ImageDraw, ImageFont

class BinarySearchTreeNodes:

    def __init__(self, key, payload):
        self.self = self
        self.key = key
        self.payload = payload
        self.parent = None
        self.left = None
        self.right = None

    def numberOfChildren(self):
        if self.right != None and self.left != None:
            return 2
        if self.right != None or  self.left != None:
            return 1
        if self.right == None and self.left == None:
            return 0



class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.current_size = 0

    # Return an integer value indicating how many
    # nodes are in the tree
    def size(self):
        return self.current_size

    # Put a new node into the BST at position, key,
    # with the associated payload of value
    def put(self, key, value):
        new_node = BinarySearchTreeNodes(key, value)
        if self.root == None:
            self.root = new_node
            self.current_size += 1
        else:
            current_node = self.root
            while True:
                if key < current_node.key:
                    if current_node.left != None:
                        current_node = current_node.left
                    else:
                        current_node.left = new_node
                        new_node.parent = current_node
                        self.current_size += 1
                        break
                else:
                    if current_node.right != None:
                        current_node = current_node.right
                    else:
                        current_node.right = new_node
                        new_node.parent = current_node
                        self.current_size += 1
                        break
        return new_node

    # Find and return the value associated with the given key
    def get(self, key):
        if self.root == None:
            raise ERROR("Empty tree")
        current_node = self.root
        while key != current_node.key:
            if key < current_node.key:
                if current_node.left != None:
                    current_node = current_node.left
                else:
                    return "Node associated with key: %d not in tree" % key
            else:
                if current_node.right != None:
                    current_node = current_node.right
                else:
                    return "Node associated with key: %d not in tree" % key
        return current_node.payload


    # Return True or False depending on whether the BST
    # has the given key or not
    def hasKey(self, key):
        if self.root == None:
            return False
        current_node = self.root
        while key != current_node.key:
            if key < current_node.key:
                if current_node.left != None:
                    current_node = current_node.left
                else:
                    return False
            else:
                if current_node.right != None:
                    current_node = current_node.right
                else:
                    return False
        return True

    # Find and remove the node with the given key
    # Make sure the resulting BST is a legal BST
    def delete(self, key):
        if self.hasKey(key) == False:
            print("Key to be removed not in tree")
        current = self.root
        while key != current.key:
            if(key < current.key):
                current = current.left
            else:
                current = current.right
        removed = current
        # leftChild = (key < removed.parent.key) # is this gonna fail if it is the root
        isRoot = (current == self.root)
        if not isRoot:
            leftChild = (key < removed.parent.key)
            if current.numberOfChildren() == 0:
                if leftChild:
                    current.parent.left = None
                else:
                    current.parent.right = None
            elif current.numberOfChildren() == 1:
                if removed.left != None:
                    current = removed.left
                else:
                    current = removed.right
                current.parent = removed.parent
                if leftChild:
                    current.parent.left = current
                else:
                    current.parent.right = current
            elif current.numberOfChildren() == 2:
                current = removed.right
                while current.left != None:
                    current = current.left
                if current == removed.right:
                    current.left = removed.left
                    current.parent = removed.parent
                else:
                    current.parent.left = None
                    current.parent = removed.parent
                    current.left = removed.left
                if leftChild:
                    current.parent.left = current
                else:
                    current.parent.right = current
        else:
            if current.numberOfChildren() == 0:
                self.root = None
            elif current.numberOfChildren() == 1:
                if current.left != None:
                    current.left.parent = None
                    self.root = current.left
                else:
                    current.right.parent = None
                    self.root = current.right
            elif current.numberOfChildren() == 2:
                current = current.right
                while(current.left != None):
                    current = current.left
                current.parent.left = None
                current.left = removed.left
                current.right = removed.right
                current.parent = None
                self.root = current
        self.current_size -= 1
        return removed

    def drawNode(self, draw, font, size, node, depth, node_number):
        number_nodes_layer = 2**depth
        interval = 1000 / number_nodes_layer
        x = int((node_number+1) * interval)
        y = depth * 1000

        draw.ellipse((x, y, x+size, y+size), fill = "blue")
        draw.text((x+(size/3), y+(size/3)), str(node.key), font=font)
        gap = size+10

        next_interval = int(interval/2)
        next_left_x = int((2*node_number+1) * next_interval + size/2)
        next_right_x = int((2*node_number+3) * next_interval + size/2)
        next_y = y + 100 + size/2

        if node.left != None:
            draw.line((x+size/2, y+size/2, next_left_x, next_y), fill="black")
            self.drawNode(draw, font, size, node.left, depth+1, 2*node_number)
        if node.right != None:
            draw.line((x+size/2, y+size/2, next_right_x, next_y), fill = "black")
            self.drawNode(draw, font, size, node.right, depth+1, 2*node_number+2)

    def saveImage(self, width=1000, height=800):
        im   = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(im)
        size = 50
        # font = ImageFont.truetype("FreeSans.ttf", int(size/2))
        font = ImageFont.load_default()
        self.drawNode(draw, font, size, self.root, 1, 0)
        im.save("bst.jpg")
