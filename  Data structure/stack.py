from typing import Any


class Stack:
    """Stack"""
    def __init__(self):
        """
        Initialize _items: list
        """
        self._items = list()

    def append(self, item) -> None:
        """
        Add item to stack
        :param item: adding item
        :return: None
        """
        self._items.append(item)

    def get(self) -> Any:
        """
        Get last item in stack
        :return: Any
        """
        if len(self._items) == 0:
            return None
        return self._items.pop()

    def __str__(self) -> str:
        """
        Convert Stack to str
        :return: str
        """
        return str(self._items)
