with open('./files/input1.txt') as f:
    x, y = map(int, f.readline().split())
    adj_matrix = [[-1 for _ in range(y)] for _ in range(x)]
    # print(adj_matrix)
    for i in range(x):
        adj_matrix[i][i] = 0
        
    for line in f:
        n1, n2, w = map(int, line.split())  # split한 요소들을 int화
        adj_matrix[n1][n2] = w
        adj_matrix[n2][n1] = w

# 인접행렬 출력
for row in range(x):
    for col in range(y):
        print(adj_matrix[row][col], end=' ')
    print()

# 연결 요소 출력
visited = [False] * x
components = []

def dfs(v, component):
    visited[v] = True
    component.append(v)
    for u in range(y):
        if (adj_matrix[v][u] != -1 and adj_matrix[v][u] != 0) and not visited[u]: # 열의 요소들을 탐색
            dfs(u, component)

for v in range(x):
    if not visited[v]:
        component = []
        dfs(v, component)
        components.append(component)
print(components)
