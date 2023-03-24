def gcd(A: int, B: int):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)


A, B = map(int, input())
result = gcd(A, B)

while result > 0:
    print(1, end='')
    result -= 1

# 큰쪽에서 작은 쪽을 나눠서 떨어지면 작은 쪽이 최대 공약수
# 나누어 떨어지지 않으면 1, 0이면 나머지 하나가 최대공약 수
