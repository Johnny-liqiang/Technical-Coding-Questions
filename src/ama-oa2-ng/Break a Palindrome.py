class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        # Only contain 1 char value return empty to break the palindrome 
        if len(palindrome) < 2 :
            return ""
        
        # Search half of the palindrome to replace a non 'a' char into 'a'
        for i in xrange(0, len(palindrome)/2):
            if palindrome[i] !='a':
                return palindrome[:i]+'a'+palindrome[i+1:]
        
        
        # for all 'a' case then break the last char into 'b'
        return palindrome[:len(palindrome)-1]+'b'
        
    
#space O(n)
#time O(n)
