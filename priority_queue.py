import copy


class Priority_queue:

# maxium is first 

    class _Item:

        __slot__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self,other):
            return self._key < other._key

    def __init__(self,k,v):
        self.pq = []
        self.pq.append(self._Item(k,v))

    def insert(self,k,v):
        temp = self._Item(k,v)
        self.pq = self.pq + [None] *1
        tempqueue = self.pq

        length = len(tempqueue) -1
        j = 0
        for i in reversed( range(length)):
            if tempqueue[i] < temp:
                tempqueue[i+1] = tempqueue[i]
                j = i
            else:
                print('i=',i)
                j = i+1
                break
        print('j=',j )
        self.pq[j] = temp

    def print_queue(self):
        for i in range(len(self.pq)):
            print('key=', self.pq[i]._key, "value=", self.pq[i]._value)
    # insert in rear, then use upheap method to implement heappriority

    def insert_1(self, v, k):
        temp = self._Item(v,k)
        self.pq.append(temp)

        self._upheap(len(self.pq)-1)

    def _parent(self, position):
        return (position-1)//2
    def _swap(self, position, parent):
        self.pq[position], self.pq[parent] = self.pq[parent], self.pq[position]
    def _upheap(self, position):
        parent = self._parent(position)
        if position>0 and self.pq[position]._key > self.pq[parent]._key:
            self._swap(position, parent)
            self._upheap(parent)
    def _left(self, position):
        return 2*position + 1
    def _right(self, position):
        return 2* position + 2

    def _has_left(self, position):
        return self._left(position) < len(self.pq)
    def _has_right(self, position):
        return self._right(position) < len(self.pq)

    # remove node, then downheap
    def _downheap(self, position):
        left = None
        right= None
        big_child = None
        if self._has_left(position):
            left = self._left(position)
            big_child = left
            if self._has_right(position):
                right = self._right(position)
                if self.pq[left]._key < self.pq[right]._key:
                    big_child = right
            if self.pq[big_child]._key > self.pq[position]._key:
                self._swap(position, big_child)
                self._downheap(big_child)

    def delete(self, position):
        self.pq[position] = self.pq[-1]
        self.pq.pop(-1)
        self._downheap(position)



t = Priority_queue(3,"this")

t.insert(5, "test")
t.insert(9, "fhwoeh")
t.insert(10, "hrehg")
t.insert(1, "gwgw")
t.print_queue()
print("***************")
p = Priority_queue(3, "this")
p.insert_1(5, "test")
p.insert_1(9, "fhwoeh")
p.insert_1(10, "hrehg")
p.insert_1(1, "gwgw")
p.print_queue()
print("%%%%%%%%%%%%%%%%%%%")
p.delete(2)
p.print_queue()
