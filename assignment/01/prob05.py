# 파일 불러오기
with open("./files/maze.txt", 'r', encoding='utf-8-sig') as f:
    N = int(f.readline())
    maze = [[*map(int, f.readline().split())] for _ in range(N)]
    K = int(f.readline())

offset = [
    [-1, 0],    # 북
    [0, 1],     # 동
    [1, 0],     # 남
    [0, -1]     # 서
]

rest_count_min = -1  # 최소 휴식 횟수 (출구 못 찾으면 업데이트 X)

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

# 1. "일직선"으로 3칸까지 한번에 갈 수 있다.
# 2. 한번 이동하면 반드시 휴식을 취해야 한다.

# 일직선으로 K칸을 움직이거나 움직이는 도중 방향을 바꿀 때 1을 추가하는 형식
def solveMaze(x, y, dir, dir_before, move_count, rest_count):
    """미로의 경로를 구하는 함수입니다.

    Args:
        x (int): 현재 위치의 x좌표
        y (int): 현재 위치의 y좌표
        dir (int): 가고 싶은 방향
        dir_before (int): 이전에 향하던 방향(move_count와 함께 움직이는 도중 방향을 바꾸었는지 파악)
        move_count (int): 이동 횟수(현재 일직선으로 움직일 수 있는 한계인지 파악)
        rest_count (int): 휴식 횟수
    """
    
    global rest_count_min

    maze[x][y] = 2          # visited 표시
    
    if x == N-1 and y == N-1:   # 목적지 도착 - 최소 휴식 횟수 최신화
        # 목적지 도착한 것도 멈춘 것 - 기존의 rest_count에 + 1
        if rest_count_min == -1 or rest_count_min > rest_count+1:
            rest_count_min = rest_count+1
            
    else:
        while (dir < 4):
            
            if moveable(x, y, dir):     # 움직일 수 있으면
                
                # move_count가 "3이 될 때" / "움직인 전적이 있는데" 방향을 바꾸려 할 때
                # 쉬었고(rest_count += 1), 한 번 움직였음(move_count = 1)을 알려주기
                if (move_count == K) or (move_count != 0 and dir != dir_before):
                    solveMaze(x + offset[dir][0], y + offset[dir][1], 0, dir, 1, rest_count+1)
                    
                # 나머지 경우는 move_count 세주기 
                else:
                    solveMaze(x + offset[dir][0], y + offset[dir][1], 0, dir, move_count+1, rest_count)
                    
            dir += 1   # 방향 바꾸기
        
    maze[x][y] = 0  # 자신이 온 흔적 없애기 - 다른 경우의 수에 방해가 될 수 있으므로

solveMaze(0, 0, 0, 0, 0, 0)

print(rest_count_min)

