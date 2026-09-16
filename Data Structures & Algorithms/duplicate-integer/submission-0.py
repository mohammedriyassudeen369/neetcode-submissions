class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_sorted = sorted(nums)

        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = num

            else:
                return True

        return False



        