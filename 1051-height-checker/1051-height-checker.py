class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        arr = []
        for num in heights:
            arr.append(num)
        n = len(arr)
        for i in range(n - 1):
            min = i
            for j in range(i + 1, n):
                if arr[j] < arr[min]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        count = 0
        for i in range(n):  #Compare with the original array
            if heights[i] != arr[i]:
                count += 1

        return count