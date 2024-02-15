import json
from typing import Iterable

# globals ##############################################################################################################


__FILE_NAME = "values.json"

__knapsack = {}

with open(__FILE_NAME, "r") as f:
    __knapsack = json.load(f)

NUMBER_OF_VALUES = __knapsack["n"]

CAPACITY = __knapsack["capacity"]

TUPLES = tuple(tuple(t) for t in __knapsack["tuples"])

VALUES = [v[1] for v in TUPLES]

WEIGHTS = [v[0] for v in TUPLES]


# classes ##############################################################################################################


class Item:
    weight: int
    value: int
    index: int

    def __init__(self, args):
        self.weight = args[0]
        self.value = args[1]
        self.index = args[2]
        self.__args = args

    def __hash__(self) -> int:
        return self.index

    def __eq__(self, o) -> bool:
        return self.index == o.index

    def __repr__(self) -> str:
        return f"Item-{self.index} (Weight: {self.weight}, Value: {self.value})"

    def __str__(self) -> str:
        return self.__repr__()

    def __getitem__(self, index):
        return self.__args[index]


# methods ##############################################################################################################


def real_profit(items) -> int:
    """
    Gibt den Profit zurück, der durch die Gegenstände in der Liste erzielt wird.
    Wenn das Gewicht der Gegenstände das Fassungsvermögen des Rucksacks überschreitet, wird 0 zurückgegeben.
    """
    if all([isinstance(item, Item) for item in items]):
        _sum = sum([item.value for item in items])
        _weight = sum([item.weight for item in items])
        return _sum if _weight <= CAPACITY else 0
    if not all([0 <= value < NUMBER_OF_VALUES for value in items]):
        raise ValueError(
            f"All values in the list must be between 0 and {NUMBER_OF_VALUES- 1}")
    items = set(items)
    if len(items) != len(items):
        raise ValueError("The list must contain unique values")
    weight = sum([WEIGHTS[i] for i in items])
    if weight > CAPACITY:
        return 0
    return sum([VALUES[i] for i in items])


def profit(items) -> int:
    """
    Gibt den Profit zurück, der durch die Gegenstände in der Liste erzielt wird.
    Dabei wird das Gewicht der Gegenstände nicht berücksichtigt,
    das heißt, der Rucksack darf auch zu schwer werden.
    """
    if all([isinstance(item, Item) for item in items]):
        return sum([item.value for item in items])
    if not all([0 <= value < NUMBER_OF_VALUES for value in items]):
        raise ValueError(
            f"All values in the list must be between 0 and {NUMBER_OF_VALUES- 1}")
    items = set(items)
    if len(items) != len(items):
        raise ValueError("The list must contain unique values")
    return sum([VALUES[i] for i in items])


def weight(items) -> int:
    """
    Gibt das Gewicht der Gegenstände in der Liste zurück.
    """
    if all([isinstance(item, Item) for item in items]):
        return sum([item.weight for item in items])
    if not all([0 <= value < NUMBER_OF_VALUES for value in items]):
        raise ValueError(
            f"All values in the list must be between 0 and {NUMBER_OF_VALUES- 1}")
    items = set(items)
    if len(items) != len(items):
        raise ValueError("The list must contain unique values")
    return sum([WEIGHTS[i] for i in items])


def to_items(iterable: Iterable) -> list:
    """
    Gibt eine Liste von Item-Objekten zurück, die den Gegenständen in der Liste entsprechen.
    """
    return [Item(item) for item in iterable]


def items_to_indexes(iterable: list[Item]) -> list:
    """
    Gibt eine Liste von Indizes zurück, die den Gegenständen in der Liste entsprechen.
    """
    return [item.index for item in iterable]


assert (hash(TUPLES) == -7015908621320116923), "The order, weight or value of at least one of the items has changed"

if __name__ == "__main__":
    ITEMS = to_items(TUPLES)

    assert weight((1, 2, 3)) == weight((ITEMS[1], ITEMS[2], ITEMS[3]))
    assert profit((1, 2, 3)) == profit((ITEMS[1], ITEMS[2], ITEMS[3]))

    assert real_profit((22, 23, 24, 25, 26, 27, 28, NUMBER_OF_VALUES-1)) == 0
    assert real_profit((ITEMS[22], ITEMS[23], ITEMS[24], ITEMS[25], ITEMS[26],
                       ITEMS[27], ITEMS[28], ITEMS[NUMBER_OF_VALUES-1])) == 0

    assert profit((22, 23, 24, 25, 26, 27, 28, NUMBER_OF_VALUES-1)) == profit((
        ITEMS[22], ITEMS[23], ITEMS[24], ITEMS[25], ITEMS[26], ITEMS[27], ITEMS[28], ITEMS[NUMBER_OF_VALUES-1])) > 0
