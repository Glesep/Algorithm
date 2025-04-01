n = int(input())

# 이전 숫자가 1이면 아무거나
# 이전 숫자가 0이면 1

# 이는 이전 숫자가 1이면 0을 추가로 고려하고, 
# 모든 경우의 수에 1을 고려해야 한다는 뜻입니다.

result = []

def make_binary(num_result=''):
    """
    문제의 조건에 맞는 이진수를 구해 result에 넣는 함수입니다.

    Args:
        num_result (str, optional): 이진수, 길이가 n과 같아지면 result에 저장됨. Defaults to ''.
    """
    global result
    
    if len(num_result) == n:      # 다 만들었으면 리스트에 추가 후 종료
        result.append(num_result)
    
    else:
        if num_result == '' or num_result[-1] == '1':
            make_binary(num_result+'0')

        make_binary(num_result+'1')   # 모든 경우에 한번씩 해야함


make_binary()      
print(len(result))