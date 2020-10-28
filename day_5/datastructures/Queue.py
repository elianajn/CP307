from . LinkedList import LinkedList

class Queue:
    def __init__(self):
        # self.current_size = 0
        self.queue = LinkedList()
        self.current_size = 0

    def isEmpty(self):
        if self.current_size == 0:
            return True
        return False

    def enqueue(self, data):
        self.queue.add(data)
        self.current_size += 1

    def dequeue(self):
        if self.current_size == 0:
            raise IndexError("Queue is empty")
        front = self.queue[0]
        self.queue.delete(0)
        self.current_size -= 1
        return front

    def peek(self):
        front = self.queue[0]
        return front


def main():
    s = Queue()
    s.enqueue("bella")
    s.enqueue("nala")
    s.enqueue("palu")
    s.enqueue("puppy")
    print(s.size())
    result = s.dequeue()
    print(result)
    print(s.size())

if __name__ == "__main__":
    main()
