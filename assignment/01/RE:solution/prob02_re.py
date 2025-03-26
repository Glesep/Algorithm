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

    if start > end:
        if start == 1:
            return integers[start]
        elif start == N:
            return integers[end]
    
    mid = (start + end) // 2
    
    if integers[mid] == k:
        return integers[mid]
    
    elif integers[mid] < k:
        # 이후 nearest에서 반환할 값과 integers[mid]와 비교해서 가까운 것 찾기
        return (integers[mid] 
                if abs(k-integers[mid]) <= abs(k-nearest(k, mid+1, end)) 
                else nearest(k, mid+1, end))
    
    elif integers[mid] > k:
        return (nearest(k, start, mid-1)
                if abs(k-integers[mid]) <= abs(k-nearest(k, start, mid-1))
                else integers[mid])
    