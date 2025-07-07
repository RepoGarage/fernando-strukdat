from typing import override
import random

class CircularQueue:
    def __init__(self, start_at: int, cap: int) -> None:
        self.cap:  int = cap
        self.head: int = start_at
        self.tail: int = self.head
        self.len:  int = 0
        self.data: list[None | int] = [None] * self.cap

    def enqueue(self, data) -> None:

        if self.data[self.tail] is None and self.is_full() is not True:
            self.data[self.tail] = data
            self.tail = (self.tail + 1) % self.cap
            self.len += 1
        else:
            print(f"ERR: Queue is full!")

    def dequeue(self) -> None:
        if self.is_empty():
            print("ERR: Queue is empty!")
            return

        counter = self.head
        for i in range (1, self.cap):
            self.data[counter] = self.data[(self.head + i) % self.cap]
            counter = (counter + 1) % self.cap
        self.data[self.tail - 1] = None
        self.len -= 1

    def is_full(self) -> bool:
        return self.len >= self.cap

    def is_empty(self) -> bool:
        return self.len < 0

    def clear(self):
        for i in range(0, self.cap):
            self.data[i] = None
        self.len = 0
        self.tail = self.head

    @override
    def __str__(self) -> str:
        return f"{self.data}"

if __name__ == "__main__":
    cap = 5
    pos = random.randint(0, cap - 1)
    cq = CircularQueue(pos, cap)

    while True:
        print(
'''

-= CircularQueue =-
1. Enqueue data
2. Dequeue data
3. Clear queue data
4. Print data
5. Exit\
''')
        opt = input("Please choose : ")
        if opt == "1":
            opt2: str = input("    Input Data: ")
            if opt2.isnumeric():
                opt2_convert = int(opt2)
                cq.enqueue(opt2_convert)
        elif opt == "2":
            cq.dequeue()
        elif opt == "3":
            cq.clear()
        elif opt == "4":
            print(cq)
        elif opt == "5":
            exit(69)
        else:
            continue
