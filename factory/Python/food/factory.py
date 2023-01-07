#!/usr/bin/env python3
"""The Factory Patterns is creational."""


from abc import ABC


# Suppose we have different sorts of food.


class Food(ABC):
    """Abstract food class."""

    def __init__(
        self,
        description: str,
    ):
        self._desc = description

    @property
    def desc(self) -> dict[str, str]:
        return {
            "desc": self._desc,
        }


class Egg(Food):
    """Eggs are food."""


class Spam(Food):
    """Spam are food."""


# Now the factory itself


class FoodFactoryError(Exception):
    """Factory base exception class."""


class FoodFactory:
    """Our food factory is an old brand."""

    @classmethod
    def create(cls, food_name: str, *args, **kwargs):
        fname: str = food_name.lower()
        # here Pythonic `__name__` feature is not favourable.
        if fname == "food":
            # see what will happen and explain why
            return Food("food")
        if fname == "spam":
            return Spam("can")
        elif fname == "egg":
            return Egg("fly")
        else:
            raise FoodFactoryError(
                f"cannot create {food_name} class."
            )


if __name__ == "__main__":
    kls_name = input("Please enter the food [sub]class name: ")
    obj = FoodFactory.create(kls_name)
    print(f"Description: {obj.desc}")
