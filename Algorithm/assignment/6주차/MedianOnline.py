import sys

def heappush(heap, item):
    heap.append(item)
    siftdown(heap, 0, len(heap)-1)

def siftdown(heap, startpos, pos):
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

def heappop(heap):
    lastelt = heap.pop()    
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        siftup(heap, 0)
        return returnitem
    return lastelt

def siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    childpos = 2*pos + 1    
    while childpos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    heap[pos] = newitem
    siftdown(heap, startpos, pos)

def push_heap(left_heap: list, right_heap: list, num: int, n: int):
    if n % 2 == 1:
        heappush(right_heap, num)
    else:
        heappush(left_heap, -num)


def make_mid_heap(left_heap: list, right_heap: list):
    if left_heap:  
        left_max = -left_heap[0]
        right_min = right_heap[0]
        if left_max > right_min:
            heappush(left_heap, -heappop(right_heap))
            heappush(right_heap, -heappop(left_heap))


def get_mid_number(left_heap: list, right_heap: list, n: int) -> int:
    # 숫자의 개수가 홀수이면, 라이트에서 최소값을 반환
    # 숫자의 개수가 짝수이면, 레프트 최대와 라이트 최소를 비교하여 최소값 반환
    if n % 2 == 1:
        return right_heap[0]
    else:
        return (-left_heap[0] + right_heap[0]) //2


if __name__ == '__main__':
    T = int(sys.stdin.readline())  # 숫자의 개수
    for i in range(T):
        iter, *N = map(int, sys.stdin.readline().split())

        left_numbers = []  # 최대 힙(최대값을 음수로 넣어 최대값이 0번에 오게 한다)
        right_numbers = []  # 최소 힙
        median = 0
        sum_median = 0

        for i in range(iter):
            number = N[i]
            push_heap(left_numbers, right_numbers, number, i+1)
            make_mid_heap(left_numbers, right_numbers)
            median = get_mid_number(left_numbers, right_numbers, i+1)
            sum_median += median

        print(sum_median % 10)