"""This defines the creation of a linkedList"""

class linkedList():
    """linkedList class"""
    class element():
        """declaration of element class"""
        def __init__(self, data=None, point=None):
            self._point = point
            self._data = data
    def __init__(self):
        """"initialization of the linkedList"""
        self._head = None
        self._size = 0
        self.element(data=0, point=0)
    def insert(self):
        """inserts into the linked list"""
        self.elem = self.element(data=input)
        self.elem._point = self._head
        self._head = self.elem
        self._size += 1
        return self.elem

    def top(self):
        """this returns the topmost item in a list"""
        return self._head
    def size(self):
        """returns the size of the linked list"""
        return self._size
    def delete(self):
        """deletes an element in a linked list"""
        self._head = self._point
        self._point = None
        self._head = None
        self._size -= 1
