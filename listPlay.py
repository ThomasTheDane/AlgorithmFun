class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        sizeCount = 0;
        while(current != None):
            sizeCount = sizeCount + 1
            current = current.getNext()
        return sizeCount
    def search(self, item):
        current = self.head
        found = False
        while(current != None and not found):
            if(current.getData() == item):
                found = True
            else:
                current = current.getNext()
        return found

    def indexOf(self, item):
        current = self.head
        found = False;
        index = 0;
        while(not found):
            if(current.getData() == item):
                found = True;
            else:
                index = index + 1;
                current = current.getNext();
        if(found):
            return index
        else:
            return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    def insert(self, item, position):
        current = self.head
        previous = None
        index = 0
        while current != None:
            if(index == position):
                temp = Node(item)
                temp.setNext(current)
                if(previous):
                    previous.setNext(temp)
                else:
                    self.head = temp
                return True
            else:
                previous = current
                index = index + 1
                current = current.getNext()
        return False

    def printList(self):
        current = self.head
        print(self.head.getData())
        while(current.getNext() != None):
            current = current.getNext()
            print current.getData()

def binarySearch(searchList, item):
    length = len(searchList)
    first = 0
    last = length - 1
    index = (first + last) / 2

    while(searchList[index] != item):
        if(searchList[index] < item):
            last = index
        if(searchList[index] > item):
            first = index
        if(first == last):
            return false
        index = (first + last) / 2
    return index

def binarSearchRecursive(searchList, itemSearching):
    if(len(searchList) == 0):
        return False
    else:
        index = len(searchList) / 2
        if(searchList[index] == itemSearching):
            return True
        if(searchList[index] < itemSearching):
            return binarSearchRecursive(searchList[index+1:],itemSearching)
        if(searchList[index] > itemSearching):
            return binarSearchRecursive(searchList[:index], itemSearching)

def tests():
    myList = UnorderedList()
    myList.add(7)
    myList.add(6)
    myList.add(5)
    myList.add(4)
    
    print "size", myList.size()
    print "has 22: ", myList.search(22)
    if(myList.search(22)):
        print "location of 22: ", myList.indexOf(22)

    myList.insert(3, 0)
    myList.add(2)
    myList.add(1)
    myList.printList()
    myNormalList = [1,2,3,4,5,6,7]
    print binarySearch(myNormalList, 4) == 3
    print not binarSearchRecursive(myNormalList, 44)

if __name__ == '__main__':
    tests()