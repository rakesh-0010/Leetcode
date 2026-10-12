class Solution:
    def calculateTime(self,piles,b_count):
        time=0
        for i in range(0,len(piles)):
            time+=math.ceil(piles[i]/b_count)
        return time
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low=1
        high=max(piles)
        ans=0
        while low<=high:
            mid=(low+high)//2
            time=self.calculateTime(piles,mid)
            if time<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
