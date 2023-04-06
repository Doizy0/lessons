class MyHashMap:

    def __init__(self):
        self.my_map = [None] * (10 ** 6+1)

    def put(self, key: int, value: int) -> None:
        self.my_map[key] = value

    def get(self, key: int) -> int:
        if self.my_map[key] is None:
            return -1
        return self.my_map[key]

    def remove(self, key: int) -> None:
        self.my_map[key]=None
# hash_map = MyHashMap()
# hash_map.remove(2)
# hash_map.put(3,11)
# hash_map.put(4,13)
# hash_map.put(15,6)
# hash_map.put(5,16)
# hash_map.put(8,8)
# hash_map.put(11,0)
# print(hash_map.get(11))
# hash_map.put(1,10)
# hash_map.put(12,14)
