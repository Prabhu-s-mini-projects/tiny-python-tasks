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
            print(f"{temp_pointer.sheet_data}")
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

        self.length -= 1

        return remove_node

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

    def append(self,data)-> None:
        """ add a new element into a list"""

        # Looping the end of the list:
        while self.node.p_next:
            self.node = self.node.p_next

        # Creating a new node
        new_node = Node(data= data)
        new_node.previous = self.node
        self.node.p_next = new_node

        self.tail = self.node.p_next
        self.node = self.head


    def print_head_to_tail(self) -> None:
        """Print all the elements form head to tail"""

        # Creating a temp node for iterating
        current_node = self.head
        print(f"{current_node.data}")

        # Looping until we reach the end of the list
        while current_node.p_next:
            current_node = current_node.p_next
            print(f"{current_node.sheet_data}")

    def print_tail_to_head(self)-> None:
        """print all the elements from tail to head"""

        #Creating temp node
        current_node = self.tail
        print(f"{current_node.data}")

        while current_node.previous:
            current_node = current_node.previous
            print(f"{current_node.sheet_data}")

    def insert_before_node(self, data, target_node:Node)->  None:
        """
        Inserts a node before the given node
        :param data:
        :param target_node:
        :return:
        """
        # Making sure the first node is not the target_node
        if self.head != target_node:

            # Looping to all the element in the list
            while self.node.p_next:

                #self.node =  self.node.next

                # Making checking current node is target node
                if self.node.p_next == target_node:

                    # Creating a new node
                    new_node = Node(data=data)

                    # Assigning previous and next of target node to newly created node
                    new_node.previous = self.node
                    new_node.p_next = self.node.p_next

                    # Updating the current node chain
                    self.node.previous = new_node

                    break


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
    new_linked_list.print_all_items()

    new_double_linked_list = DoubleLinkedList(data=1)
    new_double_linked_list.append(data=2)
    new_double_linked_list.append(data=3)
    new_double_linked_list.append(data=4)
    new_double_linked_list.append(data=5)
    new_double_linked_list.print_head_to_tail()
    new_double_linked_list.print_tail_to_head()

    data =5
    print(" ______")
    print(f"|   {data}  |")
    print("|______|")

    print_in_box("5")

if __name__ == '__main__':
    main()
