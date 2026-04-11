class Solution:
    def search(self, nums: List[int], target: int) -> int:
        indices = range(len(nums))
        dict_nums = dict(zip(nums, indices))
        if target in dict_nums:
            return dict_nums[target]
        else:
            return -1
