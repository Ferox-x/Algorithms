class Item:
    """Node in Linked list"""
    def __init__(self, obj):
        """
        Initialize Item
        self.obj: Any: Any data type.
        self.next_node: Item: link to next node .
        """
        self.obj = obj
        self.next_node = None

    def __str__(self):
        """Convert Item to str"""
        return self.obj


class LinkedList:
    """Linked List"""
    def __init__(self):
        """
        Initialize Linked list
        self.head: Item: First item in linked list, default None
        """
        self.head = None

    def contains(self, item: Item) -> bool:
        """
        Method for detecting the presence of an item in the linked list
        :param item: Item
        :return: bool
        """
        for node in self:
            if node == item:
                return True
        else:
            return False

    def append(self, item: Item) -> None:
        """
        Adds an element to the end of the list
        :param item: Item
        :return: None
        """
        self._check_type(item)
        if self.head:
            last_node = None
            for node in self:
                if node == item:
                    raise ValueError(f'Этот узел уже есть, повторно его добавить нельзя')
                last_node = node
            last_node.next_node = item
            return
        self.head = item

    def get(self, index: int) -> Item:
        """
        Gets an element by index
        :param index: Int
        :return: Item
        """
        if not isinstance(index, int):
            raise IndexError('Index must be type int')
        for index_node, node in enumerate(self):
            if index_node == index:
                return node
        raise IndexError('Index out of range')

    @staticmethod
    def _check_type(item: Item) -> None:
        """
        Check type of item
        :param item: Item
        :return: None
        """
        if not isinstance(item, Item):
            raise TypeError('Object must be of class Item')

    def __iter__(self) -> 'LinkedList':
        """
        Make iterable object
        :return: Linked List
        """
        self._next = self.head
        return self

    def __next__(self) -> Item:
        """
        Get next object
        :return: Item
        """
        current = self._next
        if current:
            self._next = current.next_node
            return current
        else:
            raise StopIteration

    def __str__(self) -> str:
        """
        Format Linked list to str
        :return: str
        """
        string = '['
        for index, item in enumerate(self):
            if index == 0:
                string += str(item)
                continue
            string += ', ' + str(item)
        string += ']'
        return string

    def __add__(self, other) -> 'LinkedList':
        """
        Add item to Linked list
        :param other: Item
        :return: LinkedList
        """
        self._check_type(other)
        self.append(other)
        return self

