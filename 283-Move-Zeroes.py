class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        r = len(nums)

        while (l<r):
            if nums[l] == 0:
                del nums[l]
                nums.append(0)

                r-=1
            else:
                l+=1
