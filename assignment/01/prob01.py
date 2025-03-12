# 임의의 정수 K의 rank : N개의 정수 중 K보다 작은 것의 개수 + 1

# 정수 개수 입력
N = int(input())

# 정수 입력
input_N = input()
integers = [int(i) for i in input_N.split(" ")]

# K 입력
K = int(input())

def checkRank(K, target_index=0, rank=1):
    """Rank를 찾는 함수입니다.
    이 함수는 N개의 요소를 가진 리스트를 순차탐색하며 rank 검사를 하므로
    시간복잡도는 O(N)입니다.

    Args:
        K (int): Rank를 구하는 대상입니다.
        target (int): 비교 대상의 리스트 상 위치(인덱스)입니다.
        rank: rank입니다. (초기값: 1)
    """
    
    if target_index >= N:   # 인덱스가 N 이상일 때(검사가 끝났을 때)
        print(rank)
    elif K > integers[target_index]:    # rank 조건에 맞을 때
        checkRank(K, target_index+1, rank+1)
    else:   # rank 조건에 맞지 않을 때
        checkRank(K, target_index+1, rank)
          
checkRank(K)