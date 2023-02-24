# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = 0
#
#         lowest = prices[0]
#         for price in prices:
#             if price < lowest:
#                 lowest = price
#             res = max(res, price - lowest)
#         return res
# 더 쉬운 방법

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        max_profit = 0
        l = 0 # buying
        r = 1 # selling

        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l == r
            r += 1

        return max_profit



# 문제 해석
# prices 배열이 주어지고, i는 i 번째 일자의 가격을 의미함.
# 가장 낮은 값에서 가장 높은 값 때 팔면됨.
# 이익을 그대화해야함. 하나의 날짜 무터 다른 날짜까지 해서..
# 2중 for 문 -> 시간 초과 198 / 211 testcases passed

# sudo code

# 제한사항
# 1 <= prices.length <= 10^5 -> 이중 포문으로 풀긴 어려울듯


