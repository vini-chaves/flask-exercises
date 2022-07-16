class Node: #this is just the creation of a basic node (box with a data and a pointer)
	def __init__(self, data=None, next_node=None):
		self.data=data
		self.next_node=next_node

class Data: #this class creates the data that goes inside the hash table, oposed of the linked list method where we hard coded the dicts that we needed as we go
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key): #this is the criation of a custom hash value key ... hash table method is faster than linked list when you are trying to find a specific db log
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * ord(i)) % self.table_size #use of the module operator to make sure that the hash value never exeeds the table size, this way we never cal a index outside of the hash table
        return hash_value

    def add_key_value(self, key, value): #this creates a key-value pair to our hash table
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node
            node.next_node = Node(Data(key, value), None)

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            if node.next_node is None:
                return node.data.value
            while node.next_node:
                if key == node.data.key:
                    return node.data.value
                node = node.next_node

            if key == node.data.key:
                return node.data.value
        return None
    def print_table(self):
        print("{")
        for i, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val
                if node.next_node:
                    while node.next_node:
                        llist_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " --> "
                        )
                        node = node.next_node
                    llist_string += (
                        str(node.data.key) + " : " + str(node.data.value) + " --> None"
                    )
                    print(f"    [{i}] {llist_string}")
                else:
                    print(f"    [{i}] {val.data.key} : {val.data.value}")
            else:
                print(f"    [{i}] {val}")
        print("}")

'''
this is just a visualization example of the hash table 
important to note that the custom hash created is not very eficient and can generete conflicts (same hash value to diferent key)
better to implement other function to hash teh table (need to internet serach other formulas)
'''
'''
ht=HashTable(10)
ht.add_key_value("title","there1")
ht.add_key_value("body","there2")
ht.add_key_value("date","there3")
ht.add_key_value("user_id","there4")
ht.print_table()
'''
