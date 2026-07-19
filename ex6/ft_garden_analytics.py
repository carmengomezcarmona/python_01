#!/usr/bin/env python3

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grow, {self.age_calls} age "
                  f"{self.show_calls} show")

    def __init__(self, name: str, height: float, days: int) -> None:
        self._name = name
        self._height = height
        self._days = days
        self._stats = self._Stats()

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._days} days old")
        self._stats.show_calls += 1

    def age(self) -> None:
        self._days += 1
        self._stats.age_calls += 1

    def grow(self) -> None:
        self._stats.grow_calls += 1

    @staticmethod
    def than_a_year(days: int) -> bool:
        if days > 365:
            return True
        else:
            return False

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._stats.display()


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int,
                 color: str) -> None:
        super().__init__(name, height, days)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def grow(self) -> None:
        super().grow()
        self._height = round(self._height + 8.0, 1)

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self.shade_calls = 0

        def display(self) -> None:
            super().display()
            print(f"{self.shade_calls} shade")

    def __init__(self, name: str, height: float, days: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter
        self._stats: Tree._Stats = self._Stats()

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height}cm "
              f" long and {self.trunk_diameter}cm wide.")
        self._stats.shade_calls += 1

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int,
                 color: str) -> None:
        super().__init__(name, height, days, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def grow(self) -> None:
        super().grow()
        self._height = round(self._height + 22.0, 1)

    def age(self) -> None:
        super().age()
        self._days += 19

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.than_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.than_a_year(400)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)
    print()
    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_plant_stats(anon)
