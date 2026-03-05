class Solution:
    def minOperations(self, s: str) -> int:
        oddCount, evenCount = 0, 0
        cnt=0
        if s.count('1') == len(s) or s.count('0') == len(s):
            return len(s)//2
        for i in range(len(s)):
            if i %2 == 0:
                if s[i] == '0':
                    evenCount +=1 
                else:
                    evenCount -=1
            else:
                if s[i] == '0':
                    oddCount +=1 
                else:
                    oddCount -=1
        #print(oddCount,evenCount)
        if oddCount >= 0 and evenCount >= 0:
            if evenCount >= oddCount:
                for i in range(len(s)):
                    if i % 2 == 0:
                        if s[i] == '1':
                            cnt+=1
                    else:
                        if s[i] == '0':
                            cnt+=1
            else:
                for i in range(len(s)):
                    if i % 2 == 0:
                        if s[i] == '0':
                            cnt+=1
                    else:
                        if s[i] == '1':
                            cnt+=1
        elif oddCount >= 0 and evenCount < 0:
            for i in range(len(s)):
                if i % 2 == 0:
                    if s[i] == '0':
                        cnt+=1
                else:
                    if s[i] == '1':
                        cnt+=1
            
        elif oddCount < 0 and evenCount >= 0:
            for i in range(len(s)):
                if i % 2 == 0:
                    if s[i] == '1':
                        cnt+=1
                else:
                    if s[i] == '0':
                        cnt+=1
        
        elif oddCount < 0 and evenCount < 0:
            if evenCount >= oddCount:
                for i in range(len(s)):
                    if i % 2 == 0:
                        if s[i] == '1':
                            cnt+=1
                    else:
                        if s[i] == '0':
                            cnt+=1
            else:
                for i in range(len(s)):
                    if i % 2 == 0:
                        if s[i] == '0':
                            cnt+=1
                    else:
                        if s[i] == '1':
                            cnt+=1

        return cnt
