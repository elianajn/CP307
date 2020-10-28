from datastructures.Queue import Queue

def main():
    q = Queue()
    print(q.isEmpty())
    q.enqueue("bella")
    print(q.peek())
    print(q.isEmpty())
    q.enqueue("nala")
    q.enqueue("palu")
    q.enqueue("puppy")
    q.dequeue()
    result = q.dequeue()
    print(result)

if __name__ == "__main__":
    main()
