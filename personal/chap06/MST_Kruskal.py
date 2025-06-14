class DisjointSet:
    def __init__(self, vertices, mode='rank'):
        self.parent = {v: v for v in vertices}
        self.mode = mode
        if mode == 'rank':
            self.rank = {v: 0 for v in vertices}
        elif mode == 'size':
            self.size = {v: 1 for v in vertices}
        else:
            raise ValueError("mode는 'rank' 또는 'size'만 가능합니다.")

    # path compression
    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # path compression
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 == root2:
            return

        if self.mode == 'rank':
            # Union by rank (높이 기준)
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
        elif self.mode == 'size':
            # Weighted union (크기 기준)
            if self.size[root1] < self.size[root2]:
                self.parent[root1] = root2
                self.size[root2] += self.size[root1]
            else:
                self.parent[root2] = root1
                self.size[root1] += self.size[root2]

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def kruskal_mst(self, union_mode='rank'):
        self.edges.sort(key=lambda x: x[2])
        ds = DisjointSet(self.vertices, mode=union_mode)
        mst = []

        for u, v, weight in self.edges:
            if ds.find(u) != ds.find(v):
                mst.append((u, v, weight))
                ds.union(u, v)
            if len(mst) == len(self.vertices) - 1:
                break
        return mst



# 사용 예시 (강의자료 예시)
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
g = Graph(vertices)
g.add_edge('A', 'B', 4)
g.add_edge('B', 'C', 8)
g.add_edge('C', 'D', 7)
g.add_edge('D', 'E', 9)
g.add_edge('A', 'H', 8)
g.add_edge('B', 'H', 11)
g.add_edge('C', 'I', 2)
g.add_edge('C', 'F', 4)
g.add_edge('D', 'F', 14)
g.add_edge('I', 'H', 7)
g.add_edge('I', 'G', 6)
g.add_edge('H', 'G', 1)
g.add_edge('G', 'F', 2)

    
print("== Union by rank ==")
mst_rank = g.kruskal_mst(union_mode='rank')
for u, v, w in mst_rank:
    print(f"{u} - {v}, weight: {w}")

print("\n== Weighted union (by size) ==")
mst_size = g.kruskal_mst(union_mode='size')
for u, v, w in mst_size:
    print(f"{u} - {v}, weight: {w}")
