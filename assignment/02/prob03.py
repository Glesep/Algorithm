# 정렬되지 않은 배열으로 만들어진 우선순위 큐
class pqueue_array:
    
    def __init__(self):
        self.array = []
    
    def add(self, integer):
        self.array.append(integer)
    
    # 추출할 값이 있다고 가정
    def extractMax(self):
            
        max_value = self.array[0]
        index_ofMax = 0
        
        for i in range(1,len(self.array)):
            if self.array[i] > max_value:
                max_value = self.array[i]
                index_ofMax = i
        
        # index_ofMax가 마지막 요소가 아니면 마지막 요소의 값을 덮어씀(삭제)
        
        if index_ofMax != len(self.array)-1:
            self.array[index_ofMax] = self.array[len(self.array)-1]
            
        # 마지막 요소를 삭제
        del self.array[len(self.array)-1]
            
# heap으로 만들어진 우선순위 큐
class pqueue_heap:
    
    def __init__(self):
        self.heap = []      # heap이 들어가야 함
    
    # i == 1 일 때, 에러
    # class 내부에서 만들어진 함수는 무조건 self 넣기
    def parent(self, child_index):   # 왼: 홀, 오:짝
        if child_index == 0:
            return 0
        
        elif child_index % 2 == 0:
            return int((child_index-1)/2)
        
        elif child_index % 2 != 0:
            return int((child_index-2)/2)
            
    def max_heapify(self, words_copy, i):
        """노드 i를 루트로 하는 서브트리를 heapify </br>

        if i가 부모 노드라면, 자식노드는 2i+1, 2i+2</br></br>
        전체 트리의 루트 노드를 0번 노드라고 가정합니다.

        Args:
            words_copy (list): string으로 구성된 list
            i (int): 서브트리의 루트로 삼고 싶은 노드

        Returns:
            list: 분할 정복 기법으로 heapify가 완료된 words_copy 리스트
        """

        if (i*2+1 > len(words_copy)-1):
            return words_copy


        k = i*2+1 if (i*2+2 > len(words_copy)-1) or (words_copy[i*2+1] > words_copy[i*2+2]) else i*2+2

        if (words_copy[i] >= words_copy[k]):
            return words_copy

        words_copy[i], words_copy[k] = words_copy[k], words_copy[i]

        return self.max_heapify(words_copy, k)
    
    def add(self, integer):
        
        self.heap.append(integer)
        
        i = len(self.heap)-1
        
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
    
    # 추출할 값이 있다고 가정
    def extractMax(self):
        
        max = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        del self.heap[len(self.heap)-1]
        
        self.heap = self.max_heapify(self.heap, 0)
        
        return max


import random
import time
def test(N, M):
    pq_array = pqueue_array()
    pq_heap = pqueue_heap()
    
    time_pq = {}
    
    for _ in range(N+1):
        pq_array.add(random.randint(0, N))
    
    start_time = time.time()
    
    for _ in range(M+1):
        if random.randint(0, 1) == 0 or not pq_array:
            pq_array.add(random.randint(0, N))
            
        else:
            pq_array.extractMax()
            
    end_time = time.time()
    
    time_pq['pq_array'] = end_time - start_time
    
    
    for _ in range(N+1):
        pq_heap.add(random.randint(0, N))
    
    start_time = time.time()
    
    for _ in range(M+1):
        if random.randint(0, 1) == 0 or not pq_heap:
            pq_heap.add(random.randint(0, N))
            
        else:
            pq_heap.extractMax()
            
    end_time = time.time()
    
    time_pq['pq_heap'] = end_time - start_time
    
    
    return time_pq

result = test(100000, 100000)


# {'pq_array': 84.89653015136719, 'pq_heap': 0.23450803756713867}
# 성능 차이가 많이 남을 알 수 있다.
print(result)

