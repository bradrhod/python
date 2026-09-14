class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            ni = nums[i]
            if i > 0 and ni == nums[i-1]:
                continue  # skip duplicate first element
            if ni + nums[-2] + nums [-1]< 0:
                continue
            if ni>0:
                # sorted, no more negatives, so no way to get to 0
                break
            if i < n - 2 and ni + nums[i+1] + nums[i+2] > 0:
                break #smallest possible
            
                
            left = i + 1
            right = n - 1
            while left<right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1  # skip the left (second) element it is duplicated
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1 # skip the right (third) element it is duplicated
            
        return res    


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    res = Solution().threeSum(nums)
    print(res)


if __name__ == "__main__":
    main()
