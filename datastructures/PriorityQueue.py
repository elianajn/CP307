# from LinkedList import LinkedList
from HashTable import HashTable
import heapq

class PriorityQueue:
    def __init__(self):
        # self.current_size = 0
        # self.queue = LinkedList()
        self.queue = []
        self.dictionary = HashTable()
        heapq.heapify(self.queue)
        self.current_size = 0

    def isEmpty(self):
        if self.current_size == 0:
            return True
        return False

    def enqueue(self, data):
        # self.queue.add(data)
        # heapq.heapify(self.queue)
        score, item = data
        score *= -1 # invert to make a max heap
        heapq.heappush(self.queue, score)
        self.dictionary.put(score, item)
        self.current_size += 1

    def dequeue(self):
        if self.current_size == 0:
            raise IndexError("Queue is empty")
        # front = self.queue[0]
        # self.queue.delete(0)
        top = heapq.heappop(self.queue)
        item = self.dictionary.get(top)
        self.current_size -= 1
        return item

    def peek(self):
        front = self.queue[0]
        return front

    def size(self):
        return self.current_size


def main():
    s = PriorityQueue()
    s.enqueue((1, "hello"))
    s.enqueue((5, "fuck you"))
    s.enqueue((2, "im begging you to work"))
    s.enqueue((9, "cat"))
    print(s.size())
    result = s.dequeue()
    print(result)
    print(s.size())

if __name__ == "__main__":
    main()
