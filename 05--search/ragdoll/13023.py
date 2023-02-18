people_count, relation_count = map(int, input().split())

relations = [[] for i in range(people_count + 1)]
visited = [False] * (people_count + 1)
find_count = 5

result = 0


def DFS(vertex: int, count: int) -> None:
    if count == find_count:
        global result
        result = 1
        return

    visited[vertex] = True
    count += 1

    for adjacent_vertex in relations[vertex]:
        if not visited[adjacent_vertex]:
            DFS(adjacent_vertex, count)

    visited[vertex] = False


for _ in range(relation_count):
    person1, person2 = map(int, input().split())
    relations[person1].append(person2)
    relations[person2].append(person1)

for i in range(len(relations)):
    for friend in relations[i]:
        count = 1
        DFS(friend, count)

    if result == 1:
        break

print(result)
