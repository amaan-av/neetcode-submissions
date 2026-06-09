class Solution(object):
    def hasDuplicate(self, nums):
        seen = set()

        for i in nums:
            if i in seen:
                return True
                break
            seen.add(i)
            
        return False
        