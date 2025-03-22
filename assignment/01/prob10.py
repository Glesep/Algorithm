with open('./files/input10.txt', 'r', encoding='utf-8-sig') as f:
    N = int(f.readline())
    info = [[*map(int, f.readline().split())] for _ in range(N)]
    W = int(f.readline())

# 가져갈 물건의 부피 총량은 W를 초과해서는 안됨
# (가져가는 물건의 가격의 합 - 가져가지 않을 물건의 폐기비용)의 최대값


# 모든 경우의 수를 다 확인해야함 - 멱집합 응용

include = [None] * N    # 물건이 들어가는지 들어가지 않는지 정의하는 boolean 리스트
result_max = None

def Move_powerset(k=0):
    """
    멱집합을 구하는 알고리즘을 이용하여 모든 경우의 수를 확인 후, </br>
    조건에 맞는 답을 추출해내는 함수입니다.

    Args:
        k (int): 멱집합 알고리즘의 상태이상트리에서 현재 위치. 기본값:0
    """
    global result_max
    
    if k == N:
        
        # include[i]가 True일 때의 부피 추출
        W_include = [info[i][0] for i in range(N) if include[i]]
        W_total = sum(W_include)
        
        if W_total <= W:    # 한계 부피를 초과하지 않을 때
        
            # include[i]가 True일 때의 가격 추출
            V_include = [info[i][1] for i in range(N) if include[i]]
            V_total = sum(V_include)
            
            # include[i]가 False일 때 폐기비용 추출
            C_exclude = [info[i][2] for i in range(N) if not include[i]]
            C_total = sum(C_exclude)
            
            result = V_total - C_total
            
            if result_max == None or result > result_max:
                result_max = result
    
        return
    
    include[k] = False      # k번째를 제외한 나머지 수로 부분집합
    Move_powerset(k+1)
    
    include[k] = True       # k번째를 포함하고 나머지 수로 부분집합
    Move_powerset(k+1)

Move_powerset(0)
print(result_max)