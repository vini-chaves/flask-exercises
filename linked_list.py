class Node: #this is just the creation of a basic node (box with a data and a pointer)
	def __init__(self, data=None, next_node=None):
		self.data=data
		self.next_node=next_node	

class LinkedList: #this is the linked list method
    def __init__(self): #linked list needs a haed to begin. we are keeping trak of the tail of the list to make things easier
        self.head = None
        self.last_node = None

    def to_list(self): #this method returns the linked list for the user to see
        l = []
        if self.head is None:
            return l

        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l

    def print_ll(self): #just some shenanigans to print a linked list (not reevant)
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node

        ll_string += " None"
        print(ll_string)

    def insert_beginning(self, data): #inserting at the beginning ends up changing the haed of teh list
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
            return

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data): #inserting at the end you need to create a node that takes the data and points to None, important to keep trak of the last node
        if self.head is None:
            self.insert_beginning(data)
            return

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def get_user_by_id(self, user_id): #comparing the key "id" from the dict node.data with the user_id that the requets is giving, when found return
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None