class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            my_nums = {}
            for index, val  in enumerate(nums):
                curr = target - val
                if curr in my_nums:
                    return (my_nums[curr], index) 
                else:
                    my_nums[val] = index
