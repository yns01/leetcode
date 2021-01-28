from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set, sequence = set(nums), set()
        seq_len, res = 0, 0
        # For each number we try to build the longest possible sequence
        # However, to avoid going quadratic, we only expand the sequence
        # if we haven't use the number if a previous sequence.
        # Why? Because the first time we expanded a much as possible the
        # sequence we are about to explore is going to be the same
        for n in nums:
            if n in sequence:
                continue

            seq_len = 1
            for n_seq in range(n+1, len(nums) + 1):
                if n_seq not in nums_set or n_seq in sequence:
                    break

                seq_len += 1
                sequence.add(n_seq)

            for n_seq in range(n-1, (n-1) - len(nums), -1):
                if n_seq not in nums_set or n_seq in sequence:
                    break

                seq_len += 1
                sequence.add(n_seq)

            res = max(res, seq_len)

        return res


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(Solution().longestConsecutive([1, 2, 3, 5, 2, 4]))
