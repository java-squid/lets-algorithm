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