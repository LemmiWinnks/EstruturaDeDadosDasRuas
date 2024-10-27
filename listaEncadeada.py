class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next
    
    def setNext(self, newNext):
        self.next = newNext

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.quantity = 0
    
    def insert(self, value):
        if self.quantity == 0:
            new_node = Node(value)
            self.head = new_node
            self.quantity += 1
        else:
            new_node = Node(value)

            previous_node = self.previousNode()
            previous_node.next = new_node

            self.quantity += 1

    def removeNo(self, nodeForRemove):
        node_X = Node(None)
        node = self.head
        counter = 0
        while counter < self.quantity:
            counter += 1
            if node == self.head:
                if  node.getValue() == nodeForRemove:
                    self.head = self.head.getNext()
                    break
            else:
                if node.getValue() == nodeForRemove:
                    node_X = node
                    counter = 0
                    node = self.head

                if node.getNext() == node_X:
                    node.setNext(node_X.getNext()) 
                    break

            node = node.getNext()

    def previousNode(self):
        node = self.head
        counter = 0
        while counter < self.quantity:
            if node.getNext() == None:
                return node
            else:
                node = node.getNext()
            
            counter += 1

    def displayList(self):
        node = self.head
        counter = 0
        while counter < self.quantity:
            if node.getNext() == None:
                print(node.getValue())
                break
            else:
                print(node.getValue())
                node = node.getNext()
            

            counter += 1




lista = LinkedList()

lista.insert(10)
lista.insert(40)
lista.insert(50)

lista.displayList()

print("-----------------")

lista.removeNo(40)

lista.displayList()