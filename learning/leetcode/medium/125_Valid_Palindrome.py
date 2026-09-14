class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            lc = s[left].lower()
            lr = s[right].lower()
            while not (lc.isalnum()) and left < right:
                left += 1
                lc = s[left].lower()
            while not (lr.isalnum()) and right > left:
                right -= 1
                lr = s[right].lower()
            if lc != lr:
                return False
            else:
                left += 1
                right -= 1
        return True


def main():
    print("started")
    s = "A man, a plan, a canal: Panama"
    res = Solution().isPalindrome(s)
    print(res)
    s = "race a car"
    res = Solution().isPalindrome(s)
    print(res)
    s = "0P"
    res = Solution().isPalindrome(s)
    print(res)
    print("finished")


if __name__ == "__main__":

    main()
