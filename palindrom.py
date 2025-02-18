def validPalindrome(s: str) -> bool:
        s=s.lower()
        s = ''.join([char for char in s if char.isalnum()])
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                s=s[0:i]+s[i+1::]
                print(s)
                k=0
                l=len(s)-1
                while k<l:
                    if s[k]!=s[l]:
                        return False
                    k=k+1
                    l-=1
            i+=1
            j-=1
        return True
s=validPalindrome('abca')
print(s)