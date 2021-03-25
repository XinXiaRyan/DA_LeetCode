class Solution:
    def binarySearch(self, nums:List[int], target:int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) //2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    def search(self, nums:List[int], target:int) -> int:
        start = self.binarySearch(nums,target)
        if start == len(nums) or nums[start] != target:
            return [-1,-1]
        return[start,self.binarySearch(nums,target+1)-1]