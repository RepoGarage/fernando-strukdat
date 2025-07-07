class Robot:
    def __init__(self, name: str, version: float):
        self.name: str = name
        self.version: float = version
        self.friend: Robot|None = None
