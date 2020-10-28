from datastructures.Stack import Stack


def main():
    s = Stack()
    s.push("pumbaa")
    s.push("rafi")
    s.push("zazu")
    print(s.size())
    result = s.pop()
    print(result)
    print(s.size())
    s.pop()
    s.pop()
    # print(s.size())
    # s.pop() # correctly throws error


main()
