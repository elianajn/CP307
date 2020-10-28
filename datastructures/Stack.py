from . LinkedList import LinkedList

class Stack:
    def __init__(self):
        # self.current_size = 0
        self.stack = LinkedList()
        self.current_size = 0

    def size(self):
        return self.current_size

    def push(self, data):
        self.stack.add(data)
        self.current_size += 1

    def pop(self):
        if self.current_size == 0:
            raise IndexError("Stack is empty")
        top = self.stack[self.current_size-1]
        self.stack.delete(self.current_size-1)
        self.current_size -= 1
        return top

    def peek(self):
        top = self.stack[self.current_size-1]
        return top


def main():
    s = Stack()
    s.push("pumbaa")
    s.push("rafi")
    s.push("zazu")
    print(s.size())
    result = s.pop()
    print(result)
    print(s.size())

if __name__ == "__main__":
    main()
