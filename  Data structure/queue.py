from typing import Any


class Item:

    def __init__(self, obj):
        self.obj = obj
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.obj)


class Queue:

    def __init__(self):
        """
        Init first and last in queue
        """
        self.first = None
        self.last = None

    def append(self, item: Any) -> None:
        """
        Add item to queue
        :param item: Adding item to queue
        :return: None
        """
        item = Item(item)
        if not self.first:
            self.first = self.last = item
            return
        self.last.next = item
        item.prev = self.last
        self.last = item

    def get(self) -> None:
        """
        Get First item in queue
        :return: Item: first item
        """
        self.first, item = self.first.next, self.first
        return item

    def get_reverse(self) -> None:
        """
        Get Last item in queue
        :return: Item: last item
        """
        self.last, get_item = self.last.prev, self.last
        return get_item
