import sys
from collections import defaultdict
import heapq

class HuffmanNode(object):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __gt__(self, other):
        if not other or not isinstance(other, HuffmanNode):
            return -1
        return self.freq > other.freq

class HuffmanEncoder(object):

    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    def make_frequency_dict(self, text):
        frequency = defaultdict(int)
        for char in text:
            frequency[char] += 1
        return frequency

    def make_heap(self, frequency_dict):
        for key, value in frequency_dict.items():
            new_node = HuffmanNode(key, value)
            heapq.heappush(self.heap, new_node)

    def merge_nodes(self):
        if len(self.heap) == 1: #explicitly handle the case where the heap size is 1
            node = heapq.heappop(self.heap)
            node1 = HuffmanNode(None, node.freq)
            node1.left = node
            heapq.heappush(self.heap, node1)
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = HuffmanNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)

    def make_codes_recursive(self, root, current_code):
        if (root == None):
            return

        if (root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return

        self.make_codes_recursive(root.left, current_code + "0")
        self.make_codes_recursive(root.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        self.make_codes_recursive(root, "")

    def get_encoded_text(self, text):
        text_encoded = ""
        for char in text:
            text_encoded += self.codes[char]
        return text_encoded

    def encode(self, data):
        frequency_dict = self.make_frequency_dict(data)
        self.make_heap(frequency_dict)
        self.merge_nodes()
        tree = heapq.nlargest(1, self.heap)[0] # take the top value without removing
        self.make_codes()
        text_encoded = self.get_encoded_text(data)
        return text_encoded, tree

    def decode(self, data, tree):
        decoded_data = ""
        current_node = tree

        for char in data:
            current_node = current_node.left if char == '0' else current_node.right
            if current_node.char is not None:
                decoded_data += current_node.char
                current_node = tree
        return decoded_data

if __name__ == "__main__":

    print("Test 1")
    print("-------------")
    encoder_test_1 = HuffmanEncoder()
    test_sentence = "The bird is the word"
    print ("The size of the data is: {}".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))
    encoded_data, tree = encoder_test_1.encode(test_sentence)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = encoder_test_1.decode(encoded_data, tree)
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("Test 2")
    print("-------------")
    encoder_test_2 = HuffmanEncoder()
    test_sentence = "a *word*#, anoth__er word, one last CAPITAL WORD."
    print ("The size of the data is: {}".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))
    encoded_data, tree = encoder_test_2.encode(test_sentence)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = encoder_test_2.decode(encoded_data, tree)
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("Test 3")
    print("-------------")
    encoder_test_3 = HuffmanEncoder()
    test_sentence = "aaaaaaA"
    print ("The size of the data is: {}".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))
    encoded_data, tree = encoder_test_3.encode(test_sentence)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = encoder_test_3.decode(encoded_data, tree)
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("Test 4")
    print("-------------")
    encoder_test_4 = HuffmanEncoder()
    test_sentence = "aaaaaa"
    print ("The size of the data is: {}".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))
    encoded_data, tree = encoder_test_4.encode(test_sentence)
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = encoder_test_4.decode(encoded_data, tree)
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
