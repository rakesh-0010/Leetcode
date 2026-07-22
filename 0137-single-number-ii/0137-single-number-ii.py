class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one=0
        two=0
        for x in range(len(nums)):
            one=(one^nums[x]&~two)
            two=(two^nums[x]&~one)
        return one
