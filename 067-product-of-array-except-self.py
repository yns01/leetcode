from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return

        products = []
        product = 1
        for n in nums:
            products.append(product)
            product *= n

        product_so_far = 1

        for i in range(len(products)-1, -1, -1):
            products[i] = products[i] * product_so_far
            product_so_far *= nums[i]

        return products


print(Solution().productExceptSelf([1, 2, 3, 4]))
