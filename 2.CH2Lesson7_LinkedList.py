"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        Obj = self.head
        counter = 1
        if (position > 1):
            while counter < position:
                Obj = Obj.next
                counter += 1
        return Obj

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        temp_Obj = self.head
        counter = 1
        while counter < position:
            temp_Obj = temp_Obj.next
            if (counter == position - 2):
                new_element.next = temp_Obj.next
                temp_Obj.next = new_element
            counter += 1

    def delete(self, value):
        """Delete the first node with a given value."""
        obj = self.head
        if value == obj.value:  # if first object match the values then change in head other wiise change in obj.head
            pass
            self.head = self.head.next
            obj.next = None
        else:
            count = 1
            while obj.next != None:
                if value == obj.value:
                    prevObj.next = obj.next
                    obj.next = None
                else:
                    prevObj = obj
                    obj = obj.next
                count += 1


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
