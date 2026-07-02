#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = height
        self._days = days

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = new_age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._days} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    flower_a = Plant("Rose", 15.0, 10)
    flower_a.show()
    print()
    flower_a.set_height(25.0)
    print("Height updated: 25cm")
    flower_a.set_age(30)
    print("Age updated: 30 days")
    print()
    flower_a.set_height(-10.5)
    flower_a.set_age(-5)
    print()
    print("Current state ", end="")
    flower_a.show()
