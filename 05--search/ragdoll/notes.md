## Graph

- 정점들을 간선으로 연결
- 트리도 일종의 그래프 (하단 두 가지 조건을 만족시킬 때)
    - 노드들이 서로 순환 참조 관계가 아닐 때
    - 연결되지 않는 노드가 없을 때
- 구성요소
    - vertex : 정점
    - edge : vertex를 연결 짓는 선
    - adjacent : edge로 연결된 관계
- https://github.com/MuseopKim/data-structures/commit/5cdd0847216b588c498a8bc16e95503c60f94911

## Search

### DFS

- 트리의 순회 방식과 마찬가지로 시작 정점 기준으로 가장 깊이 있는 정점까지 먼저 탐색. 해당 정점의 인접 정점으로 이동하며 이를 반복
- 구현 순서
    1. 현재 정점을 배열 혹은 맵에 저장
    2. 현재 정점의 인접 정점들을 순회
    3. 선택된 인접 접점이 방문하지 않았던 정점이면 해당 정점에 대해 재귀적으로 깊이 우선탐색 수행
- https://github.com/MuseopKim/data-structures/commit/e0e7c76082da4b39d787e5a7fcf5369827c33708

### BFS

- 시작 정점의 인접 정점들을 먼저 순회하고, 1depth씩 이동하며 해당 깊이의 정점을 우선 탐색
- 구현 순서
    1. 방문한 정점을 저장하고 큐에 삽입
    2. dequeue
    3. dequeue한 접점의 인접 정점을 순회
        - 인접 정점이 방문한 정점이라면 건너뛴다.
        - 방문하지 않은 접점이라면 `1.` 부터 반복한다.
- https://github.com/MuseopKim/data-structures/blob/master/rewind/src/main/java/graph/BFS.java

### Binary search

- 리스트의 중간 지점과 지속 비교하며 답을 찾는 탐색 방법
- 중간 지점과 검색 대상과의 대소비교를 통해 탐색 범위를 좁혀가기 때문에 정렬이 선행 되어야한다.
- https://github.com/MuseopKim/data-structures/blob/master/rewind/src/main/java/binarysearch/BinarySearch.java

## 다시 볼 문제

- [2178](https://www.acmicpc.net/problem/2178)
  - 기본적인 탐색 문제인 듯 한데 아예 풀지 못했다.
- [1260](https://www.acmicpc.net/problem/1260)
  - BFS, DFS 개념만 알면 풀 수 있었던 문제. 그냥 구현해보기 보다 문제로 복습하기 좋은 것 같아서 선정

