import sys

class MaxHeap:
    def __init__(self):
        self.data = [None]
    def insert(self, item):
        self.data.append(item)
        i = len(self.data) - 1
        while i > 1:
            if self.data[i] > self.data[(i // 2)]:
                self.data[i], self.data[(i // 2)] = self.data[(i // 2)], self.data[i]
                i = i // 2
            else: break

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop()
            self.maxHeapify(1)
        else: data = None
        return data

    def maxHeapify(self, i):
        left = 2 * i
        right = (2 * i) + 1
        biggest = i
        
        if left < len(self.data) and self.data[i] < self.data[left]:
            biggest = left
        
        if right < len(self.data) and self.data[biggest] < self.data[right]:            
            biggest = right

        if biggest != i:
            self.data[i], self.data[biggest] = self.data[biggest], self.data[i]
            self.maxHeapify(biggest)

class MinHeap:
    def __init__(self):
        self.data = [None]
    def insert(self, item):
        self.data.append(item)
        i = len(self.data) - 1
        while i > 1:
            if self.data[i] < self.data[(i // 2)]:
                self.data[i], self.data[(i // 2)] = self.data[(i // 2)], self.data[i]
                i = i // 2
            else: break

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop()
            self.minHeapify(1)
        else: data = None
        return data

    def minHeapify(self, i):
        left = 2 * i
        right = (2 * i) + 1
        smallest = i
        
        if left < len(self.data) and self.data[i] > self.data[left]:
            smallest = left
        
        if right < len(self.data) and self.data[smallest] > self.data[right]:            
            smallest = right

        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.minHeapify(smallest)

def medianonline():
   
    
    max = MaxHeap()
    min = MinHeap()
    median = 0
    sum_median = 0

    for i in range(iter):
        '''insert'''
        if i == 0: 
            max.insert(N[i])
            median = N[i]
            sum_median += N[i]
            continue
        
        elif len(max.data) == len(min.data):
            max.insert(N[i])
        
        else: 
            min.insert(N[i])

        '''maxheap.root > minheap.root일 때 바꿔주기'''
        if len(max.data) > 1 and len(min.data) > 1 and max.data[1] > min.data[1]:
            a = max.data[1]
            b = min.data[1]

            max.remove()
            min.remove()

            max.insert(b)
            min.insert(a)

        '''홀수 / 짝수 케이스 나누기'''
        # 홀수
        if i % 2 == 0: median = max.data[1]
        # 짝수
        else: median = (max.data[1] + min.data[1]) // 2
        
        sum_median += median


    print(sum_median % 10)

T = int(sys.stdin.readline())
for i in range(T):
    medianonline()