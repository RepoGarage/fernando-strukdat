from typing import override

class Stack:
    def __init__(self, cap: int = 5):
        self.m_cap: int = cap
        self.m_data: list[int] = []

    def push(self, data: int):
        if self.m_cap <= len(self.m_data) + 1:
            print("INFO: stack full!")
            # to grow disabled
            # self.m_cap = self.m_cap * 2
            return
        self.m_data.append(data)

    def pop(self) -> int | None:
        if len(self.m_data) <= 0:
            print("INFO: stack kosong!")
            return None
        data: int = self.m_data[-1]
        del self.m_data[-1]
        return data

    def clear(self):
        del self.m_data[0:len(self.m_data)]

    def peek(self) -> int | None:
        if len(self.m_data) <= 0:
            print("INFO: stack kosong!")
            return None
        return self.m_data[-1]

    @override
    def __str__(self) -> str:
        if len(self.m_data) <= 0:
            return "Empty."
        builder: str = ""
        for i in range(0, len(self.m_data)):
            builder += f"{i}. {self.m_data[i]}\n"
        return builder

if __name__ == "__main__":
    s: Stack = Stack(5)
    running: bool = True

    print('''\
    [INFO: Capacity is 5]
    1. Push new data
    2. Pop data
    3. Print data
    4. clear data
    5. Peek data
    6. exit''')
    while running:
        option = int(input("Please give chooice : "))
        if option == 1:
            opt2 = int(input("  What to push : "))
            s.push(opt2)
        elif option == 2:
            _ = s.pop()
        elif option == 3:
            print(s)
        elif option == 4:
            s.clear()
        elif option == 5:
            data = s.peek()
            if data is not None:
                print(f"the data is : {data}")
        else:
            exit(1)
