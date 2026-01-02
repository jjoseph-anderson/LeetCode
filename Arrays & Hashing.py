
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


# array1 = [1, 2, 3, 4]
# array2 = [1, 2, '#', '#']
# print(Solution().hasDuplicate(array1))

#### 2) Valid Anagram

# 2.1) brute force - sort each array

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = sorted(s)
        sort_t = sorted(t)
        if sort_s == sort_t:
            return True
        else:
            return False

# s = "racecar"
# t = "carrace"
# print(Solution().isAnagram(s, t))

# s = "jar"
# t = "jam"
# print(Solution().isAnagram(s, t))

# 2.2) Optimize using hash map

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_S, map_T = {}, {}
    # make hashmap frequency table
    for i in range(len(s)):
        map_S[s[i]] = 1 + map_S.get(s[i], 0)
        map_T[t[i]] = 1 + map_T.get(t[i], 0)

    return map_S == map_T

# s = "racecar"
# t = "carrace"
# print(Solution().isAnagram(s, t))

# s = "jar"
# t = "jam"
# print(Solution().isAnagram(s, t))

s = "x"
t = "xx"
print(Solution().isAnagram(s, t))