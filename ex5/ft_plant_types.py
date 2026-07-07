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


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str) -> None:
        super().__init__(name, height, days)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        if self.is_blooming:
            print(f"Color: {self.color}")
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"Color: {self.color}")
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int, nutritional_value: int) -> None:
        super().__init__(name, height, days)
        self.nutritional_value = nutritional_value

    def 



if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower_a = Flower("Rose", 15.0, 10, "red")
    flower_a.show()
    print("[asking the rosa to bloom]")
    flower_a.bloom()
    flower_a.show()
    print()
    print("=== Tree")
    tree_a = Tree("Oak", 200.0, 365, 5)
    tree_a.show()
    print("[asking the oak to produce shade]")
    tree_a.produce_shade()
    print()
    print("=== Vegetable")