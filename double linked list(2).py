class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext
    def setPrev(self,newprev):
        self.prev = newprev

class orderedlist:

    def __init__(self):
        self.head = None

    def show(self):
        current = self.head
        print ('None <-')
        print ('Head ->', end='')
        while current != None:
            if current.getNext() == None:
                print (current.getData(), end='->')
            else:
                print (current.getData(), end='<->')
            current = current.getNext()
        print ('None')
    def isEmpty(self):
        return self.head == None
    def add(self,item):
        temp = Node(item)

        temp.setNext(self.head)
        temp.setPrev(None)
        next = temp.getNext()
        if next != None:
            next.setPrev(temp)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
    def gan(self,item):
        for i in range(len(item)):
            if item[i] % 2 == 1:
                ganjil.append(item[i])
        ol.sort(ganjil)
        print(ganjil)

    def gen(self,item):
        for i in range(len(item)):
            if item[i] % 2 == 0:
                genap.append(item[i])
        ol.sort(genap)
        print(genap)

    def sort(self,item):
        for x in range(len(item)-1, 0, -1):
            for y in range(x):
                if item[y] > item[y+1]:
                    item[y], item[y+1] = item[y+1], item[y]
    def tambah(self,item):
        pil = "y"
        while pil == "y":
            tam = int(input("masukkan data : "))
            lis.append(tam)
            pil = str(input("apakah anda mau memasukkan data lagi ? (y/n)"))
        ol.gan(lis)
        ol.gen(lis)
        genap.reverse()
        merge = ganjil + genap
        for i in merge:
            ol.add(i)

    def search(self):
        current = self.head
        s = int(input("masukkan data yang akan dicari : "))
        found = False
        while current != None and not found:
            if current.getData() == s:
                found = True
                print('Data in List')
            else:
                current = current.getNext()
        if found == False:
            print('Data not in List')

        return found
    def remove(self):
        current = self.head
        s = int(input("masukkan data yang akan dihapus : "))
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == s:
                found = True
                print("Data deleted")
            else:
                previous = current
                current = current.getNext()
                if current == None:
                    next = None
                else:
                    next = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            if current == None:
                previous.setNext(None)
            else:
                previous.setNext(current.getNext())
            if next != None:
                next.setPrev(current.getPrev)
        if current is None:
            print("Data not in list")

ol = orderedlist()
lis = [100,200,300,311,255]
genap=[]
ganjil=[]
merge = ganjil + genap
ol.tambah(ol)
ol.show()
print("panjang datanya adalah",orderedlist.size(ol))
orderedlist.search(ol)
orderedlist.remove(ol)