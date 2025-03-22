
#### 1) Contains Duplicates

# 1.1) Brute Force - search each element of array
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False

# array1 = [1, 2, 3, 4]
# array2 = [1, 2, '#', '#']
# print(Solution().hasDuplicate(array2))

# 1.2) Could sort array and then filter through it for O(n log(n) )

# 1.3) Hash table
class Solution:
    def hasDuplicate(self, nums):
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


array1 = [1, 2, 3, 4]
array2 = [1, 2, '#', '#']
print(Solution().hasDuplicate(array1))