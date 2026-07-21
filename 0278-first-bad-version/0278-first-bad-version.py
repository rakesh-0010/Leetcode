# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low=0
        high=n
        ans=-1
        while low<=high:
            mid=low+(high-low)//2
            result=isBadVersion(mid)
            if (result):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans


        