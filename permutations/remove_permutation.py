def checkInclusion(self, s1: str, s2: str) -> bool:
    def counter(s):
        temp = {}
        for ele in s:
            if ele in temp:
                temp[ele] = temp[ele] + 1
            else:
                temp[ele] = 1
        return temp

    l = 0,
    r = len(s1)
    word_count = counter(s1)
    while r < len(s2):
        win_word = s2[l:r]
        temp_count = counter(win_word)
        if temp_count == word_count:
            return True
        l = l + 1
        r = r + 1
    return False
s1='ss'
s2='adsasdas'
l=0
r=len(s1)
print(s2[l:r])