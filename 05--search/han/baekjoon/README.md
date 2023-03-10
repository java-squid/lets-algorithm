# 정리

## DFS
- 그래프 탐색의 한 종류
- 그래프의 한쪽을 최대 깊이까지 탐색한 후 후, 다른쪽 분기로 이동하는 것.
- 한번 방문한 노드는 다시 방문하면 안된다 -> 방문했는지 안했는지 체크할 리스트가 필요.
- 보통 재귀를 많이 이용 (혹은 스택)

## 소수 판별
- https://seongonion.tistory.com/43

## BFS
- Queue 많이 이용
- 시작노드 부터 가까운 노드를 먼저 방문하면서, 탐색하는 알고리즘
- 방문했던 노드는 다시 방문하지 않도록 체크하는게 필요
- 진행 방식은..
  1. 큐에 시작점을 더하고
  2. 큐에서 하나 꺼내서, popleft(), 인접 노드 모두를 넣음.
  3. 넣을 때, 방문했던 노드면 넣지 않고.
  4. 이제 2번으로 다시 돌아감. (큐에 남는 노드가 없을 때까지, 그럼 모든 노드를 탐색하게됨.)

## 이진 탐색
- binary search
- 데이터가 정렬된 상태에서 원하는 값을 찾는 알고리즘 (데이터 정렬이 핵심)
- 시간 복잡도 O(logN)
- 탐색 방법 (데이터가 오름 차순 일 때)
  1. 현재 데이터의 중앙값 선택
  2. 찾고자 하는 데이터 = 타겟 값이 중앙값 보다 크다면(target > median), 오른쪽 데이터 셋을 선택, 
  3. target < median 이면 왼쪽 데이터 셋 선택
  4. 2~3번 과정 반복하면서 원하는 값 찾음.

## 다시 풀어보기
- [v] <https://www.acmicpc.net/problem/11724>
- [v] <https://www.acmicpc.net/problem/2023>
- [v] <https://www.acmicpc.net/problem/1260>
- [ ] <https://www.acmicpc.net/problem/1300>
- [ ] <https://www.acmicpc.net/problem/13023>
- [ ] <https://www.acmicpc.net/problem/2178>