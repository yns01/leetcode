class Solution:
    def findMin(self, nums):
        if nums[-1] > nums[0]:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2

            if nums[mid-1] > nums[mid] < nums[mid+1]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid
            else:
                right = mid

        return min(nums[left], nums[right])
