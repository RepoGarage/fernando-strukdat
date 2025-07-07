#!/usr/bin/env python

from typing import override

class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def append(self, ll):
        current = self
        while current.next is not None:
            current = current.next
        current.next = ll

class Queue:
    def __init__(self):
        self.len = 0
        self.head = None
        self.tail = None

    def enqueue(self, data: int):
        if self.head is None:
            self.head = LinkedList(data)
            self.tail = self.head
            self.len += 1
        else:
            if self.tail is not None:
                self.tail.next = LinkedList(data)
                self.tail = self.tail.next
                self.len += 1

    def dequeue(self):
        if self.is_empty() == False and self.head is not None:
            self.head = self.head.next
            self.len -= 1

    def is_empty(self) -> bool:
        return self.len <= 0

    def clear(self):
        self.head = None
        self.tail = None
        self.len = 0

    @override
    def __str__(self) -> str:
        builder = ""
        current = self.head
        while current is not None:
            builder += str(current.data) + "->"
            current = current.next
        return builder

class DoubleQueue:
    def __init__(self, cap: int) -> None:
        self.rside = Queue()
        self.lside = Queue()
        self.cap = cap

    def enqueue_wrapper(self, qn: int, data: int):
        if qn > 1 and qn < 0:
            print("ERR: Invalid Queue N input")
            return

        if self.is_full() == True:
            print("ERR: Queue reached the cap.")
            return

        if qn == 0:
            self.lside.enqueue(data)
        else:
            self.rside.enqueue(data)

    def is_full(self) -> bool:
        return self.rside.len + self.lside.len >= self.cap

    @override
    def __str__(self) -> str:
        builder = "["
        lside = []
        rside = []

        current = self.lside.head
        while current is not None:
            lside.append(current.data)
            current = current.next

        current = self.rside.head
        while current is not None:
            rside.append(current.data)
            current = current.next

        for data in lside:
            builder += f"{data}, "

        for data in reversed(rside):
            builder += f"{data}, "

        if builder[len(builder) - 1] == " ":
            builder = builder[:len(builder) -2]

        return builder + "]"


if __name__ == "__main__":
    cap: int = 4
    q = DoubleQueue(cap)
    while True:
        print(
'''

-= DoubleQueue =-
1. Enqueue data
2. Dequeue data
3. Clear queue data
4. Print data
5. Exit\
''')
        opt = input("Please choose : ")
        if opt == "1":
            opt2: str = input("  Choose side Left[0], Right[1]: ")
            if opt2.isnumeric():
                opt2_convert = int(opt2)
                opt3: str = input("    Input Data: ")
                if opt3.isnumeric():
                    opt3_convert = int(opt3)
                    if opt2_convert >= 0 and opt2_convert <= 1:
                        q.enqueue_wrapper(opt2_convert, int(opt3))
                        continue
                    else:
                        print("ERR: Not Valid")
                        continue
                print("ERR: Not Valid")
                continue
        elif opt == "2":
            opt2: str = input("  Choose side Left[0], Right[1]: ")
            if opt2.isnumeric():
                opt2_convert = int(opt2)
                if opt2_convert == 1:
                    q.lside.dequeue()
                elif opt2_convert == 2:
                    q.rside.dequeue()
        elif opt == "3":
            q.rside.clear()
            q.lside.clear()
        elif opt == "4":
            print(q)
        elif opt == "5":
            exit(69)
        else:
            continue
