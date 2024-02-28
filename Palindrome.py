class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=x
        if x<0:
            return False
        else:
            r=0
            while x!=0:
                r=r*10+x%10
                x=x//10
        if r==a:
            return True
        else:
            return False
