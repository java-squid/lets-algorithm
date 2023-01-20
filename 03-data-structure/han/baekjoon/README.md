# 문제 풀면서 배운점 정리

## split()
```python
list(input().split())  
```
-  split default separator is any whitespace

## list comprehension

```python
 scores_i = [int(i) for i in scores]  
```

- list comprehension 
- string list cast to int list

## sys.stdin.readline

```python
import sys
input = sys.stdin.readline
```

- 반복문으로 여러 입력을 받는 상황에서는 시간초과를 방지하기 위해 사용해야하는듯.
- https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline

## prefix sum
- 구간합 알고리즘
- https://www.crocus.co.kr/843
- https://en.wikipedia.org/wiki/Prefix_sum 읽어봐도 좋을듯.

## nC2
- NC2 = `n * (n-1) / 2` -> `C[i] * (C[i] - 1) / 2`
- https://www.quora.com/What-is-the-value-of-N-in-NC2

## / vs //

```python
>>> 5 / 2
2.5
>>> 5 // 2
2
```
- / -> float division
- // -> integer division


## 슬라이딩 윈도우
- 지정된 길이가 있으면, 그 길이를 유지하면서 한칸씩 옆으로 이동하는 기법을 말함.

## Deque
- 양방향 큐
- 양끝에 엘리먼트를 추가 혹은 제거가 O(1) 시간복잡도를 가짐
- `popleft()` 왼쪽에서 pop 


## 다시 풀 문제
- [v] <https://www.acmicpc.net/problem/11986>
- [ ] <https://www.acmicpc.net/problem/2018>
- [ ] <https://www.acmicpc.net/problem/11659>
- [ ] <https://www.acmicpc.net/problem/11660>
- [ ] <https://www.acmicpc.net/problem/1253>
- [ ] <https://www.acmicpc.net/problem/12891>
- [ ] <https://www.acmicpc.net/problem/11003>