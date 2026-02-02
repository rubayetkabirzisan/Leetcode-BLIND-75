class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)#0->[-1]
        curMin,curMax=1,1
        for n in nums:
            tmp=curMax*n
            curMax=max(n*curMax,n*curMin,n)
            curMin=min(tmp,n*curMin,n)
            res=max(res,curMax,curMin)
        return res