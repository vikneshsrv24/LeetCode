class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a,b=0,len(numbers)-1
        while a<b:
            if numbers[a]+numbers[b]==target:
                return (a+1,b+1)
            elif numbers[a]+numbers[b]<target:
                a+=1
            else:
                b-=1
            


        
