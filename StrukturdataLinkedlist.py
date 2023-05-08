class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        Memeriksa apakah linked list kosong.

        Returns:
            bool: True jika linked list kosong, False jika sebaliknya.
        """
        return self.head is None

    def append(self, data):
        """
        Menambahkan elemen baru ke akhir linked list.

        Args:
            data: Nilai data dari elemen baru.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        """
        Menambahkan elemen baru di awal linked list.

        Args:
            data: Nilai data dari elemen baru.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """
        Menghapus kemunculan pertama elemen yang ditentukan dari linked list.

        Args:
            data: Nilai data yang akan dihapus.
        """
        if self.head and self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                current = current.next

    def search(self, data):
        """
        Mencari elemen yang ditentukan dalam linked list.

        Args:
            data: Nilai data yang akan dicari.

        Returns:
            bool: True jika elemen ditemukan, False jika sebaliknya.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def print_list(self):
        """
        Mencetak elemen-elemen dari linked list.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


"""
Membuat linked list dari input user
"""
def create_linked_list():
    values = input("Masukkan elemen-elemen dalam list (dipisahkan oleh spasi): ").split()
    my_list = LinkedList()
    for value in values:
        my_list.append(int(value))
    return my_list


my_list = create_linked_list()

"""
Mencetak linked list
"""
my_list.print_list()
