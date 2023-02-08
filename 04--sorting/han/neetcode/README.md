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

## Python 문자열 뒤집기(Reverse String)
```python
s = 'Reverse this strings'
s = s[::-1]
print(s)
```
- [참고](https://dongyeopblog.wordpress.com/2016/11/21/python-%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%92%A4%EC%A7%91%EA%B8%B0reverse-string/)

## Remove non-alphanumeric characters from a Python string
```python
input = "Welcome, User_12!!"
s = ''.join(filter(str.isalnum, input))
print(s)    # WelcomeUser12
```

- [참고](https://www.techiedelight.com/remove-non-alphanumeric-characters-string-python/)

## 다시 풀 문제
- [ ] <https://leetcode.com/problems/longest-consecutive-sequence/>