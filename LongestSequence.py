class Solution(object):
   def longestConsecutive(self, a):
      a = set(a)
      longest = 0
      for i in a:
         if i-1 not in a:
            current = i
            streak = 0
            while i in a:
               i+=1
               streak+=1
               longest = max(longest,streak)
      return longest

ob = Solution()
n=int(input())
m=list(map(int,input().strip().split()))[:n]
print(ob.longestConsecutive(m))