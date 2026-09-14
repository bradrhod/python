class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0 
        right = len(numbers)-1
        while left<right:
            total = numbers[left]+numbers[right]
            if(total == target):
                return [left+1, right+1]
            elif total < target:
                left+=1
            else:
                right-=1
        return[]
   
def main():
    print("started")
    numbers = [2, 7, 11, 15]
    target = 9
    res = Solution().twoSum(numbers, target)
    print(res)
    numbers = [2,3,4]
    target = 6
    res = Solution().twoSum(numbers, target)
    print(res)
    
    
if __name__ == "__main__":
    main()