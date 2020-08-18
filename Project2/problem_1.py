# use an OrderedDict
# which remembers insertion order
# we can change that order to keep track of
# each values usage

from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = OrderedDict() #a dict, which is a hashmap

    def get(self, key):
        if self.capacity == 0:
            raise Exception("Sorry, cannot perform actions on empty cache")
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        if self.capacity == 0:
            raise Exception("Sorry, cannot perform actions on empty cache")

        if len(self.cache) + 1 > self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
        self.cache.move_to_end(key, last=True)

our_cache = LRU_Cache(4)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))    # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)
print(len(our_cache.cache))  # returns 4
print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

a_new_cache = LRU_Cache(0) # no capacity
a_new_cache.set(1, 1) # raises an exception
