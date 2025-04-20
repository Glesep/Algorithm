class Node:
    def __init__(self, val, color, left=None, right=None):
        self.val = val
        self.color = color  # 'R' for red, 'B' for black
        self.left = left
        self.right = right

def is_red(node):
    if node is None:
        return False
    return node.color == 'R'

def is_red_black_tree(node):
    if node is None:
        return True, 1  # Null 노드는 black, black height 1

    # (1) Red-Black 트리의 조건: red 노드는 red 자식을 가질 수 없음
    if is_red(node):
        if is_red(node.left) or is_red(node.right):
            return False, 0

    # (2) 왼쪽과 오른쪽 서브트리 각각 검사
    left_valid, left_black_height = is_red_black_tree(node.left)
    right_valid, right_black_height = is_red_black_tree(node.right)

    # (3) 두 서브트리가 모두 유효하고 black height가 같아야 함
    if not left_valid or not right_valid or left_black_height != right_black_height:
        return False, 0

    # (4) 현재 노드의 black height 계산
    black_height = left_black_height + (1 if node.color == 'B' else 0)

    return True, black_height

def check_red_black_tree(root):
    valid, _ = is_red_black_tree(root)
    return valid
