import time

with open("./files/harry_full.txt", 'r', encoding='utf-8-sig') as f:
    lines = f.read().splitlines()
    words = [words for line in lines for words in line.split()]
    
# -------------------------------------------------------------------------------------------------------

def bubble_sort(words_copy):
    """bubble sort 알고리즘을 구현한 함수입니다.

    Args:
        words_copy (list): 정렬하고 싶은 리스트

    Returns:
        list: 정렬된 리스트
    """
    for i in range(len(words)-1, 0, -1):
        for j in range(0, i):
            if (words_copy[j] > words_copy[j+1]):
                words_copy[j], words_copy[j+1] = words_copy[j+1], words_copy[j]
                
    return words_copy

# -------------------------------------------------------------------------------------------------------

def insertion_sort(words_copy):
    """insertion sort 알고리즘을 구현한 함수입니다.

    Args:
        words_copy (list): 정렬하고 싶은 리스트

    Returns:
        list: 정렬된 리스트
    """
    for i in range(1, len(words_copy)):
        tmp = words_copy[i]
        j = i
        
        while j > 0 and tmp < words_copy[j-1]:
            words_copy[j] = words_copy[j-1]
            j -= 1
            
        words_copy[j] = tmp   
    
    return words_copy

# -------------------------------------------------------------------------------------------------------

def merge(words_copy, start, mid, end):
    """words_copy 리스트에서 첫 번째 부분 집합([start, mid]), 두 번째 부분집합([mid+1, end])을 merge하는 함수입니다.

    Args:
        words_copy (list): 정렬하고 싶은 list
        start (int): 첫번째 부분집합의 시작 인덱스
        mid (int): 첫 번째 부분집합의 끝 인덱스
        end (int): 두 번째 부분집합의 끝 인덱스

    Returns:
        list: 두 부분집합이 merge되어 나온 집합이 적용된 전체 집합 words_copy
    """
    i = start
    j = mid+1
    tmp = []
    while (i <= mid and j <= end):
        if words_copy[i] <= words_copy[j]:
            tmp.append(words_copy[i])
            i+=1
        else:
            tmp.append(words_copy[j])
            j+=1
            
    while(i<=mid):
        tmp.append(words_copy[i])
        i+=1
    while(j <= end):
        tmp.append(words_copy[j])
        j+=1
    
    words_copy[start:end+1] = tmp
    return words_copy

def merge_sort(words_copy, start, end):
    """merge sort 알고리즘을 구현한 함수입니다.

    Args:
        words_copy (list): 정렬하고 싶은 리스트
        start (int): 정렬하고 싶은 범위의 시작 인덱스
        end (int): 정렬하고 싶은 범위의 끝 인덱스

    Returns:
        list: 분할 정복 기법으로 정렬이 완료된 words_copy 리스트
    """
    mid = (start + end) // 2
    
    if start < end:
        words_copy = merge_sort(words_copy, start, mid)
        words_copy = merge_sort(words_copy, mid+1, end)
    
    return merge(words_copy, start, mid, end)

# -------------------------------------------------------------------------------------------------------

def partition(words_copy, p, r):
    """하나의 시행에서 pivot을 기준으로 pivot보다 작은 수는 왼쪽, 큰 수는 오른쪽에 위치하도록 만들고, </br>
    변화된 리스트와 pivot의 현 위치를 반환하는 함수입니다.

    Args:
        words_copy (list): 정렬하고 싶은 인덱스
        p (int): 정렬할 범위의 첫 번째 인덱스
        r (_type_): 정렬할 범위의 마지막 인덱스

    Returns:
        int: pivot이 위치할 인덱스
    """
    pivot = words_copy[r]
    i = p-1
    
    for j in range(p, r):

        if words_copy[j] <= pivot:
            i += 1
            words_copy[i], words_copy[j] = words_copy[j], words_copy[i]
        
    words_copy[i+1], words_copy[r] = words_copy[r], words_copy[i+1]
    
    return words_copy, i+1

    
def quick_sort(words_copy, p, r):
    """quik sort 알고리즘을 구현한 함수입니다. pivot은 항상 words_copy[r]입니다.

    Args:
        words_copy (_type_): 정렬하고 싶은 함수
        p (int): 정렬하고 싶은 범위의 첫 번째 인덱스
        r (int): 정렬하고 싶은 범위의 마지막 인덱스

    Returns:
        list: 분할 정복 기법으로 도출된 정렬된 words_copy 리스트
    """
    if (p < r):
        words_copy, q = partition(words_copy, p, r)
        words_copy = quick_sort(words_copy, p, q-1)
        words_copy = quick_sort(words_copy, q+1, r)
        
    return words_copy
    
# -------------------------------------------------------------------------------------------------------
# max-heapify의 시간복잡도는 트리의 높이를 넘을 수 없음
# 따라서 O(logn)
def max_heapify(words_copy, i):
    """노드 i를 루트로 하는 서브트리를 heapify </br>
    
    if i가 부모 노드라면, 자식노드는 2i+1, 2i+2</br></br>
    전체 트리의 루트 노드를 0번 노드라고 가정합니다.

    Args:
        words_copy (list): string으로 구성된 list
        i (int): 서브트리의 루트로 삼고 싶은 노드

    Returns:
        list: 분할 정복 기법으로 heapify가 완료된 words_copy 리스트
    """
    
    # 자식 노드가 없다면 종료
    if (i*2+1 > len(words_copy)-1):
        return words_copy
    
    # 자식 노드 중 큰 쪽을 선택
    k = i*2+1 if (i*2+2 > len(words_copy)-1) or (words_copy[i*2+1] > words_copy[i*2+2]) else i*2+2
    
    # 만약 선택된 자식 노드보다 부모노드가 크거나 같다면 종료
    if (words_copy[i] >= words_copy[k]):
        return words_copy

    # 아니라면 교환
    words_copy[i], words_copy[k] = words_copy[k], words_copy[i]
    
    # 후 교환된 노드를 root로 하는 max heapify를 recursive하게 실행
    return max_heapify(words_copy, k)
    
# O(n)으로 알려져있다.
def build_max_heap(words_copy):
    """words_copy 리스트 구성을 max-heap으로 만드는 함수입니다.

    Args:
        words_copy (list): max-heap으로 구성하고 싶은 list

    Returns:
        list: max-heap화 완료된 리스트
    """
    
    for i in range(len(words_copy)//2, -1, -1):
        words_copy = max_heapify(words_copy, i)
        
    return words_copy

def max_heap_sort(words_copy):
    """ max-heap으로 heap sort 알고리즘을 구현한 함수입니다.
        오름차순 정렬이 수행됩니다.

    Args:
        words_copy (list): 정렬하고 싶은 리스트

    Returns:
        list: heap sort로 오름차순 정렬이 된 리스트
    """
    
    words_copy = build_max_heap(words_copy)
    heap_size = len(words_copy)
    while heap_size > 1:
        words_copy[heap_size-1], words_copy[0] = words_copy[0], words_copy[heap_size-1]
        heap_size -= 1
        words_copy[:heap_size] = max_heapify(words_copy[:heap_size], 0)
        
    return words_copy
        
# -------------------------------------------------------------------------------------------------------
 
def min_heapify(words_copy, i):
    """노드 i를 루트로 하는 서브트리를 min-heapify </br>
    
    if i가 부모 노드라면, 자식노드는 2i+1, 2i+2</br></br>
    전체 트리의 루트 노드를 0번 노드라고 가정합니다.

    Args:
        words_copy (list): string으로 구성된 list
        i (int): 서브트리의 루트로 삼고 싶은 노드

    Returns:
        list: 분할 정복 기법으로 heapify가 완료된 words_copy 리스트
    """
    
    # 자식 노드가 없다면 종료
    if (i*2+1 > len(words_copy)-1):
        return words_copy
    
    # 자식 노드 중 작은 쪽을 선택
    k = i*2+1 if (i*2+2 > len(words_copy)-1) or (words_copy[i*2+1] < words_copy[i*2+2]) else i*2+2
    
    # 만약 선택된 자식 노드보다 부모노드가 작거나 같다면 종료
    if (words_copy[i] <= words_copy[k]):
        return words_copy

    # 아니라면 교환
    words_copy[i], words_copy[k] = words_copy[k], words_copy[i]
    
    # 후 교환된 노드를 root로 하는 min heapify를 recursive하게 실행
    return min_heapify(words_copy, k)

# O(n)으로 알려져있다.
def build_min_heap(words_copy):
    """words_copy 리스트 구성을 min-heap으로 만드는 함수입니다.

    Args:
        words_copy (list): min-heap으로 구성하고 싶은 list

    Returns:
        list: min-heap화 완료된 리스트
    """
    
    for i in range(len(words_copy)//2, -1, -1):
        words_copy = min_heapify(words_copy, i)
        
    return words_copy

def min_heap_sort(words_copy):
    """ min-heap으로 heap sort 알고리즘을 구현한 함수입니다.
        내림차순 정렬이 수행됩니다.

    Args:
        words_copy (list): 정렬하고 싶은 리스트

    Returns:
        list: heap sort로 내림차순 정렬이 된 리스트
    """
    
    words_copy = build_min_heap(words_copy)
    heap_size = len(words_copy)
    while heap_size > 1:
        words_copy[heap_size-1], words_copy[0] = words_copy[0], words_copy[heap_size-1]
        heap_size -= 1
        words_copy[:heap_size] = min_heapify(words_copy[:heap_size], 0)
        
    return words_copy

# -------------------------------------------------------------------------------------------------------

# max, min heap_sort를 합친 함수를 구현함
def heap_sort(words_copy, ascending=True):
    
    if ascending:
        words_copy = build_max_heap(words_copy)
        heap_size = len(words_copy)
        while heap_size > 1:
            words_copy[heap_size-1], words_copy[0] = words_copy[0], words_copy[heap_size-1]
            heap_size -= 1
            words_copy[:heap_size] = max_heapify(words_copy[:heap_size], 0)

        
    
    else:
        words_copy = build_min_heap(words_copy)
        heap_size = len(words_copy)
        while heap_size > 1:
            words_copy[heap_size-1], words_copy[0] = words_copy[0], words_copy[heap_size-1]
            heap_size -= 1
            words_copy[:heap_size] = min_heapify(words_copy[:heap_size], 0)


    return words_copy

# -------------------------------------------------------------------------------------------------------
# 자유작성

target_list = [10,20,9,81,33,7,100]

result = heap_sort(target_list, True)
print(result)

# -------------------------------------------------------------------------------------------------------
# archive = {}

# sort들을 각각 실행하는 것은 측정이 되는데 한꺼번에 실행하는 것은 stackoverflow가 납니다.

# 380.6092691421509s
# words_copied = words
# start_time = time.time()
# bubble_sort(words_copied)
# end_time = time.time()
# archive['bubble_sort'] = end_time-start_time


# 239.17551016807556s
# words_copied = words
# start_time = time.time()
# words_copied = insertion_sort(words_copied)
# end_time = time.time()
# archive['insertion_sort'] = end_time-start_time


# 0.15517807006835938
# words_copied = words
# start_time = time.time()
# words_copied = merge_sort(words_copied, 0, len(words_copied)-1)
# end_time = time.time()
# archive['merge_sort'] = end_time-start_time


# 3.721475839614868s
# import sys
# sys.setrecursionlimit(10000)

# words_copied = words
# start_time = time.time()
# words_copied = quick_sort(words_copied, 0, len(words_copied)-1)
# end_time = time.time()
# print(words_copied)
# archive['quick_sort'] = end_time-start_time


# 44.33114433288574s
# words_copied = words
# start_time = time.time()
# words_copied = heap_sort(words_copied)
# end_time = time.time()
# archive['heap_sort'] = end_time-start_time

# 0.02200603485107422s
# words_copied = words
# start_time = time.time()
# words_copied.sort()
# end_time = time.time()
# archive['library_sort'] = end_time-start_time

# print(archive)