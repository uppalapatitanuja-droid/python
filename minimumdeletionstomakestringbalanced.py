class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans=0
        while True:
            if 'ba' not in s:
                return ans
            ans+=s.count('ba')
            s=s.replace('ba','')
        
