import hashlib
import time

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.data).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __str__(self):
        return ('Timestamp: {}\nData: {}\nPrevious Hash: {}\nHash: {}\nNext: {}\n'.format(self.timestamp, self.data, self.previous_hash, self.hash, self.next))

class BlockChain:

    def __init__(self):
        self.tail = None #we'll append to the end of the chain

    def append(self, data):
        """
        Append a value to the end of the chain
        """
        timestamp = time.gmtime()
        previous_hash = self.tail.hash if self.tail else None
        new_block = Block(timestamp, data, previous_hash)
        if self.tail:
            self.tail.next = new_block
        self.tail = new_block


my_block_chain = BlockChain()
my_block_chain.append(1)
print(my_block_chain.tail)

my_block_chain.append(99)
print(my_block_chain.tail)

my_block_chain.append(18736)
print(my_block_chain.tail)
