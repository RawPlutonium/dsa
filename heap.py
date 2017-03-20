"""just learning heaps"""
import heapq
import threading
class Heap(object):
    """all possible heap combos"""
    def __init__(self):
        self.heap = []
    def heapush(self, item):
        """pushes item to the top of a heap(obviously :) )"""
        heapq.heappush(self.heap, item)
        print self.heap
        return self.heap

tems = Heap()
tems.heap = [9, 2, 3, 4, 'John']
tems.heapush('Dosho')
print threading.active_count()
