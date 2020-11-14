class Solution:
    def decodeString(self, s: str) -> str:
        def recurse(string: str, index):
            multiplier, current_result = 0, []

            while index < len(string):
                c = string[index]

                if c.isdigit():
                    multiplier = multiplier * 10 + int(c)
                elif c == '[':
                    # Skip '['
                    index += 1
                    (res, next_pos) = recurse(s, index)
                    # Merge result from subcalls to current result
                    current_result.extend(multiplier * res)
                    # Restore mutliplier as we used it
                    multiplier = 0
                    # Move the index to the last processed index from subcalls
                    index = next_pos
                elif c == ']':
                    return (current_result, index)
                else:
                    current_result.append(c)

                index += 1

            return current_result

        if not s:
            return s

        result = recurse(s, 0)
        return ''.join(result)

    def decodeStringv1(self, s: str) -> str:
        def recurse(string: str, start, end):
            multiplier, current_result = 0, []

            index = start
            while index < end:
                c = string[index]

                if c.isdigit():
                    multiplier = multiplier * 10 + int(c)
                elif c == '[':
                    closer_index = self.bracket_index.get(index)
                    res = recurse(s, index + 1, closer_index)
                    # Merge result from subcalls to current result
                    current_result.extend(multiplier * res)
                    # Restore mutliplier as we used it
                    multiplier = 0
                    # Move the index to the last processed index from subcalls
                    index = closer_index
                else:
                    current_result.append(c)

                index += 1

            return current_result

        def build_indexes(string: str):
            bracket_index = {}
            stack = []

            for i, c in enumerate(s):
                if c == '[':
                    stack.append(i)
                elif c == ']':
                    bracket_index[stack.pop()] = i

            return bracket_index

        if not s:
            return s

        self.bracket_index = build_indexes(s)
        result = recurse(s, 0, len(s))
        return ''.join(result)


print(Solution().decodeString('2[abc]3[cd]ef'))
