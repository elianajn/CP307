class ListNode:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.current_size = 0

    def size(self):
        return self.current_size

    #Add new item to end of list
    def add(self, data):
        new_node = ListNode(data)
        if self.size() == 0:
            self.first = new_node
            self.last = new_node
        elif self.size() == 1:
            self.last = new_node
            new_node.prev = self.first
            self.first.next = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node

        self.current_size += 1

    #Return item at target index
    def __getitem__(self, target_index):
        curr_index = 0
        curr_node = self.first
        while curr_node != None and curr_index < target_index:
            curr_node = curr_node.next
            curr_index += 1

        if curr_node != None:
            return curr_node.data
        else:
            print("ERROR: ILLEGAL INDEX")
            indexErr = "Index %d out of bounds for list size: %d" % (target_index, self.size())
            raise IndexError(indexErr)


    def delete(self, target_index):
        if target_index == 0 and self.size() > 1:
            self.first.next.prev = None
            self.first = self.first.next
        elif target_index == 0 and self.size() == 1:
            self.first = None
            self.last = None
        elif target_index == self.size() - 1 and self.size() > 1:
            self.last.prev.next = None
            self.last = self.last.prev
        else:
            curr_index = 0
            curr_node = self.first
            while curr_node != None and curr_index < target_index:
                curr_node = curr_node.next
                curr_index += 1

            if curr_node != None:
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
            else:
                raise IndexError("Index %d out of bounds for list size: %d" % (target_index, self.size()))

        self.current_size -= 1

    def __repr__(self):
        result = ""
        curr_node = self.first
        while curr_node != None:
            result += str(curr_node) + ", "
            curr_node = curr_node.next
        return result
