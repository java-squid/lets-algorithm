# 정리

## 그리드 알고리즘
- 수행 과정
  1. 해 선택 (가장 최선의 해선택)
  2. 적절성 검사 (현재 선택한 해가 제약 조건에 벗어나지 않는지 검사)
  3. 해 검사 (현재까지 선택한 해 집합이 전체 문제를 해결할 수 있는지 검사, 안되면 1번으로 돌아감)
- 그리드 알고리즘에서는 우선순위 큐를 많이 이용함.

```python
# import pq
from queue import PriorityQueue

# instance
q = PriorityQueue()

# import heapq
import heapq

# how to use
l = []
data = 'data'
heapq.heappush(l, data)

```

## Sorted

```python
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sorted(student_tuples, key=lambda student: student[2]) # sorted by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

- https://docs.python.org/ko/3/howto/sorting.html

## 다시 풀기
- [ ] <https://www.acmicpc.net/problem/11047>
- [ ] <https://www.acmicpc.net/problem/1931>