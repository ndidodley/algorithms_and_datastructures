from DoublyLinkedBase import _DoublyLinkedBase
from Exceptions import Empty


class LinkedDeque(_DoublyLinkedBase):

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")

        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._header, self._header._next)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")

        return self._delete_node(self._trailer._prev)
