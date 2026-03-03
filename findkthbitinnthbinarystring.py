class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n==1:
            return '0'

        sequenced_size=1<<n

        if k==sequenced_size//2:
            return '1'
        elif k < sequenced_size // 2:
            return self.findKthBit(n - 1, k)

        else:
            res=self.findKthBit(n-1,sequenced_size-k)
            return '0' if res=='1' else '1'

        
