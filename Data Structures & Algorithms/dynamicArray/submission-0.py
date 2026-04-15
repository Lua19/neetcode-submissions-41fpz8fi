class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # Initialize the array with 'capacity' number of slots
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        # Per instructions, assume index i is valid
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # Per instructions, assume index i is valid
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # If the array is full, double the capacity before adding
        if self.size == self.capacity:
            self.resize()
        
        # Insert at the next available 'size' index, then increment
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # Reduce size first; the element at self.size is now effectively "removed"
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        # 1. Double the capacity
        self.capacity = self.capacity * 2
        # 2. Create a new physical list with the new capacity
        new_arr = [0] * self.capacity
        # 3. Copy elements from the old list to the new list
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        # 4. Update the reference to the new list
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity