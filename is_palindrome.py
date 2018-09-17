class Solution:
  def isPalindrome(self, x):
    if (x < 0):
      return False
    z = 0
    number = x
    while (number > 0):
      digit  = number % 10
      z = z * 10 + digit
      number //= 10
    return z == x

if __name__ == "__main__":
  sol = Solution()
  print (sol.isPalindrome(1771))
