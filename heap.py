import heapq


class Bin_heap:
    def __init__(self):
        self.heaplist = []
        self.heapsize = 0

    def heapify(self, root_index):
        largest = root_index
        left_child = 2 * root_index + 1
        right_child = 2 * root_index + 2

        if left_child < self.heapsize and self.heaplist[left_child] > self.heaplist[largest]:
            self.heaplist[largest], self.heaplist[left_child] = self.heaplist[left_child], self.heaplist[largest]
            self.heapify(left_child)

        if right_child < self.heapsize and self.heaplist[right_child] > self.heaplist[largest]:
            self.heaplist[largest], self.heaplist[right_child] = self.heaplist[right_child], self.heaplist[largest]
            self.heapify(right_child)


    def build_heap(self, lst:list):
        self.heaplist = lst
        self.heapsize = len(lst)
        for i in range(len(lst)// 2, -1 , -1):
            self.heapify(i)

    def show_heap(self):
        return self.heaplist



b = Bin_heap()
b.build_heap([5,6,12,10,1,9])
print(b.show_heap())
t = [5,6,12,10,1,9]
heapq._heapify_max(t)
print(t)
