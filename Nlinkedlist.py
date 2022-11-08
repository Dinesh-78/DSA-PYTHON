class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_begin(self):
        data = input("Enter Data to Insert At First")
        node = Node(data)
        node.next=self.head
        self.head=node

    def inset_end(self):
        data=input("Enter Data to Insert At Last")
        mi=self.head
        while mi.next:
            mi=mi.next
        mi.next=Node(data)

    def insert_At_Middel(self):
        pos,data=map(int,input("Enter pos, data with Space ").split())
        c=0
        mi=self.head
        while mi:

            c+=1
            if c>=pos:
                break
            mi = mi.next
        node=Node(data)
        ex=mi.next

        mi.next=node
        node.next=ex

    def length(self):
        mi=self.head
        c=0
        while mi:
            c+=1
            mi=mi.next
        print('LENGTH OF LLIST - ',c)

    def delete_first(self):
        if self.head==None:
            print('LLIST IS EMPTY')
        self.head=self.head.next

    def delete_last(self):
        if self.head==None:
            print('LLIST IS EMPTY')
            return
        if self.head.next==None:
            self.head=None
            return

        mi=self.head
        while mi.next:
            prev=mi
            mi=mi.next
        prev.next=None







    def print_llist(self):
        if self.head==None:
            print("LLIST IS EMPTY")
            return
        llist = ''
        mi = self.head
        while mi:
            llist += str(mi.data) + '-->'
            mi = mi.next
        print(llist)

    def search(self):
        data=int(input("Enter node To search"))
        mi=self.head
        while mi:
            if int(mi.data)==data:
                print("Your Data is in LLinked List")
                return
            else:
                mi=mi.next
        print("Your Data Not in LLinked List")


if __name__ == "__main__":

    ll = LinkedList()
    # ll.print_llist()
    ll.insert_at_begin()
    #ll.insert_at_begin()
    ll.insert_at_begin()
    # ll.inset_end()
    # ll.insert_At_Middel()
    # ll.insert_At_Middel()
    ll.length()
    #ll.delete_last()
    #ll.delete_first()
    ll.search()
    ll.print_llist()
