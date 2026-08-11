class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        if not numbers:
            return []

        L, R = 0, len(numbers) - 1

        while L < R:
            total = numbers[L] + numbers[R]

            if total > target:
                R -= 1
            elif total < target:
                L += 1
            else:
                return [L + 1, R + 1]

        return []