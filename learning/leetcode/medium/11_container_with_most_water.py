
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxarea = 0
        left = 0
        right = n-1
        
        while left < right:
            hl = height[left]
            hr = height[right]
            if(hr>hl):
                area = hl * (right - left)
                if(area>maxarea):
                    maxarea = area
                left+=1
            else: 
                area = hr * (right - left)
                if(area> maxarea):
                    maxarea = area
                right-=1
            
        return maxarea            


def main():
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = Solution().maxArea(heights)
    print(f"res: {res}")
    
if __name__ == "__main__":
    main()
    