class Node:
    """
    Node object for LinkedList.
    """

    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data


class LinkedList:
    """
    Linked list of Nodes.
    """

    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")
        return (" >>> ").join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        """
        Adds a node at the start of the linked list.
        """
        node.next = self.head
        self.head = node

    def add_last(self, node):
        """
        Adds a node at the end of the linked list.
        """
        if self.head is Node:
            self.head = node
            return

        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        """
        Insert a node after a given value in the linked list.
        """
        if self.head is None:
            raise Exception("List is Empty!")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data {target_node_data} not found!")

    def add_before(self, target_node_data, new_node):
        """
        Insert a node before a give value in the linked list.
        """
        if self.head is Node:
            raise Exception("List is empty!")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f"Node with {target_node_data} not found!")


if __name__ == "__main__":

    print("Created linked list...")
    llist = LinkedList([str(i) for i in range(9)])
    print(llist)

    print("Adding 'Start' at start of linked list...")
    llist.add_first(Node("Start"))
    print(llist)

    print("Adding 'End' at end of linked list...")
    llist.add_last(Node("End"))
    print(llist)

    print("Inserting 'After' after 3...")
    llist.add_after("3", Node("After"))
    print(llist)

    print("Inserting 'Before' before 3...")
    llist.add_before("3", Node("Before"))
    print(llist)
