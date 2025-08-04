class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxvolume = 0

        while left<right:
            distance = right - left
            if min(height[left], height[right])*distance > maxvolume:
                maxvolume = min(height[left], height[right])*distance
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        return maxvolume
