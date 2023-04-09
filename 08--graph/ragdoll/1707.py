import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
test_count = int(input())

is_even = True


def DFS(vertex: int):
    global is_even
    visited[vertex] = True

    for v in vertexes[vertex]:
        if not visited[v]:
            groups[v] = (groups[vertex] + 1) % 2
            DFS(v)
        elif groups[vertex] == groups[v]:
            is_even = False


for _ in range(test_count):
    vertex_count, edge_count = map(int, input().split())
    vertexes = [[] for _ in range(vertex_count + 1)]
    visited = [False] * (vertex_count + 1)
    groups = [0] * (vertex_count + 1)
    is_even = True

    for i in range(edge_count):
        from_vertex, to_vertex = map(int, input().split())
        vertexes[from_vertex].append(to_vertex)
        vertexes[to_vertex].append(from_vertex)

    for i in range(1, vertex_count + 1):
        if is_even:
            DFS(i)
        else:
            break

    if is_even:
        print("YES")
    else:
        print("NO")

# 혼자 힘으로 풀이 실패 함
# 문제 내용 정리
# 이분 그래프
# => 서로 인접하지 않는 두 집합으로 그래프의 노드를 나눌 수 있다는 것
# => 사이클이 발생하면 안된다고 함
# => 탐색한 노드에 다시 접근했을 때 현재 노드의 집합과 같으면 안됨
