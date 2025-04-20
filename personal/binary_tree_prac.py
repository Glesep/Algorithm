from collections import deque

class Node:
    def __init__(self, key, parent=None):
        self.val = key
        self.left = None
        self.right = None
        self.parent = parent  # 부모 노드 참조

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node):
        y = None
        x = self.root
        
        while x != None:
            # x가 NIL 이 될때까지 타고 감 - y를 뒤따라오게함
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if node.parent == None:
            self.root = node
        elif node.val < node.parent.val:
            node.parent.left = node
        else:
            node.parent.right = node
    
    def delete(self, node_del_forLogic):
        
        if node_del_forLogic.left == None or node_del_forLogic.right == None:
            node_del_forReal = node_del_forLogic
        else:
            node_del_forReal = self.tree_successor(node_del_forLogic)
        
        if node_del_forReal.left != None:   # 자식이 0개 아니면 1개 - 오른쪽 자식은 무조건 없음
            x = node_del_forReal.left
        else:
            x = node_del_forReal.right      # 만약 오른쪽 있으면 오른쪽 들어가고 없으면 None
        
        # 실제 삭제되어야 하는 노드를 삭제
        if x != None:       # node_del_forReal를 삭제하고 삭제된 노드의 부모를 자신의 부모로 삼음 
            x.parent = node_del_forReal.parent
        
        if node_del_forReal.parent == None:
            self.root = x
        
        elif node_del_forReal == node_del_forReal.parent.left:
            node_del_forReal.parent.left = x
        
        else:
            node_del_forReal.parent.right = x
            
        if node_del_forReal != node_del_forLogic:       # successor 위치를 대신 삭제하는 경우
            
            # 자식 노드 관계는 위에서 다 정리됨. 나머지 데이터만 들고오기
            node_del_forLogic.val = node_del_forReal.val
            node_del_forLogic.parent = node_del_forReal.parent

        return node_del_forReal.val
        
        
        
        
    def search(self, x, k):
        
        if x == None or k == x.val:
            return x
        
        if k < x.val:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)
        
    def tree_min(self, x):
        while x.left != None:
            x = x.left
            
        return x
    
    def tree_max(self, x):
        while x.right != None:
            x = x.right
            
        return x
    
    def tree_successor(self, x):
        if x.right != None:
            return self.tree_min(x.right)
        x_parent = x.parent
        
        while x_parent != None and x == x_parent.right:
            x = x_parent
            x_parent = x_parent.parent
        
        return x_parent
    
    def tree_predecessor(self, x):
        if x.right != None:
            return self.tree_max(x.left)
        x_parent = x.parent
        
        while x_parent != None and x == x_parent.left:
            x = x_parent
            x_parent = x_parent.parent
        
        return x_parent
    
    def inorder_traversal(self, node):
        res = []
        if node:    # 노드 != NIL
            res = self.inorder_traversal(node.left)
            res.append(node.val)
            res = res + self.inorder_traversal(node.right)
        return res
    
    def preorder_traversal(self, node):
        res = []
        if node:    # 노드 != NIL
            res.append(node.val)
            res = res + self.preorder_traversal(node.left)
            res = res + self.preorder_traversal(node.right)
        return res
    
    def postorder_traversal(self, node):
        res = []
        if node:    # 노드 != NIL
            res = self.postorder_traversal(node.left)
            res = res + self.postorder_traversal(node.right)
            res.append(node.val)
        return res
    
    def level_order_traversal(self):
        res = []
        if not self.root:
            return res
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
            

def isBST(root, lower=None, upper=None):
    
    if root == None:
        return True
    
    if (lower != None and root.val < lower) or (upper != None and root.val > upper):
        return False
    
    return isBST(root.left, lower, root.val) and isBST(root.right, root.val, upper)


# 루트에서 노드까지의 깊이 찾기
def get_depth(node):
    depth = 0 
    while node:
        node = node.parent
        depth += 1
        
    return depth

# 최소 공통 조상 찾기 - 14번
def lowest_common_ancestor(node1, node2):
    
    depth1 = get_depth(node1)   # node1 깊이 - 루트부터 node1까지
    depth2 = get_depth(node2)   # node2 깊이 - 루트부터 node2까지
    
    # 깊이 맞춰주기 - 둘 중 하나 실행
    while depth1 > depth2:     
        node1 = node1.parent
        depth1 -= 1
    
    while depth1 < depth2:
        node2 = node2.parent
        depth2 -= 1
        
        
    # 깊이가 서로 맞았으면 하나씩 올리면서 둘이 같아질 때까지 찾음    
    while node1 != node2:
        node1 = node1.parent
        node2 = node2.parent
        
    return node1
    



# ================================================================================

bt = BST()
for v in [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]:
    bt.insert(Node(v))

if isBST(bt.root):
    print ('BST입니다!!')
else:
    print ('BST 아닙니다...')
    

print(bt.level_order_traversal())
print(bt.inorder_traversal(bt.root))
print(bt.preorder_traversal(bt.root))
print(bt.postorder_traversal(bt.root))


    
        
            
            
