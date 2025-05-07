from collections import deque

class Node:
    def __init__(self, 
                 key,
                 left_key,
                 right_key):
        self.val = key
        self.left_val = left_key        # 왼쪽 자식 노드의 값
        self.right_val = right_key      # 오른쪽 자식 노드의 값
        self.left = None    # 왼쪽 자식 노드
        self.right = None   # 오른쪽 자식 노드
        self.parent = None  # 부모 노드 참조
        
def inorder_traversal(node):
    res = []
    if node:    # 노드 != NIL
        res = inorder_traversal(node.left)
        res.append(node.val)
        res = res + inorder_traversal(node.right)
    return res
    
def preorder_traversal(node):
    res = []
    if node:    # 노드 != NIL
        res.append(node.val)
        res = res + preorder_traversal(node.left)
        res = res + preorder_traversal(node.right)
    return res
    
def postorder_traversal(node):
    res = []
    if node:    # 노드 != NIL
        res = postorder_traversal(node.left)
        res = res + postorder_traversal(node.right)
        res.append(node.val)
    return res

# ========================================================================================

with open("./files/input1.txt", 'r', encoding='utf-8-sig') as f:
    N = int(f.readline())
    node_target = deque()
    node_nontarget = list()
    
    # Node 객체를 생성하여 leaf노드는 deque에, internal node는 list에 각각 저장
    for _ in range(N):
        key, left_val, right_val = map(int, f.readline().split())
        # print (key, left_val, right_val)
        node = Node(key, left_val, right_val)
        
        if left_val == -1 and right_val == -1:      # leaf 노드라면
            node_target.append(node)
        else:
            node_nontarget.append(node)
        


# 현재 다른 노드의 자식노드로 들어갈 후보군을 node_target(dequeue)로 넣고
# 이후 node_target이 FIFO로 target node를 하나씩 꺼낸다.
# target node를 자식으로 삼는 node가 node_nontarget(list)에 있을 경우, 서로 연결해주고 부모노드를 deque에 다시 넣는다.
# 이미 부모노드가 deque에 들어있으면 다시 넣지 않는다.
# 이는 node_nontarget이 empty할 때까지 반복한다.

while node_nontarget:   # node_nontarget에 아무것도 들어있지 않을 때까지 반복
    target = node_target.popleft()  # FIFO Queue 형식으로 사용
    isParent = False
    
    if target in node_nontarget:
        node_nontarget.remove(target)
    
    for candidate in node_nontarget:    # 리스트가 비어있으면 다음 단계로
        # print(candidate.val, '\n')
        if candidate.left_val == target.val:
            candidate.left = target
            isParent = True
            
            
        elif candidate.right_val == target.val:
            candidate.right = target
            isParent = True
            
        if isParent:
            target.parent = candidate
            if candidate not in node_target:
                node_target.append(candidate)
            isParent = False
            break

# 마지막에 target에 저장된 노드가 root     
root = target

# * : 리스트 요소들을 언패킹
print(*preorder_traversal(root))
print(*inorder_traversal(root))
print(*postorder_traversal(root))