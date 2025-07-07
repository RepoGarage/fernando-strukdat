from typing import override

class DoubleStack:
    def __init__(self, cap: int = 5):
        self.m_len: int = cap
        self.m_data: list[int | None] = [None] * cap
        self.m_lptr: int = -1
        self.m_rptr: int = cap

    def _check_full(self) -> bool:
        if self.m_lptr + 1 == self.m_rptr:
            return True
        return False

    def _check_empty(self) -> bool:
        if self.m_lptr == -1 and self.m_rptr == self.m_len:
            return True
        return False

    def push(self, data:int, ptr: int):
        push_to = None
        if ptr == 0:
            self.m_lptr += 1
            push_to = self.m_lptr
        elif ptr == 1:
            self.m_rptr -= 1
            push_to = self.m_rptr
        if push_to is not None:
            if self._check_full():
                print("ERR: Stack full!")
                if ptr == 0:
                    self.m_lptr -= 1
                elif ptr == 1:
                    self.m_rptr += 1
                return

            self.m_data[push_to] = data

    def pop(self, ptr: int) -> int | None:
        push_to = None
        if ptr == 0:
            push_to = self.m_lptr
            self.m_lptr -= 1
        elif ptr == 1:
            push_to = self.m_rptr
            self.m_rptr += 1
        if push_to is not None:
            if self._check_empty():
                print("ERR: Stack empty!")
                if ptr == 0:
                    self.m_lptr += 1
                elif ptr == 1:
                    self.m_rptr -= 1
                return None

            data = self.m_data[push_to]
            self.m_data[push_to] = None
            return data
        return None

    def peek(self, ptr: int) -> int | None:
        if ptr == 0:
            if self.m_lptr < 0:
                return None
            return self.m_data[self.m_lptr]
        elif ptr == 1:
            if self.m_rptr >= self.m_len:
                return None
            return self.m_data[self.m_rptr]
        else:
            return None

    def clear(self, ptr: int):
        if ptr == 0:
            for i in range (0, self.m_lptr):
                self.m_data[i] = None
            self.m_lptr = -1
        elif ptr == 1:
            for i in range (self.m_rptr, self.m_len):
                self.m_data[i] = None
            self.m_rptr = self.m_len
        elif ptr == 2:
            for i in range (0, self.m_len):
                self.m_data[i] = None
            self.m_lptr = -1
            self.m_rptr = self.m_len

    @override
    def __str__(self) -> str:
        if self.m_lptr <= -1 and self.m_rptr >= self.m_len:
            return "Empty"

        builder = "["
        for i in range(0, self.m_lptr + 1):
            builder += f" {self.m_data[i]}"
        builder += " | "
        for i in range(self.m_rptr, self.m_len):
            builder += f"{self.m_data[i]} "
        builder += "]"
        return builder

if __name__ == "__main__":
    stack = DoubleStack(10)

    for i in range(0, 7):
        stack.push(i, 0)

    for i in range(0, 2):
        stack.push(i, 1)

    while True:
        print(
'''\
1. Print DoubleStack
2. Push new elm
3. Pop elm
4. Peek elm
5. Clear elm\
'''
        )
        try:
            opt: int = int(input("Chooice : "))
            if opt == 1:
                print(stack)
            elif opt == 2:
                print("(0)Stack1 or (1)Stack2")
                opt2: int = int(input("  Pick Stack : "))
                if opt2 < 0 or opt2 > 1:
                    print("ERR: Not valid!")
                    continue
                opt3: int = int(input("  Input Data : "))
                stack.push(opt3, opt2)
            elif opt == 3:
                print("(0)Stack1 or (1)Stack2")
                opt2: int = int(input("  Pick Stack : "))
                if opt2 < 0 or opt2 > 1:
                    print("ERR: Not valid!")
                    continue
                stack.pop(opt2)
            elif opt == 4:
                print("(0)Stack1 or (1)Stack2")
                opt2: int = int(input("  Pick Stack : "))
                if opt2 < 0 or opt2 > 1:
                    print("ERR: Not valid!")
                    continue
                val = stack.peek(opt2)
                if val is not None:
                    print(f"    val : {val}")
                else:
                    print("ERR: Cant peek stack empty")
            elif opt == 5:
                print("(0)Stack1 or (1)Stack2")
                opt2: int = int(input("  Pick Stack : "))
                if opt2 < 0 or opt2 > 2:
                    print("ERR: Not valid!")
                    continue
                stack.clear(opt2)
            else:
                exit(0)
        except ValueError:
            print("ERR: Not valid!")
            continue
