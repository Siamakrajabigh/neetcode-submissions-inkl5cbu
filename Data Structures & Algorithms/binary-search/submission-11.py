class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2  # Safer calculation
            if nums[mid] == target:
                return mid  # Fixed: return the index when found
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1