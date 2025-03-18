# 변수 입력 받기
N=int(input()) # N개의 행
arr=[[*map(int,input().split())] for _ in range(N)]

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
    
    return (x_next >= 0 &
            x_next < N &
            y_next >= 0 &
            y_next < N &
            arr[x_next][y_next] == 0)
    
def moveto(x, y, dir):
    

def solveMaze(x, y):