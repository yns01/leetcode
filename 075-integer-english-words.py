class Solution:
    def numberToWords(self, num):
        if num == 0:
            return 'Zero'

        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                           "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty",
                     "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

        res = ''
        for t in self.thousands:
            if num % 1000 != 0:
                res = self.convert_chunk(num % 1000) + t + ' ' + res

            num //= 1000

        return res.strip()

    def convert_chunk(self, num):
        if num == 0:
            return ''
        elif num < 20:
            return self.lessThan20[num] + ' '
        elif num < 100:
            return self.tens[num // 10] + ' ' + self.convert_chunk(num % 10)
        else:
            return self.lessThan20[num // 100] + ' Hundred ' + self.convert_chunk(num % 100)


print(Solution().numberToWords(50238))
print(Solution().numberToWords(1234567891))
