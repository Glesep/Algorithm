with open('./files/input9.txt', 'r', encoding='utf-8-sig') as f:
    N = int(f.readline())
    potential = [[*map(int, f.readline().split())] for _ in range(N)]
    k = int(f.readline())

include = [None] * N
max_potential = None        # 최대 능력치

# N명의 선수로 구성할 수 있는 모든 경우의 수 중에서
# k명으로 이루어진 팀을 모두 확인 - 멱집합의 응용
# 그 중 능력이 최대가 되는 팀을 확인


def Team_powerset(x):
    """
    멱집합을 구하는 알고리즘을 이용하여 모든 경우의 수를 확인 후, </br>
    조건에 맞는 답을 추출해내는 함수입니다.

    Args:
        k (int): 멱집합 알고리즘의 상태이상트리에서 현재 위치. 기본값:0
    """
    global max_potential
    
    if x == N:
        if include.count(True) == k:    # k명으로 팀이 이루어졌을 때
            
            team_potential = 0
            player_index = [index for index in range(N) if include[index]]
            
            for i in player_index:  # 팀 능력치 계산
                for j in player_index:
                    team_potential += potential[i][j]
            
            # 처음 계산되었거나 현재 계산된 능력치가 최대일 때
            if max_potential == None or team_potential > max_potential:
                max_potential = team_potential 
        
        return
        
    
    include[x] = False      # x번째를 제외한 나머지 수로 부분집합
    Team_powerset(x+1)
    
    include[x] = True       # x번째를 포함하고 나머지 수로 부분집합
    Team_powerset(x+1)
    
    
Team_powerset(0)
print(max_potential)

