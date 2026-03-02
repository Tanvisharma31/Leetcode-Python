# Last updated: 02/03/2026, 14:00:26
class Solution:
    def countLargestGroup(self, n: int) -> int:

        digit_sum_counts = {}

        for number in range(1, n + 1):
            digit_sum = self.calculate_digit_sum(number)
            digit_sum_counts[digit_sum] = digit_sum_counts.get(digit_sum, 0) + 1

        max_group_size = max(digit_sum_counts.values())
        largest_groups_count = sum(
            1 for count in digit_sum_counts.values() if count == max_group_size
        )

        return largest_groups_count

    def calculate_digit_sum(self, n: int) -> int:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total