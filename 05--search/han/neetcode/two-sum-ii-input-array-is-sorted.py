class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}


        for i in range(len(numbers)):
            dic[numbers[i]] = i

        for i in range(len(numbers)):
            res = target - numbers[i]
            if res in dic and i != dic[res]:
                return sorted([i + 1, dic[res] + 1])

        return []

# 문제해석
# already sorted in non-decreasing order -> 이미 오름차순으로 정렬된 배열이 주어짐
# 2개의 number가 더해서 target이 되는 인덱스를 알아야함, 리턴은 인덱스로
# You may not use the same element twice -> 같은 값을 사용하면 안됨.
# 0(1) 의 extra space만 이용

# 시간복잡도는 O(N)

# sudo code
# 1. dict을 이용하면 되지 않을까?
# 2.

# 참고
# numbers.length >= 2 -> base case는 필요없지 않을까

