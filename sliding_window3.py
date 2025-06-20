'''Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        num_indices = {}

        for i in range(len(nums)):
            if nums[i] in num_indices:
                if i - num_indices[nums[i]] <= k:
                    return True
            num_indices[nums[i]] = i

        return False

sol = Solution()

nums = [1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1]
k = 3

print("Duplicate number found:", sol.containsNearbyDuplicate(nums, k))
