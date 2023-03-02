class Player:
    score: int = 0
    sign: str

    def __init__(self, name: str, is_computer: bool = False) -> None:
        self.name = name
        self.is_computer = is_computer
