import collections


class Solution:

    def __init__(self):
        self.units = {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
        }

        self.tens = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
        }

        self.decades = {
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
        }

        self.qualifier = {
            10: '',
            100: 'Hundred',
            1000: 'Thousand',
            10000: 'Million',
            100000: 'Billion',
            1000000: 'Trillion',
            10000000: 'Quadrillion',
            100000000: 'Quintillion',
            1000000000: 'Sextillion',
            10000000000: 'Septillion',
            100000000000: 'Octillion',
            1000000000000: 'Nonillion',
            10000000000000: 'Decillion',
        }

    def numberToWords(self, num: int) -> str:
        # FIXME: Zero?
        chunks = self.build_chunks(num)
        print(chunks)

        qualifier = 100
        result = []
        for c in chunks:
            if len(chunks) > 1 and c == 0:
                qualifier *= 10
                continue
            converted_chunk = self.convert_chunk(c)
            if qualifier > 100:
                converted_chunk += ' ' + self.qualifier[qualifier]

            result.append(converted_chunk)
            qualifier *= 10

        result.reverse()

        return ' '.join(result)

    def build_chunks(self, nums: int):
        nums = str(nums)
        res = []
        tmp = []

        if len(nums) <= 3:
            res.append(int(''.join((nums))))
            return res

        for i in range(len(nums)-1, -1, -1):
            if len(tmp) == 3:
                res.append(int(''.join(reversed(tmp))))
                tmp.clear()

            tmp.append(nums[i])

        if tmp:
            res.append(int(''.join(reversed(tmp))))

        return res

    def convert_chunk(self, number) -> str:
        h, d, u = 0, 0, 0

        if number >= 100:
            h = number // 100
            number = number % (h*100)
        if number >= 10:
            d = number // 10
            number = number % (d*10)

        u = number

        res = []
        if h > 0:
            res.append(self.units.get(h))
            res.append(self.qualifier[100])

        if d > 0:
            if d*10 + u <= 19:
                res.append(self.tens[d*10 + u])
                return ' '.join(res)
            else:
                res.append(self.decades[d*10])

        if h != 0 and d == 0 and u == 0 or (d != 0 and u == 0):
            return ' '.join(res)

        res.append(self.units[u])

        return ' '.join(res)


print(Solution().numberToWords(1234567891))
