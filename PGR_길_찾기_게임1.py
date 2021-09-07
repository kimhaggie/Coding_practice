import sys
sys.setrecursionlimit(10**6)

preorder = []
postorder = []

def pre(node,cur):
    global preorder
    preorder.append(cur+1)
    for idx,child in enumerate(node[cur]):
        if idx==2:
            break
        if child!=-1:
            pre(node,child)

def post(node,cur):
    global postorder
    for idx,child in enumerate(node[cur]):
        if idx==2:
            break
        if child!=-1:
            post(node,child)
    postorder.append(cur+1)

def solution(nodeinfo):
    if len(nodeinfo)==1:
        return [[1],[1]]
    answer = [[]]
    #left right parent
    node = [[-1,-1,-1] for _ in range(len(nodeinfo))]
    visit = [False for _ in range(len(nodeinfo))]
    max_level = 0
    for val in nodeinfo:
        if max_level < val[1]:
            max_level = val[1]
    level = [[] for _ in range(max_level+1)]
    #x좌표, node 번호
    for idx, val in enumerate(nodeinfo):
        level[val[1]].append([val[0],idx])
    new_level = []
    for idx, val in enumerate(level):
        if val:
            new_level.append(sorted(val))
    level = new_level
    # print(level)
    cur_level = len(level)-1
    # import pdb;pdb.set_trace()
    while True:
        if cur_level == 0:
            break
        if cur_level == len(level)-1:#root
            next_level = cur_level-1
            root = level[cur_level][0]
            for a,b in level[next_level]:
                if a < root[0]:
                    node[root[1]][0] = b
                    node[b][2] = root[1]
                else:
                    node[root[1]][1] = b
                    node[b][2] = root[1]
        else:
            next_level = cur_level-1
            for cur in level[cur_level]:
                LB = -1
                RB = float('inf')
                parent = cur[1]
                while LB==-1 or RB==float('inf'):
                    parent = node[parent][2]
                    if parent==-1:
                        break
                    parent_x = nodeinfo[parent][0]
                    if parent_x<cur[0] and LB == -1:
                        LB = parent_x
                    if cur[0]<parent_x and RB == float('inf'):
                        RB = parent_x
                for child in level[next_level]:
                    if visit[child[1]]:
                        continue
                    if LB<child[0]<cur[0]:#left
                        node[cur[1]][0] = child[1]
                        node[child[1]][2] = cur[1]
                        visit[child[1]] = True
                    if cur[0]<child[0]<RB:#right
                        node[cur[1]][1] = child[1]
                        node[child[1]][2] = cur[1]
                        visit[child[1]] = True
        cur_level -= 1
    pre(node,root[1])
    post(node,root[1])
    return [preorder,postorder]

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
nodeinfo = [[1,1],[2,2],[3,1],[4,3],[5,1],[6,2],[7,1],[8,4],[9,1],[10,2],[11,1],[12,3],[13,1],[14,2],[15,1]]
# nodeinfo = [[2,2],[3,1]]
# nodeinfo = [[3,3]]
# nodeinfo = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# nodeinfo = [[1,3],[2,2],[3,1]]
# nodeinfo = [[4,3],[2,4],[10,5],[15,4],[13,3],[11,1]]
nodeinfo = [[0,0],[1,1]]
print(solution(nodeinfo))