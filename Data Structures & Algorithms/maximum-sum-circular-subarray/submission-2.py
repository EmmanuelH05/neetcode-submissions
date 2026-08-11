class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        total = 0 

        if not nums:
            return 0

        # for max sub array 
        maxSum = nums [0]
        curSum = 0 

        # for min sub array 
        curMin = 0
        minSum = nums [0]
        for n in nums:
            total += n 
            
            curSum = max(curSum + n, n)
            maxSum = max(maxSum, curSum)

            curMin = min(curMin + n, n)
            minSum = min(minSum, curMin)

        #if all are neg, maxSum is the answer 
        if maxSum < 0:
            return maxSum

        return max(maxSum, total - minSum)