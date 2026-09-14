
class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        
        mults = {n for n in nums if n % k == 0}
        cand = k
        while cand in mults: 
            cand += k
        return cand

def main():
    print("your program is running")
    nums = [8, 2, 3, 4, 6]
    k = 2
    Solution().missingMultiple(nums, k)

if __name__ == "__main__":
    main()
