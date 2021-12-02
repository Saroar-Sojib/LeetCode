class Solution:

	def rob(self, nums: List[int]) -> int:

		a = nums[0]
		sum = 0
		for i in range(1, len(nums)):
			temp1 = nums[i] + sum
			temp2 = max(a, sum)
			a = temp1
			sum = temp2

		return max(a, sum)	
