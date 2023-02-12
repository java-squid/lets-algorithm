class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        # O(n)
        for num in nums:
            counter[num] = counter.setdefault(num, 0) + 1

        # frequency 로 정렬하고, 그 중 K개만큼 잘라서 튜플형태로 반환
        # 시간복잡도 0(nlogn)
        sort = sorted(counter.items(), key=lambda kv: kv[1], reverse=True)[:k]

        result = []

        # O (n)
        for num, frequency in sort:
            result.append(num)

        return result
        # return [sort[i][0] for i in range(k)]


# 문제 이해
# 리스트가 주어지는데, k 숫자만큼 빈도수 만큼 리스트로 반환
# 이 리스트가 정렬되어 있나?
# 즉  nums = [1,1,1,2,2,3], k = 2 라면 가장 많은 빈도수를 보이는 1, 그다음 2 [1,2] 가 반환되어야함.

# 제한 사항
# nums.length = 1 일수 있음 -> base condition 필요할수도.


# 수도 코드
# 리스트를 돌면서, 몇번 나왔는지 카운트 하고.
# 값으로 정렬하여 가장 많이 나온 K개만큼 리턴하는 방법.

# counter = {}
# for num in nums:
#      count[num] += 1
#
# sorted counter by value and slice key by k
# k 만큼 나온 tuple num만 뽑아서 리스트로 리턴

# 참고
# https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary