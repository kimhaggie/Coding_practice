def DFS(cur, tickets_dict, n, visit, path):
    if len(path) == n+1:
        return path
    else:
        if not cur in tickets_dict.keys():
            return []
        ticket = tickets_dict[cur]
        for dest, idx in ticket:
            if not visit[idx]:
                visit[idx] = True
                path.append(dest)
                result = DFS(dest, tickets_dict, n, visit, path)
                if len(result) == n+1:
                    return result
                visit[idx] = False
                path.pop()
        return []

def solution(tickets):
    visit = [False for _ in range(len(tickets))]
    tickets_dict = dict()
    for idx, val in enumerate(tickets):
        if val[0] in tickets_dict.keys():
            tickets_dict[val[0]].append([val[1],idx])
        else:
            tickets_dict[val[0]] = [[val[1],idx]]
    for key in tickets_dict.keys():
        tickets_dict[key] = sorted(tickets_dict[key], key = lambda x: x[0])
    start = 'ICN'
    path = [start]
    answer = DFS(start, tickets_dict, len(tickets), visit, path)
    return answer

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [['ICN','b'],['ICN','c'],['c','ICN']]
print(solution(tickets))