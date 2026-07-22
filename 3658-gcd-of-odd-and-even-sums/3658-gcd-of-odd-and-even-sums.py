class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even=[]
        odd=[]
        for x in range(1,(n*2)+1):
            if x%2==0:
                even.append(x)
            else:
                odd.append(x)
        s=sum(even)
        l=sum(odd)
        while l !=0:
            s,l=l,s%l
        return s
        