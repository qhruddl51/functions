import random

class IndexRing () : 
    """
    0 ~ capacity-1 까지의 자연수를 차례대로 반환해주는 nextidx method를 가짐
    capacity-1 까지 갔으면 다시 0부터 같은 순서로 반환
    """
    def __init__(self, capacity, shuffle):
        self.capacity=capacity
        self.ring = list(range(capacity))
        self.next = 0 # 반환하고자하는 자연수의 인덱스
        self.shuffle = shuffle
        self.fixed = False
        
    def nextidx(self) :
        if self.next == 0 and self.shuffle and not self.fixed : random.shuffle(self.ring)
        # self.fixed가 되어있는데 셔플해 버리면 next가 바뀌어서 반환값도 일정하지 않음
        result = self.ring[self.next]
        if self.next == self.capacity-1 : self.next = 0
        elif not self.fixed : self.next += 1
        else : pass
        return result
    
    def fixidx(self, fix) :
        """next를 고정시켜, 반환하는 자연수값도 고정시킴. 또는 고정을 풂.
        Args:
            fix (bool): True or False
        """
        self.fixed = fix
    
    def force_shuffle(self) :
        random.shuffle(self.ring)
    
    pass # IndexRing
