# 정리

## 에라토스테네스의 체

> 1~30 까지 수 중에 소수를 구하라 
> 소수 ? 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수

1. 주어진 범위의 리스트 생성 (1 ~ 30)
   - 1은 소수가 아니므로 제거 (위 리스트에서 2부터 시작)
2. 선택한 수의 배수를 모두 제거
   - 2의 배수 제거, 3의 배수 제거.. 모든 리스트를 확인
3. 2번 과정에서 삭제되지 않는 수를 모두 출력 (소수임)

## 다시 풀기
- [ ] <>