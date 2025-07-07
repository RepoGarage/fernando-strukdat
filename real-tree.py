#!/usr/bin/env python3

class Tree:
    def __init__(self, val) -> None:
        self.val:  int         = val
        self.left: Tree | None = None
        self.right:Tree | None = None
        return

    def pprint(self, indent = 0) -> None:
        indchar = indent * "  "
        print(f"{indchar}> {self.val}")
        indent += 1
        if self.left is not None:
            self.left.pprint(indent)

        if self.right is not None:
            self.right.pprint(indent)

    def insert(self, data: int) -> None:
        if self.val > data:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.insert(data)


if __name__ == "__main__":
    a = Tree(10)
    a.insert(5)
    a.insert(12)
    a.insert(13)
    a.insert(7)
    a.pprint()
