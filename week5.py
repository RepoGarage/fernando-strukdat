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

    def print_list(self) -> str:
        builder = ""
        current = self
        while current is not None:
            builder += str(current.data) + " -> "
            current = current.next
        builder += "FULL CAPPED"
        return builder

# using LinkedList to make pop or dequeue easier
class Queue:
    def __init__(self, cap: int):
        self.cap = cap
        self.data: LinkedList | None = None
        self.len = 0

    def enqueue(self, data: int):
        if self.is_full():
            print("ERR: Queue is full")
            return
        if self.data is not None:
            self.data.append(LinkedList(data))
        else:
            self.data = LinkedList(data)
        self.len += 1

    def dequeue(self):
        if self.is_empty() == False:
            copy = self.data
            # to make lsp happy but not needed
            if self.data is not None:
                self.data = self.data.next
            self.len -= 1
            return copy

    def is_full(self) -> bool:
        return self.len + 1 > self.cap

    def is_empty(self):
        return self.len <= 0 and self.data is None

    def clear(self):
        self.data = None
        self.len = 0

    @override
    def __str__(self) -> str:
        builder = ""
        current = self.data
        for _ in range(0, self.cap):
            if current is not None:
                builder += str(current.data) + " -> "
                current = current.next
            else:
                builder += "None -> "
        # if self.data is not None:
        #     builder = self.data.print_list()
        builder += "FULL CAPPED"
        return builder

if __name__ == "__main__":
    q = Queue(3)
    while True:
        print(
'''\
1. Masukkan data ke Queue
2. Keluarkan 1 data dari Queue
3. Check Queue penuh
4. Check Queue kosong
5. Print Queue\
'''
        )
        opt = input("Masukkan input : ")
        if opt == "1":
            opt2 = input("  Data yang mau dimasukkan (int): ")
            if opt2.isnumeric():
                opt2 = int(opt2)
                q.enqueue(opt2)
        elif opt == "2":
            q.dequeue()
        elif opt == "3":
            if q.is_full():
                print("INFO: Queue is full")
            else:
                print("INFO: Queue is not full")
        elif opt == "4":
            if q.is_empty():
                print("INFO: Queue is empty")
            else:
                print("INFO: Queue is not empty")
        elif opt == "5":
            print(q)
        else:
            exit(69)
