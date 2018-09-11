def isPalindrome(s):
    """Polindrome is: empty string, 1 letter or Able was I ere, I saw Elba
        Args:
            s - string
        Return:
            bool
    """
    def toChar(s):
        """Remove unnecessary letter from string"""
        s = s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans+=c
        return ans

    def isPal(s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and isPal(s[1:-1])           
    return isPal(toChar(s))

# str0 = "Able was I ere, I saw Elba"
# str1 = ""
# print(isPalindrome(str0))