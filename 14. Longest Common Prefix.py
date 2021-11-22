class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        index,flag=0,0
        while index<len(strs[0]):
            char=strs[0][index]
            for i in range(1,len(strs)):
                if index>=len(strs[i]) or strs[i][index]!=char:
                    flag=1
                    break
            if flag==1:
                break
            res+=char
            index+=1
        return res
