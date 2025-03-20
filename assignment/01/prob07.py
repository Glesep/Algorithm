n = int(input())

# 이전 숫자가 1이면 아무거나
# 이전 숫자가 0이면 1

result = []

def solveProb(count=0, num_result='', num_prev=-1):
    """
    문제를 푸는 함수입니다.

    Args:
        count (int, optional): 이전에 함수가 몇 번 수행됐는지 확인하는 변수. 기본값은 0.
        num_result (str, optional): 이진수로 표현된 문자. 기본값은 ''.
        num_prev (int, optional): 바로 전 과정에서 무슨 숫자가 결합했는가 확인하는 변수. 기본값은 -1.
    """
    global result
    
    if count == n:      # 다 만들었으면 리스트에 추가 후 종료
        result.append(num_result)
    
    else:
        if num_prev == -1 or num_prev == 1:
            solveProb(count+1, num_result+'0', 0)

        solveProb(count+1, num_result+'1', 1)   # 모든 경우에 한번씩 해야함


solveProb()      
print(len(result))