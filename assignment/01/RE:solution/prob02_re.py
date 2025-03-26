## recursion 한 값과 mid 값을 마지막에 추가로 비교하는 방식으로 구현해보자

# 정수 개수 입력
N = int(input())

# 정수 입력
integers = [*map(int, input().split())]

# K 입력
K = int(input())

# return하도록..

# 1 2 3 4
# k = 5
def nearest(k, start, end):
    """
    비교 대상 k를 가지고 [start,end] 범위에서 조건에 맞는 결과를 찾기 위한 이진탐색을 하는 함수입니다.

    Args:
        k (int): 비교 대상
        start (int): 비교할 범위의 시작 인덱스
        end (int): 비교할 범위의 끝 인덱스

    Returns:
        int: 정답의 인덱스를 반환
    """
    candidate_index = None    # 초기값 None
    
    
    # 후보 인덱스 결정
    if start > end:
        return -1    # 비교할 것이 없다. -> 인덱스로 될 수 없는 -1 반환
    
    mid = (start + end) // 2
    
    if integers[mid] < k:
        candidate_index = nearest(k, mid+1, end)
        
    elif integers[mid] > k:
        candidate_index = nearest(k, start, mid-1)
        
        
    # 앞에서 구한 인덱스에 해당하는 값과 현재 mid 인덱스에 해당하는 값을 문제의 조건에 따라 비교하여 알맞은 인덱스를 return
    if candidate_index == -1 or integers[mid] == k:     # 비교할 대상이 없거나 integers[mid] == k일 경우
        return mid
        
    elif abs(k-integers[mid]) == abs(k-integers[candidate_index]):
        return (mid if integers[mid] < integers[candidate_index] else candidate_index)
    
    else:
        return (mid if abs(k-integers[mid]) < abs(k-integers[candidate_index]) else candidate_index)
        
        
result_index = nearest(K, 0, N-1)

print(integers[result_index])
    