# 정리

## dict.setdefault / collections.defaultdict
```python
from collections import defaultdict
from collections import defaultdict

def countLetters(word):
    counter = defaultdict(int) # key=str value=int
    for letter in word:
        counter[letter] += 1
    return counter
```

- [참고](https://www.daleseo.com/python-collections-defaultdict/)


## 다시 풀 문제
- [ ] <https://leetcode.com/problems/longest-consecutive-sequence/>