class Student:
    def __init__(self, name, sector):
        self.name = name
        self.sector = sector

    def __str__(self):
        return f"{self.name}: {self.sector}"
