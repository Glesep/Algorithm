# # 정수 개수 입력
N = int(input())

# 정수 입력
input_N = input()
integers = [int(i) for i in input_N.split(" ")]

# K 입력
K = int(input())

def nearest(start, end, target):
    """
    이진 검색을 이용하여 nearest를 구현했습니다.
    
    Args:
        start (int): 탐색 범위의 시작
        end (int) : 탐색 범위의 끝
        target (int): 비교 대상(K)
    """
    
    # 전 구간 탐색 완료 시
    if start > end:
        pass
    
    else:
        mid = (start + end) // 2
        
        # 이 경우보다 더 작은 절대값이 나올 수 없음 - end case
        if target == integers[mid]:
            print(integers[mid])
            
        elif target > integers[mid]:
            nearest(mid, end, target)
            
        else:
            nearest(start, mid, target)
            


"""
25개 
12

무조건 두개가 남는가? - NO
1 3 6 9 13 17 21 23 24 31 37 38(12) 44 45 47 51 55 58 71 73 88 91 99 101 102
"""
    
    


