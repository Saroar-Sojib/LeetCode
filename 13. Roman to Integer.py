class Solution:
    def romanToInt(self, s: str) -> int:
        sum=0
        thisdict = {
          "I": 1,
          "V": 5,
          "X": 10,
          "L": 50,
          "C": 100,
          "D": 500,
          "M": 1000
        }
        for i in range(0,len(s)-1):
            if thisdict[s[i]]>=thisdict[s[i+1]]:
                sum=sum+thisdict[s[i]]
            else:
                sum=sum-thisdict[s[i]]
        sum=sum+thisdict[s[len(s)-1]]
        return sum
