```python
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		dic = {}
		count = 0

		for num in range(len(nums)):
			element = nums[num]
			if nums[num] in dic:
				nums[num] = 100000
				dic[element] += 1
				count += 1
			else:
				dic[element] = 1
				nums.sort()

		return len(nums) - count
```