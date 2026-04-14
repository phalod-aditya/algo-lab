# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Two pointers ----->

        left, right = 0, len(nums)-1

        sorted_nums = sorted(nums)

        first, second = 0, 0

        while left<right:

            summ = sorted_nums[left] + sorted_nums[right]

            if summ == target:
                # print("Bingo: ", left, right)
                left_val = sorted_nums[left]
                right_val = sorted_nums[right]
                break
            
            elif summ > target:
                right-=1
            
            elif summ < target:
                left+=1

        if left_val != right_val:
            return [nums.index(left_val), nums.index(right_val)]
        else:
            first = nums.index(left_val)
            second = nums.index(left_val, first + 1)
            return [first, second]

        # Naive soln ----->

        # for i in range(len(nums)):

        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             # print("Bingo: ", i, j)
        #             return [i,j]
            
        # return 
