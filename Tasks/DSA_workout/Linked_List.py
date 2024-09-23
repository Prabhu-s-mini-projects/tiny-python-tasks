# Dependencies

# CONSTANTS

# Global Parameters

class Node:

    def __init__(self, data, next = None, previous = None):
        self.previous = previous
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self,data=None):
        self.node = Node(data=data) if data is not None else None
        self.head = self.node

        self.node.next = None # No need for this line since Node object by default set this as NONE. Just for understanding

    def append(self,data)-> None:

        # Looping until we reach the end of the list
        while self.node.next:
            self.node = self.node.next

        # Adding a new node at end of the list
        self.node.next = Node(data=data)

        # Bring the pointer back to head
        self.node = self.head

    def print_all_items(self)-> None:

        # Creating a temp node for iterate
        current_node = self.head
        print(f"{current_node.data}")

        # Looping until we reach the end of the list
        while current_node.next:
            current_node = current_node.next
            print(f"{current_node.data}")


class DoubleLinkedList:

    def __init__(self, data=None):
        self.node = Node(data=data) if data is not None else None
        self.head = self.node
        self.tail = self.node

        # No need for this line since Node object by default set this as NONE. Just for understanding
        self.node.next = None
        self.node.previous =None

    def append(self,data)-> None:

        # Looping the end of the list:
        while self.node.next:
            self.node = self.node.next

        # Creating a new node
        new_node = Node(data= data)
        new_node.previous = self.node
        self.node.next = new_node

        self.tail = self.node.next
        self.node = self.head


    def print_head_to_tail(self) -> None:

        # Creating a temp node for iterate
        current_node = self.head
        print(f"{current_node.data}")

        # Looping until we reach the end of the list
        while current_node.next :
            current_node = current_node.next
            print(f"{current_node.data}")

    def print_tail_to_head(self)-> None:

        #Creating temp node
        current_node = self.tail
        print(f"{current_node.data}")

        while current_node.previous:
            current_node = current_node.previous
            print(f"{current_node.data}")

    def insert_before_node(self, data, target_node:Node)->  None:
        """
        Inserts a node before the given node
        :param target_node:
        :return:
        """
        # Making sure first node is not the target_node
        if self.head != target_node:

           # Looping to all the element in the list
            while self.node.next:
                #self.node =  self.node.next

                # Making checking current node is target node
                if self.node.next == target_node:

                    # Creating a new node
                    new_node = Node(data=data)

                    # Assigning previous and next of target node to newly created node
                    new_node.previous = self.node
                    new_node.next = self.node.next

                    # Updating the current node chain
                    self.node.previous = new_node

                    break
def print_in_box(text)-> None:

    # Calculate the width of the box
    width = len(text) + 4  # 2 spaces on each side + 2 for the borders
    print('+' + '-' * (width - 2) + '+')  # Top border
    print('| ' + text + ' |')  # Text line
    print('+' + '-' * (width - 2) + '+')  # Bottom border

def main()-> None:
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
