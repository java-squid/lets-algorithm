# 정리

## python print list without spaces

```python
list_of_strings = ['bobby', 'hadz', '.com']

print(*list_of_strings, sep='')  # 👉️ bobbyhadz.com
print(*list_of_strings, sep=',')  # 👉️ bobby,hadz,.com

# ---------------------------------------------

list_of_numbers = [44, 22, 88]

print(*list_of_numbers, sep='')  # 👉️ 442288
print(*list_of_numbers, sep=',')  # 👉️ 44,22,88

```

- [참고](https://bobbyhadz.com/blog/python-print-list-without-spaces)