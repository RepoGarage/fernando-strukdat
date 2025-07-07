class Tree:
    def __init__(self, nama: str, alamat: list = [None]) -> None:
        self.nama: str = nama
        self.alamat: list[Tree | None] = alamat
        pass

    def add_alamat(self, alamat):
        self.alamat.append(alamat)
        pass

    def explore(self):
        print(f" Nama : {self.nama}")
        for i in range(len(self.alamat)):
            current = self.alamat[i]
            if current is not None:
                current.explore()
        pass

if __name__ == "__main__":
    a = Tree("budi")
    b = Tree("simon")
    c = Tree("anton", [a, b])

    c.explore()
    pass
