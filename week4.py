from typing import override
import random

class CircularStack:
    def __init__(self, cap: int = 5, start_pos: int = 0):
        assert cap > start_pos and cap >= 0, "yang benar aja bro..."

        self.cap: int  = cap
        self.sptr: int = start_pos
        self.bptr: int = -1
        self.data: list[int | None] = [None] * self.cap

    def is_empty(self) -> bool:
        return self.bptr == -1

    def is_full(self) -> bool:
        if self.is_empty():
            return False

        if self.bptr < self.sptr:
            return self.bptr + 1 >= self.sptr

        if self.bptr == self.sptr:
            return False

        if self.bptr < self.cap - 1:
            return False

        if self.sptr > 0:
            return False

        return True

    def peek(self) -> int | None:
        if self.is_empty():
            return None
        return self.data[self.bptr]

    def pop(self) -> int | None:
        data = self.peek()
        if data is None:
            return None

        self.data[self.bptr] = None
        if self.bptr - 1 >= 0:
            self.bptr -= 1
        else:
            self.bptr = self.cap - 1
        return data

    def clear(self):
        for i in range(0, self.cap):
            self.data[i] = None
        self.bptr = -1

    def push(self, data: int):
        if self.is_full():
            print("ERR: Stack is full")
            return

        if self.bptr <= -1:
            self.bptr = self.sptr
        else:
            self.bptr = (self.bptr + 1) % self.cap
        self.data[self.bptr] = data

    @override
    def __str__(self) -> str:
        builder = f"{self.data}"
        if self.is_empty():
            return "Empty."
        return builder

if __name__ == "__main__":
    size = 5
    start_at = random.randint(0, size - 1)
    s = CircularStack(size, start_at)
    while True:
        print(
'''\
(P) Print stack
(A) Add elm to stack
(D) Del stack elm
(E) Peek stack elm
(C) Clear stack
(Q) Exit\
'''
        )
        opt = input("Chooice : ").capitalize()
        if opt == "P":
            print(s)
        elif opt == "A":
            opt2 = input("  Enter data (int) : ")
            if opt2.isdigit():
                opt2 = int(opt2)
                s.push(opt2)
        elif opt == "D":
            s.pop()
        elif opt == "E":
            data = s.peek()
            if data is not None:
                print(data)
            else:
                print("Empty")
        elif opt == "C":
            s.clear()
        elif opt == "Q":
            exit(69)
        else:
            print("ERR: Not a valid chooice!")
            continue
