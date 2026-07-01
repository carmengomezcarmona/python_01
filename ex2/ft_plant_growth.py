#!/usr/bin/env python3

class Plant:
    def __init__ (self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days
    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")
    def age(self) -> None:
        self.days += 1
    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

if __name__== "__main__":
    print("=== Garden Plant Growth ===")
    flower1 = Plant("Rose", 25.0, 30)
    flower1.show()
    initial_height = flower1.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        flower1.age()
        flower1.grow()
        flower1.show()
    print(f"=== Growth this week: {round(flower1.height - initial_height, 1)}cm ===")
