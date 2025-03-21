from dataclasses import dataclass
from typing import Any

@dataclass
class Element:
    value: Any
    priority: int
 

class BinaryHeap:
    def __init__(self):
        self.heap: list[Element] = []
        
    def push(self,element:Element):
        self.heap.append(element)
        idx=(len(self.heap))-1
        while idx>0:
            idx_rodic = (idx-1) // 2
            rodic = self.heap[idx_rodic] 
            dite = element           
            if rodic.priority > dite.priority:
                self.heap[idx] = rodic
                self.heap[idx_rodic] = dite
            else: 
                break
         

    def pop(self):
        min_element=self.heap[0]
        last_element=self.heap.pop()
        if not self.heap: 
            return min_element
        else:
            self.heap[0]=last_element
            idx=0

            while True:
                smallest=idx
                left_child = 2 * idx + 1
                right_child = 2 * idx + 2
                if left_child <= len(self.heap)-1 and self.heap[left_child].priority < self.heap[smallest].priority:
                        smallest = left_child
                if  right_child <= len(self.heap)-1 and self.heap[right_child].priority < self.heap[smallest].priority:
                        smallest = right_child
                if smallest != idx:
                    self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
                    idx = smallest
                else: 
                    break
            return min_element

    def head(self):
        if not self.heap:
            raise Exception("Heap is empty")
        # vrati nejmensi element ve fronte (element na cele fronty)
        # protoze mame naivni implementaci, musime projit cely seznam
        min_idx = 0
        for idx in range(1,len(self.heap)):
            if self.heap[idx].priority < self.heap[min_idx].priority:
                min_idx = idx
        return self.heap[min_idx]
        
