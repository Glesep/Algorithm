N=int(input()) # N개의 행
maze=[[*map(int,input().split())] for _ in range(N)]

K = int(input())

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
            maze[x_next][y_next] == 0)
    

## 도착 시 경로의 개수는 1개
## 도착하지 않을 시 이후 스탭에서 구해진 경로의 개수를 리턴

def solveMaze(x=0, y=0, dir=0, move_count=0):
    """미로 내에서 K번 이하로 움직인 서로 다른 경로의 개수를 반환하는 함수입니다.

    Args:
        x (int): 현재 위치의 x좌표
        y (int): 현재 위치의 y좌표
        dir (int): 가고 싶은 방향
        move_count (int): 이동 횟수
        
    Returns:
        int: 가능한 경로의 개수
    """
    
    # 조건을 먼저 다 따져준다.
    if move_count > K:  # K번을 초과 시, 이후 스텝에서 경로가 없는 것으로 간주
        return 0
    
    if x == N-1 and y == N-1:   # 목적지 도착 - 여기까지 하나의 경로임
        return 1
        

    maze[x][y] = 2          # visited 표시
    result_route = 0
            
    while (dir < 4):
                
        if moveable(x, y, dir):     # 움직일 수 있으면
            result_route += solveMaze(x+offset[dir][0], y+offset[dir][1], 0, move_count+1)
                    
        dir += 1   # 방향 바꾸기
          
    maze[x][y] = 0  # 자신이 온 흔적 없애기 - 다른 경우의 수에 방해가 될 수 있으므로
    
    return result_route

result = solveMaze()
    
print(result)