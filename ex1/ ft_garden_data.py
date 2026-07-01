#!/usr/bin/env python3

class Plant:
    def __init__ (self, name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days
    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")

if __name__== "__main__":
    print("=== Garden Plant Registry ===")
    flower1 = Plant("Rose", 25, 30)
    flower2 = Plant("Sunflower", 80, 45)
    flower3 = Plant("Cactus", 15, 120)
    flower1.show()
    flower2.show()
    flower3.show()
