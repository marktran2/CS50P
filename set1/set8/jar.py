class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if self._size + n > self.capacity:
            raise ValueError("Exceeded max capacity")
        else:
            self._size += n
    
    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Insufficient cookies to take from")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError("Negative capacity")
        self._capacity = n

    @property
    def size(self):
        return self._size