class jar:
    def __init__(self, capacity = 12):
        if capacity < 0:
            raise ValueError("Boss jar can't have negative capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Boss, you can't put that many cookies in the jar!")
        self._size += n
        pass

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Boss, you can't take that many cookies out of the jar!")
        self._size -= n
        pass

    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self._size
    
