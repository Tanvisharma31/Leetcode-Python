# Last updated: 02/03/2026, 14:02:36
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        billion = 1000000000
        million = 1000000
        thousand = 1000

        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return self.lessThan20[num] + " "
            elif num < 100:
                return self.tens[num // 10] + " " + helper(num % 10)
            else:
                return self.lessThan20[num // 100] + " Hundred " + helper(num % 100)

        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        result = ""
        if num >= billion:
            result += helper(num // billion) + "Billion "
            num %= billion
        if num >= million:
            result += helper(num // million) + "Million "
            num %= million
        if num >= thousand:
            result += helper(num // thousand) + "Thousand "
            num %= thousand
        if num > 0:
            result += helper(num)

        return result.strip()
