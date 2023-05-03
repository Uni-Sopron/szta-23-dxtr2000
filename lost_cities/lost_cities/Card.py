class Card:
    def __init__(self, color: str, value: int):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color.capitalize()} {self.value}"
    def __repr__(self):
        return f"{self.color} {self.value}"