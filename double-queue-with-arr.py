#!/usr/bin/env python
from typing import override

class DoubleQueue:
    def __init__(self, cap: int) -> None:
        self.cap: int               = cap
        self.data: list[None | int] = [None] * self.cap
        self.ltail: int             = -1
        self.rtail: int             = self.cap

    def enqueue(self, pos: int, data: int):
        if pos in [1, 2]:
            if self.is_full():
                print("ERR: DoubleQueue is full.")
                return
            if pos == 1:
                self.ltail += 1
                self.data[self.ltail] = data
            else:
                self.rtail -= 1
                self.data[self.rtail] = data
        else:
            print("ERR: Not a valid pos.")
            return

    def dequeue(self, pos: int):
        if pos in [1, 2]:
            if self.is_empty():
                print("ERR: DoubleQueue is empty.")
                return
            if pos == 1:
                for i in range(0, self.ltail):
                    if i+1 == self.rtail:
                        continue
                    self.data[i] = self.data[i+1]
                self.data[self.ltail] = None
                self.ltail = self.ltail - 1
            else:
                for i in range(self.cap - 1, self.rtail - 1, -1):
                    if i - 1 == self.ltail:
                        continue
                    self.data[i] = self.data[i-1]
                self.data[self.rtail] = None
                self.rtail = self.rtail + 1
        else:
            print("ERR: Not a valid pos.")
            return

    def is_full(self) -> bool:
        return self.ltail + 1 == self.rtail

    def is_empty(self) -> bool:
        return self.ltail == 0 and self.rtail == 0

    def clear(self):
        for i in range(0, self.cap):
            self.data[i] = None
        self.ltail = -1
        self.rtail = self.cap

    @override
    def __str__(self) -> str:
        return f"{self.data}"

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
            opt2: str = input("  Choose side Left[1], Right[2]: ")
            if opt2.isnumeric():
                opt2_convert = int(opt2)
                opt3: str = input("    Input Data: ")
                if opt3.isnumeric():
                    opt3_convert = int(opt3)
                    if opt2_convert >= 1 and opt2_convert <= 2:
                        q.enqueue(opt2_convert, int(opt3))
                        continue
                    else:
                        print("ERR: Not Valid")
                        continue
                print("ERR: Not Valid")
                continue
        elif opt == "2":
            opt2: str = input("  Choose side Left[1], Right[2]: ")
            if opt2.isnumeric():
                opt2_convert = int(opt2)
                q.dequeue(opt2_convert)
        elif opt == "3":
            q.clear()
        elif opt == "4":
            print(q)
        elif opt == "5":
            exit(69)
        else:
            continue
