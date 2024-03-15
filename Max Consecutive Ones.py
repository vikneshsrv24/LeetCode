class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,out=0,0
        for i in nums:
            if i==1:          # we asked to find only ones 
               count+=1
               out=max(out,count)
            else:
                count=0
        return out

        
