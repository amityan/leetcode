class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        n = x
        num = ""
        while (n > 0):
            temp = str(n % 10)
            num += temp
            n //= 10

        if(num != ''):
            if(int(num) == x):
                return True
            else:
                return False
