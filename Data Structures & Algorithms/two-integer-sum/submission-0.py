class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for this we will use a hashmap because we dont want to linear scan
        # and we also need a key value pair usage
        # a dict for seen values from array into hashmap
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i] # returning i and the index of the complement
            seen[num] = i