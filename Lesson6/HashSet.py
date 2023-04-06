class MyHashSet:  # [0 , 0 , 0 , [10, 11] ]
    def __init__(self):
        self.my_set = [[] for i in range(1000)]

    def contains(self, key) -> bool:
        for elem in self.my_set[self.hash(key)]:
            if elem == key:
                return True
        return False

    def add(self, key) -> None:
        if not self.contains(key):
            self.my_set[self.hash(key)].append(key)

    def remove(self, key) -> None:
        if self.contains(key):
            self.my_set[self.hash(key)].remove(key)

    def hash(self, key):
        return key % 1000 # -> 1 1


myHashSet = MyHashSet()
# print(myHashSet.my_set)
# myHashSet.add(1)
# print(myHashSet.my_set)
# myHashSet.add(2)
# print(myHashSet.my_set)
# print(myHashSet.contains(1))
# print(myHashSet.contains(3))
# myHashSet.add(2)
# print(myHashSet.my_set)
# print(myHashSet.contains(2))
# myHashSet.remove(2)
# print(myHashSet.my_set)
# print(myHashSet.contains(2))
print(myHashSet.my_set)
myHashSet.add(1)
myHashSet.add(1001)
print(myHashSet.my_set)