'''345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.


'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        p = len(s)-1
        vouwls_list=['a','e','o','i','u','A','E','O','I','U']
        # str_list=list(s)
        result=[]
        for c in s:
            if c in vouwls_list:
                while(s[p] not in vouwls_list):
                    p-=1
                result.append(s[p])
                p-=1
            else:
                result.append(c)

        return "".join(result)

