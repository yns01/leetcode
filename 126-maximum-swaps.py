class Solution:
    def maximumSwap(self, num: int) -> int:
        digits_dict = {}
        digit_list = list(str(num))

        for i, d in enumerate(digit_list):
            digits_dict[d] = i

        for i, d in enumerate(digit_list):
            for candidate in range(9, int(d), -1):
                pos = digits_dict.get(str(candidate), None)

                if pos and pos > i:
                    digit_list[i], digit_list[pos] = digit_list[pos], digit_list[i]
                    return ''.join(digit_list)

        return ''.join(digit_list)

    def maximumSwapv1(self, num: int) -> int:
        digit_list = list(str(num))

        max_digit, max_digit_pos = -1, -1
        left_pos, right_pos = -1, -1

        # Going from right to left, we keep track of the maximum value position
        # If we find a smaller value than the current max, it means we found a possible
        # swap solution, left and right. So we memo the current max position as right.
        # Why? For example, 921680
        # When we reach 9, the left will be 2 and max will be 8.
        # If we use the max_pos to swap value, we will swap 9 (as it's bigger than current_max) with 2
        # This is why when we see a lower value than the current_max, we memo the max position.
        # It would also happen in with a increasing sequence: 9876523
        # The candidate for swaps are 2 and 3, but if we don't memo the position when seeing 2, the max will be 9.
        # But it's not a valid swap.
        for i in range(len(digit_list) - 1, -1, -1):
            d = int(digit_list[i])

            if d > max_digit:
                max_digit = d
                max_digit_pos = i
            elif d < max_digit:
                left_pos = i
                right_pos = max_digit_pos

        if left_pos == -1:
            return num

        digit_list[left_pos], digit_list[right_pos] = digit_list[right_pos], digit_list[left_pos]

        return ''.join(digit_list)


print(Solution().maximumSwap(921680))
