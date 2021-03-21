class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:   
        try: 
            i = nums.index(target) #按升序找到第一个匹配
        except:
            return [-1,-1]
        j = list(reversed(nums)).index(target)#按降序找到第一个匹配
        return [i,len(nums)-j-1] # len(nums)-j-1 将降序匹配的index转化为升序的index 再返回值
