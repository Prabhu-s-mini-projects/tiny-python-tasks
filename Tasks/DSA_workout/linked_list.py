""" The Script contains the implementation one of Data structure (Linked list)"""


class Node:
    """Contains that holds data and next pointer"""

    def __init__(self, data, pointer_next=None, previous=None):
        self.previous = previous
        self.data = data
        self.p_next = pointer_next

    def print_node_data(self) -> None:
        """print: node value"""
        print(f"{ self.data = } ")

    def print_next_node(self) -> None:
        """print Next node"""
        print(f"{ self.p_next = } ")


class LinkedList:
    """ Class of singly LINKED LIST data structure"""

    def __init__(self,data=None):
        self.node = Node(data=data) if data is not None else None
        self.head = self.node
        self.tail = self.node
        # No need for this line since Node object by default set this as NONE.
        # Just for understanding
        self.node.p_next = None
        self.length = 1

    def append(self, data: object) -> None:
        """ add a new element into a list"""
        # Creates a new node
        new_node = Node(data)

        # Makes the tail end of the list to point to new node
        self.tail.p_next = new_node

        # Moves the tail pointer to a new node
        self.tail = new_node

        # Increment length of the list by 1
        self.length += 1

    def print_all_items(self)-> None:
        """ Print all the elements in the list of the same order"""

        # Creating a temp node for iterating
        temp_pointer = self.head

        # Looping until we reach the end of the list
        while temp_pointer:
            print(f"{temp_pointer.data}")
            temp_pointer = temp_pointer.p_next

    def pop(self) -> Node | None:
        """Removes the last element from the list"""

        # Covers the scenario when there is no node in a list
        if self.length == 0:
            return None

        # for scenario with multiple Nodes
        # creates a temp pointer
        temp_p = self.head
        pre_p = self.head

        # Traverse one by one until None
        while temp_p.p_next is not None:
            pre_p = temp_p
            temp_p = temp_p.p_next

        # Marks the pre-pointer as tail
        self.tail = pre_p
        self.tail.p_next = None  # Marks the end of the list

        # Decrease the length by 1
        self.length -= 1

        # for scenario where length of node was 1
        if self.length == 0:
            self.head = None
            self.tail = None

        # Returns the pop node
        return temp_p

    def prepend(self, data: object) -> None:
        """add a node in the front of a list"""
        # Creates a New Node
        new_node = Node(data)

        # Marks the next to be current head
        new_node.p_next = self.head

        # Moves the heads to the new node
        self.head = new_node

        # Increments the list by 1
        self.length += 1

        # Covers the scenario when no node was there before
        if self.length == 1:
            self.tail = new_node

    def pop_first(self) -> Node | None:
        """Removes the first element in the list"""
        # Covers the scenario when no node in a list
        if self.length == 0:
            return None

        # For Multiples nodes:
        # Creates a temp pointer
        temp = self.head

        # Moves the head pointer to the next node
        self.head = self.head.p_next

        # Remove the temp from the list
        temp.p_next = None

        # Decrement the count by 1
        self.length -= 1

        # For scenario when there was only one Node
        if self.length == 0:
            # self.head = None[not required:covers as part of this self.head = self.head.p_next]
            self.tail = None

        return temp

    def get(self, index: int) -> Node | None:
        """returns the element at the given index """

        # Covers the scenario for negative index and higher than length
        if not 0 <= index <= self.length:
            return None

        # To track the index
        temp = self.head

        # Moves the pointer the index
        for _ in range(index):
            temp = temp.p_next

        return temp

    def set_value(self, index: int, data: object) -> bool:
        """ set the object at a given index"""

        # Using get-method to return the Node at a given index
        temp = self.get(index=index)

        # If the return is valid
        if temp:
            # updates the values
            temp.data = data
            return True

        return False

    def insert(self, index: int, data: object) -> bool | None:
        """Adds a new node to list at a given index"""

        # Creates a new node
        new_node = Node(data)

        # Check for valid index
        if not 0 <= index <= self.length:
            return False

        # To add at the starting
        if index == 0:
            return self.prepend(data)

        # To add at the end
        if index == self.length:
            return self.append(data)

        # Returns the node at the given index-1
        temp = self.get(index - 1)

        # Map the new node next to Temp nodes next
        new_node.p_next = temp.p_next

        # Maps the index-1 node to new node
        temp.p_next = new_node  # [Now at the given index new node added]

        # Increments the method by 1
        self.length += 1

        return True

    def remove(self, index: int) -> Node | None:
        """ removes a node at a given index"""

        # Check for valid index
        if not 0 <= index <= self.length:
            return None

        # To add at the starting
        if index == 0:
            return self.pop_first()

        # To add at the end
        if index == self.length:
            return self.pop()

        # Get to Node before the node to be removed
        temp = self.get(index - 1)

        # Gets the remove node
        remove_node = temp.p_next

        # Links the before next to remove_nodes next
        temp.p_next = remove_node.p_next

        # Detaches the node from the list
        remove_node.p_next = None

        # Decrements the count by 1
        self.length -= 1

        return remove_node

    def reverse(self) -> None:
        """ reverse the linked list"""
        # Swap head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # Need 3 variables to reverse the link
        before = None
        # after = temp.p_next [will be declared inside a loop]
        # temp = self.head [already declared]

        # Traverse element one by one
        for _ in range(self.length):
            # Move after a pointer to temp.next
            after = temp.p_next

            # Reversing the link
            temp.p_next = before

            # Move the before pointer to temp
            before = temp

            # Move the temp pointer to after node
            temp = after

class DoubleLinkedList:
    """ Class of Doubly LINKED LIST data structure"""

    def __init__(self, data=None):
        self.node = Node(data=data) if data is not None else None
        self.head = self.node
        self.tail = self.node

        # No need for this line since Node object by default set this as NONE.
        # Just for understanding
        self.node.p_next = None
        self.node.previous =None

        # Defining length
        self.length = 1

    def append(self, data: object) -> None:
        """ add a new element into a list"""

        # Creating a new node
        new_node = Node(data= data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # Moves the tail next to new node(sets the link)
        self.tail.p_next = new_node

        # Moves the nodes prev to tail (sets the reverse link)
        new_node.previous = self.tail

        # Moves the tail to New node(marks the new tail)
        self.tail = new_node

        # Increments the length by 1
        self.length += 1

    def pop(self) -> Node | None:
        """ will return the last element"""
        # for an empty list
        if self.length == 0:
            return None

        # for one or more nodes list
        pop_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            # Moves the tail one node back
            self.tail = pop_node.previous

            # Disconnect the tail link
            self.tail.p_next = None

            # Disconnects the reverse link
            pop_node.previous = None

        # Decrements the length
        self.length -= 1

        return pop_node

    def prepend(self, data: object) -> None:
        """ will add to the start of the list"""

        # Creates a new Node
        new_node = Node(data)

        # for an empty list
        if self.length == 0:

            self.head = self.tail = new_node

        else:  # when one or node present

            # Establishing the link (Connects New node next to head)
            new_node.p_next = self.head

            # Establish the reverse link (Connects head prev to new node)
            self.head.previous = new_node

            # Moves the head to the new node
            self.head = new_node

        # Increments the length by 1
        self.length += 1

    def pop_first(self) -> Node | None:
        """will return the first element"""

        # Covers empty list scenario
        if self.length == 0:
            return None

        # Takes the pop node
        pop_node = self.head

        # for list with one node
        if self.length == 1:
            self.head = self.tail = None
        else:
            # for 2 or more nodes
            self.head = pop_node.p_next

            # Disconnects the link
            pop_node.p_next = None
            self.head.previous = None

        self.length -= 1

        return pop_node

    def get(self, index_: int) -> Node | None:
        """return the node at a given index"""
        if not 0 <= index_ < self.length:
            return None

        if index_ < self.length / 2:
            temp = self.head
            for _ in range(index_):
                temp = temp.p_next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index_, -1):
                temp = temp.previous

        return temp

    def set_value(self, index_: int, data: object) -> None:
        """ will set the value at a given node"""
        temp = self.get(index_)

        if temp:
            temp.data = data

    def insert(self, index_: int, data: object) -> None:
        """ will add a node at a given index"""
        temp = self.get(index_)

        if index_ == 0:
            self.prepend(data)
        if index_ == self.length - 1:
            self.append(data)
        else:
            new_node = Node(data)
            # Get the previous node
            prev_node = temp.previous

            # Disconnect and re-establish the new link prev
            prev_node.p_next = new_node

            # establish the reverse link on a new node
            new_node.previous = prev_node

            # Disconnect and re-establish the reverse link of temp node
            temp.previous = new_node

            # Establishing the link for the new node
            new_node.p_next = temp

            self.length += 1

    def remove(self, index_: int) -> Node | None:
        """ will return the element at a given index"""
        if index_ == 0:
            return self.pop_first()
        if index_ == self.length - 1:
            return self.pop()
        temp = self.get(index_)

        if temp:
            before = temp.previous
            after = temp.p_next
            before.p_next = after
            after.previous = before
            temp.p_next = temp.previous = None
            self.length -= 1
            return temp

        return None

def print_in_box(text)-> None:
    """To display a list as per the understanding logical image format"""

    # Calculate the width of the box
    width = len(text) + 4  # 2 spaces on each side + 2 for the borders
    print('+' + '-' * (width - 2) + '+')  # Top border
    print('| ' + text + ' |')  # Text line
    print('+' + '-' * (width - 2) + '+')  # Bottom border

def main()-> None:
    """Contains the main loop of a program"""
    new_linked_list = LinkedList(data=5)
    new_linked_list.append(6)
    new_linked_list.append(7)
    new_linked_list.append(8)
    new_linked_list.append(9)
    new_linked_list.append(10)

    new_double_linked_list = DoubleLinkedList(data='a')
    new_double_linked_list.append(data='b')
    new_double_linked_list.append(data='c')
    new_double_linked_list.append(data='d')
    new_double_linked_list.append(data='e')

    data = new_double_linked_list.get(2).data
    print_in_box(str(data))

    new_double_linked_list.set_value(2, data=23)
    data = new_double_linked_list.get(2).data

    print_in_box(str(data))

if __name__ == '__main__':
    main()
