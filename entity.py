class ShortStockInfo:
    def __init__(self, id, name) -> None:
        super().__init__()
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return "["+self.id+"]" + self.name
