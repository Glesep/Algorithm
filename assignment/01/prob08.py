with open('./files/input.txt', 'r', encoding='utf-8-sig') as f:
    N = int(f.readline())
    W = int(f.readline())
    w = [*map(int, f.readline().split())]
    v = [*map(int, f.readline().split())]

# 모든 경우의 수를 다 확인해야함 - 멱집합 응용

include = [None] * N    # 물건이 들어가는지 들어가지 않는지 정의하는 boolean 리스트
max_value = -1
def Knapsack_powerset(k):
    
    global max_value
    
    if k == N:
        # include[i]가 True일 때의 w[i]를 추출
        w_include = [w[i] for i in range(N) if include[i]]
        weight = sum(w_include)
        if weight <= W:   # 조건에 맞는다면
            v_include = [v[i] for i in range(N) if include[i]]
            value = sum(v_include)
            
            if value > max_value:
                max_value = value
        return
    
    include[k] = False      # k번째를 제외한 나머지 수로 부분집합
    Knapsack_powerset(k+1)
    
    include[k] = True       # k번째를 포함하고 나머지 수로 부분집합
    Knapsack_powerset(k+1)

Knapsack_powerset(0)
print(max_value)
                
            
            
                
            
    
    






