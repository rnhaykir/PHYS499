from LinkedList import LinkedList

class LinkedList(LinkedList):
    def __init__(self):
        super().__init__()
    
    def intersection(self, L2):
        L3 = LinkedList()
        L2_elements = []
        L3_elements = []
        current_L2 = L2.__head
        while current_L2:
            L2_elements.append(current_L2.element)
            current_L2 = current_L2.next
        current = self.__head
        while current:
            if current.element in L2_elements and current.element not in L3_elements:
                L3_elements.append(current.element)
            current = current.next
        L3_elements.sort()
        for i in L3_elements:
            L3.addLast(i)
        return L3
    
    def union(self, L2):
        L3 = LinkedList()
        L3_elements = []
        current_L2 = L2.__head
        while current_L2:
            L3_elements.append(current_L2.element)
            current_L2 = current_L2.next
        current = self.__head
        while current:
            if current.element not in L3_elements:
                L3_elements.append(current.element)
            current = current.next
        L3_elements.sort()
        for i in L3_elements:
            L3.addLast(i)
        return L3
    
    def __isequal__(self, L2):
        current = self.__head
        current_l2 = L2.__head
        while current and current_l2:
            if current.element != current_l2.element:
                return False
            current = current.next
            current_l2 = current_l2.next
        return True


L1 = LinkedList()
L2 = LinkedList()
expected_intersection = LinkedList()
for i in [2, 4, 8, 12, 20, 46]:
    L1.addLast(i)
for i in [1, 4, 12, 35, 72]:
    L2.addLast(i)
for i in [4, 12]:
    expected_intersection.addLast(i)
L3 = L1.intersection(L2)

print(L1.__str__(), L2.__str__(), L3.__str__())

L1 = LinkedList()
L2 = LinkedList()
expected_union = LinkedList()
for i in [2, 4, 8, 12, 20, 46]:
    L1.addLast(i)
for i in [1, 4, 12, 35, 72]:
    L1.addLast(i)
for i in [1, 2, 4, 8, 12, 20, 35, 46, 72]:
    expected_union.addLast(i)
L3 = L1.union(L2)

print(L1.__str__(), L2.__str__(), L3.__str__())
