def solve(nums):
   if len(nums) < 1:
      return 0
   min_val = min(nums)
   max_val = max(nums)
   if max_val - min_val + 1 == len(nums):
      for i in range(len(nums)):
         if nums[i] < 0:
            j = -nums[i] - min_val
         else:
            j = nums[i] - min_val
            if nums[j] > 0:
               nums[j] = -nums[j]
            else:
               return 0
      return 1
   return 0

n = int(input(""))
nums = list(int(num) for num in input("").strip().split())[:n]

print(solve(nums))