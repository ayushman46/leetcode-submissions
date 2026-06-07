class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        l, r = 0, 1
        ans = 1
        n = len(s)

        set1 = set()
        set1.add(s[0])

        while r < n:
            while s[r] in set1:
                set1.remove(s[l])
                l += 1

            set1.add(s[r])
            r+=1
            ans = max(ans, r - l)
            

        return ans