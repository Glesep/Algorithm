# 정수 개수 입력
N = int(input())

# 정수 입력
input_N = input()
integers = [int(i) for i in input_N.split(" ")]

# K 입력
K = int(input())


# if-else문이 너무 많다...!
def nearest(start, end, target):
    """
    이진 검색을 이용하여 nearest를 구현했습니다.
    
    Args:
        start (int): 탐색 범위의 시작
        end (int) : 탐색 범위의 끝
        target (int): 비교 대상(K)
    """
    
    # 전 구간 탐색 완료 시 (리스트의 첫 번째 수나 마지막 수를 확인하는 경우)
    if start > end:
        if start == 1:
            print(integers[start])
        elif start == N:
            print(integers[end])
    else:
        mid = (start + end) // 2    # 직은것 먼저 체크함
        
        # 이 경우보다 더 작은 절대값이 나올 수 없음 - end case
        if target == integers[mid]:
            print(integers[mid])
        
        # target 기준 연속된 두 수가 절댓값이 같을 때 - 작은 것을 고름 (end case 2)
        elif end-start == 1:
            if abs(target - integers[end]) == abs(target - integers[start]):
                print(integers[start])
            else:
                print(integers[end] 
                      if abs(target-integers[end]) < abs(target - integers[start])
                      else integers[start])
            
        # 인덱스가 mid에 해당하는 값이 고려되지 않으면 안됨 - mid+1 대신 mid로
        elif target > integers[mid]:
            nearest(mid, end, target)
        else:
            nearest(start, mid, target)
            
nearest(0, N-1, K)