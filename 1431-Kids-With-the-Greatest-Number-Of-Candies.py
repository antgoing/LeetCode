class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mostcandies = max(candies)
        answer = [True] * len(candies)
        for i in range (len(candies)):
            if (candies[i] + extraCandies < mostcandies):
                answer[i] = False
        return answer
