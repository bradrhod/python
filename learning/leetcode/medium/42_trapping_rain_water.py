class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0 
        right = n-1
        tr = 0
        while(left < right):
            hlw = height[left]
            hrw = height[right]
            # find next left and next right height wall. 
            nlw = left+1
            nlh = height[nlw]
            nrw = right-1
            nrh = height[nrw]
            if(hlw<hrw):
                while(nlh < hlw and nlw < right):
                    tr += hlw - nlh
                    nlw +=1     
                    nlh = height[nlw]
                left = nlw
            else:
                while(nrh<hrw and nrw > left):
                    tr += hrw - nrh
                    nrw -= 1
                    nrh = height[nrw]
                right = nrw
        
        return tr
            
            
        

def main():
    print("started")
    height = (0,1,0,2,1,0,1,3,2,1,2,1)
    res = Solution().trap(height)
    print(f"tr: {res}")
    
if __name__ == "__main__":
    main()