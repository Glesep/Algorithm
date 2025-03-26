# 값을 반환하도록 만들어보기

# 정수 개수 입력
N = int(input())

# 정수 입력
integers = [*map(int, input().split())]

# K 입력
K = int(input())

def rank(k, target_index=0):
    """
    integers 리스트 내에 있는 정수들과 K에 대하여 정수 K의 rank를 반환하는 함수입니다.

    Args:
        k (int): 리스트의 요소들와 비교될 정수 K
        target_index (int): K와 비교될 integers 리스트 내의 요소를 가리키는 인덱스. 초기값 0
    """
    
    if target_index == N:   # 순차 탐색이 끝났을 때
        return 1    # 반환할 rank가 없음, 전체 개수 + 1을 여기서 해준다.
    
    elif k > integers[target_index]:    # rank의 조건을 만족 시
        return 1 + rank(k, target_index+1)     # rank 개수를 1 추가
    
    else:
        return rank(k, target_index+1)
    
result_rank = rank(K)
print(result_rank)