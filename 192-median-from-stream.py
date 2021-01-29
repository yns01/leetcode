import heapq


class MedianFinder:

    def __init__(self):
        self.minheap, self.maxheap = [], []

    def addNum(self, num: int) -> None:
        # The median is either the middle element or the mean between the two mid elements.
        # Those elements are the max value from the left part of the array
        # and the min value from the right part of the array.
        # We use two heaps to get access in O(1) time

        # We always push the max heap first. To keep them balanced, we take one from
        # the max heap and push it to the min heap
        # If the minheap has more elements than the max heap, we pop one and push it
        # to the max heap.
        # Why? Because if want to maintain them balanced, and if we can't we favor
        # the max heap so when we need the median we can just return its top element

        # Push then pop on the maxheap
        max_n = heapq.heappushpop(self.maxheap, -1 * num)
        # Push the popped element (current max) to the min heap
        # NB: We have to negate back the value as it was coming from the maxheap
        heapq.heappush(self.minheap, -max_n)

        # If the heaps are not balanced, pop the minheap and push to the max
        if len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, -1 * heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -1 * self.maxheap[0]
        else:
            return (self.minheap[0] + (-1 * self.maxheap[0])) / 2.0


mf = MedianFinder()
for n in [41, 35, 62, 5, 97, 108]:
    mf.addNum(n)

print(mf.findMedian())
