from node import Node
from requests import get


class LinkedList:
    
    def __init__(self):
        self.head = None

    def add_node(self, value):
        node = Node(value)
        if not self.head:
          self.head = node
        else:
          current_node = self.head
          while current_node.right:
              current_node = current_node.right
          current_node.right = node

    def __iter__(self):
       current_node = self.head
       while current_node:
          yield current_node
          current_node = current_node.right

    def __repr__(self):
      return ' -> '.join(node.value for node in self)
      # nodes = []
      # for node in self:
      #   nodes.append(node.value)
      # return ' -> '.join(nodes)

    def insert_node(self, target, value):
       new_node = Node(value)
       if self.head:
          for node in self:
             if node.value == target:
                right_node = node.right
                node.right = new_node
                new_node.right = right_node
       else:
          print('Empty List')
    
    def insert_node_before(self, target, value):
       new_node = Node(value)
       if self.head:
          for node in self:
             if node.value == target:
                left_node = node
                node = new_node
                new_node = left_node

    def remove_node(self, value):
       if value == self.head.value:
            self.head = self.head.right
       else:
          for node in self:
             if node.right.value == value:
                node.right = node.right.right
                return
    
    def add_list_elements(self, lst):
       for ele in lst:
          self.add_node(ele)
          
       
             
    

linked_list = LinkedList()

linked_list.add_node('Sunday')
linked_list.add_node('Monday')
linked_list.add_node('Tuesday')
linked_list.add_node('Thursday')
#print(linked_list)


linked_list.insert_node_before('Thursday', 'Wednesday')
#print(linked_list)


