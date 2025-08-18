class Solution(object):

    def custom_sort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                # Compare concatenated results
                if str(nums[i]) + str(nums[j]) < str(nums[j]) + str(nums[i]):
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        #nums.sort(key=self.lam,reverse=True)
        summ=''
        nums=self.custom_sort(nums)

        for i in nums:
            summ+=str(i)
        
        if int(summ)==0:
            return '0'
        return summ