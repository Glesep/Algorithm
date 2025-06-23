# 키보드 입력 받기

size = int(input())

adj_matrix = []

for _ in range(size):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

# 인접행렬 출력
for row in range(size):
    for col in range(size):
        print(adj_matrix[row][col], end=' ')
    print()
    
    
# 연결 요소 출력
visited = [False] * size
components = []

def dfs(v, component):
    visited[v] = True
    component.append(v)
    for u in range(size):
        if (adj_matrix[v][u] != -1 and adj_matrix[v][u] != 0) and not visited[u]: # 열의 요소들을 탐색
            dfs(u, component)

for v in range(size):
    if not visited[v]:
        component = []
        dfs(v, component)
        components.append(component)


for component in components:
    print(len(component), end=' ')
print()