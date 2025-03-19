# 1은 벽, 2는 폭탄

N=int(input()) # N개의 행
maze=[[*map(int,input().split())] for _ in range(N)]
K = int(input())    # 목숨 횟수

offset = [
    [-1, 0],    # 북
    [0, 1],     # 동
    [1, 0],     # 남
    [0, -1]     # 서
]

def moveable(x, y, dir):
    """
    현재 위치(x,y)에서 dir 방향으로 갈 수 있는지 확인하는 함수입니다.

    Args:
        x (int): 현재 좌표의 x값
        y (int): 현재 좌표의 y값
        dir (int): 가고 싶은 방향

    Returns:
        boolean: 갈 수 있으면 True, 아니면 False
    """
    x_next = x + offset[dir][0]
    y_next = y + offset[dir][1]
    
    return (x_next >= 0 and
            x_next < N and
            y_next >= 0 and
            y_next < N and
            (maze[x_next][y_next] == 0 or
             maze[x_next][y_next] == 2))


canGo = False   # 갈 수 있는지 확인하는 플래그

def solveMaze(x, y, dir, life_coin):
    """미로의 경로를 구하는 함수입니다.

    Args:
        x (int): 현재 위치의 x좌표
        y (int): 현재 위치의 y좌표
        dir (int): 가고 싶은 방향
        life_coin (int): 남은 부상 가능한 횟수
    """
    global canGo
    
    isBomb = False  # 흔적 지울 때, Bomb인지 확인하기 위해
    
    if maze[x][y] == 2:     # 폭탄 밟았을 때
        isBomb = True
        
    maze[x][y] = 3         # visited 표시
    
    if life_coin >= 0:      # 조건 충족 (살아있음)
        
        if x == N-1 and y == N-1:   # 목적지 도착
            canGo = True
        
        else:
            while (dir < 4):
                
                if moveable(x, y, dir):     # 움직일 수 있으면
                    if isBomb:
                        solveMaze(x+offset[dir][0], y+offset[dir][1], 0, life_coin-1)
                    else:
                        solveMaze(x+offset[dir][0], y+offset[dir][1], 0, life_coin)
                    
                dir += 1   # 방향 바꾸기
                
    if isBomb:
        maze[x][y] = 2
    else:
        maze[x][y] = 0  # 자신이 온 흔적 없애기 - 다른 경우의 수에 방해가 될 수 있으므로

solveMaze(0, 0, 0, K)

if canGo:
    print('Yes')
else:
    print('No')