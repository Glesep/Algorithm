import math


# CCW: Counter-Clockwise -> 양수 - 반시계, 음수 - 
# p0 출발 p2 도착
def ccw(p, q, r):
    val = (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1])

    if val == 0:
        return 0
    return 1 if val > 0 else -1     # 반시계: 1, 시계: -1

def sort_nonclockwise_hull(hull):
    """hull 내의 좌표들을 반시계방향으로 정렬합니다.

    Args:
        hull (list): 정렬하고싶은 리스트

    Returns:
        list: 반시계방향으로 정렬된 리스트
    """
    # 중심을 기준으로 각 점을 정렬
    center_x = sum(p[0] for p in hull) / len(hull)
    center_y = sum(p[1] for p in hull) / len(hull)
    center = (center_x, center_y)
    
    # math.atan2(y, x)는 주어진 좌표 (x, y)를 기준으로 원점에서의 극각(각도)을 반환
    # 각이 작은 순에서 큰 순으로 정렬 (각이 커지니 반시계방향 정렬. 사분면 생각)
    hull.sort(key=lambda p: math.atan2(p[1] - center[1], p[0] - center[0]))
    return hull

def merge_hulls(left_hull, right_hull):
    """좌측과 우측 hull들을 반시계방향으로 합치는 함수입니다.

    Args:
        left_hull (list): 좌측 hull
        right_hull (list): 우측 hull

    Returns:
        list: 반시계방향으로 합쳐진 하나의 hull
    """
    
    left_index = max(range(len(left_hull)), key=lambda x: left_hull[x][0])
    right_index = min(range(len(right_hull)), key=lambda x: right_hull[x][0])
    
    while True:
        changed = False
        
        
        # 우회전인지 확인 = (p,q)에서 (p,r)로 변했을 때 반시계방향으로 도는지 확인(hull의 방향 x)
        while ccw(right_hull[right_index], left_hull[left_index], left_hull[(left_index + 1) % len(left_hull)]) == -1:
            left_index = (left_index+1) % len(left_hull)        # 원형 배열을 사용. hull은 반시계 정렬되어있으므로 반시계 방향 진행 시 좌표 +1
            changed = True
        
        # 좌회전인지 확인 = (p,q)에서 (p,r)로 변했을 때 시계방향으로 도는지 확인(hull의 방향 x)
        while ccw(left_hull[left_index], right_hull[right_index], right_hull[(right_index - 1) % len(right_hull)]) == 1:
            right_index = (right_index-1) % len(right_hull)        # 원형 배열을 사용 hull은 반시계 정렬되어있으므로 시계 방향 진행 시 좌표 -1
            changed = True
        
        if not changed:
            break
        
    upper_left, upper_right = left_index, right_index
    
    left_index = max(range(len(left_hull)), key=lambda x: left_hull[x][0])
    right_index = min(range(len(right_hull)), key=lambda x: right_hull[x][0])
    
    while True:
        changed = False
        
        
        # 좌회전인지 확인 = (p,q)에서 (p,r)로 변했을 때 반시계방향으로 도는지 확인(hull의 방향 x)
        while ccw(right_hull[right_index], left_hull[left_index], left_hull[(left_index - 1) % len(left_hull)]) == 1:
            left_index = (left_index-1) % len(left_hull)        # 원형 배열을 사용 hull은 반시계 정렬되어있으므로 시계 방향 진행 시 좌표 -1
            changed = True
        
        # 우회전인지 확인 = (p,q)에서 (p,r)로 변했을 때 반시계방향으로 도는지 확인(hull의 방향 x)
        while ccw(left_hull[left_index], right_hull[right_index], right_hull[(right_index + 1) % len(right_hull)]) == -1:
            right_index = (right_index+1) % len(right_hull)        # 원형 배열을 사용 hull은 반시계 정렬되어있으므로 반시계 방향 진행 시 좌표 +1
            changed = True
        
        if not changed:
            break
        
    lower_left, lower_right = left_index, right_index
    
    
    # hull을 반시계 방향으로 병합함
    result = []
    idx = upper_left
    while idx != lower_left:
        result.append(left_hull[idx])
        idx = (idx + 1) % len(left_hull)
    result.append(left_hull[lower_left])

    idx = lower_right
    while idx != upper_right:
        result.append(right_hull[idx])
        idx = (idx + 1) % len(right_hull)
    result.append(right_hull[upper_right])

    return result
    
    
    
    

def divide_and_conquer(points):
    """x좌표로 정렬된 points 리스트를 분할정복하는 함수입니다.

    Args:
        points (list): x좌표로 정렬된 리스트

    Returns:
        list: 각 시점에서 좌측 hull과 우측 hull을 합병한 리스트
    """
    if len(points) <= 3:
        # base case : 직접 convex hull을 제작
        
        if len(points) == 3 and ccw(points[0], points[1], points[2]) == 0:
            return [points[0], points[2]]        
        
        sort_nonclockwise_hull(points)   # 여기에서 hull의 반시계 방향성을 유지시켜줘야 함
        return points

    mid = len(points)//2
    left_points = points[:mid]
    right_points = points[mid:]
    
    # 분할
    left_hull = divide_and_conquer(left_points)
    right_hull = divide_and_conquer(right_points)
    
    # 병합
    return merge_hulls(left_hull, right_hull)



def convex_hull(points):
    """points(이차원 배열) 내 점들을 x좌표를 기준으로 정렬 후, 분할정복을 한 결과(convex hull의 좌표들)를 반환하는 함수입니다.

    Args:
        points (list): 일차원 리스트로 이루어진 좌표들을 저장한 리스트 (이차원 리스트)

    Returns:
        list: convex hull의 좌표들
    """
    # x축을 기준으로 정렬
    points.sort(key=lambda x: x[0])
    return divide_and_conquer(points)


with open('./files/input.txt') as f:
    node_count = int(f.readline())
    tmp = f.readlines()
    points = [[int(j) for j in i.strip().split()] for i in tmp]
    
hull = convex_hull(points)
print("Convex Hull:", hull)