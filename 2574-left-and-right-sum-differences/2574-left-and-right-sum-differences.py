class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        totalsum=sum(nums)  # Calculate the sum of all elements.
        leftsum =0       
        answer=[0]*len(nums)    # Create result array filled with zeros.
        for i in range(len(nums)):              # Traverse each index.
            rightsum=totalsum-leftsum-nums[i]
            answer[i]=abs(leftsum-rightsum)  # Store absolute difference between left and right sums.
            leftsum+=nums[i]    #Include current element in left sum  # for the next iteration.
        return answer           # Return final result array.
