class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        if not binaryMatrix:
            return -1

        rows, cols = binaryMatrix.dimensions()
        if not rows or not cols:
            return -1

        r, c = 0, cols - 1
        answer = -1

        while r < rows and c >= 0:
            if binaryMatrix.get(r, c) == 1:
                answer = c
                c -= 1
            else:
                r += 1

        return answer
