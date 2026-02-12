class Solution:
    def longestBalanced(self, s: str) -> int:
        n, ans = len(s), 1
        for i in range(n - 1):
            if ans > n - i:
                break
            freq = defaultdict(int)
            j, g = i, 1
            while j < n:
                for _ in range(min(n - j, g)):
                    freq[s[j]] += 1
                    j += 1
                mx, ln, sm = max(freq.values()), len(freq), j - i
                g = mx * ln - sm
                if g == 0:
                    ans = max(ans, sm)
                    g = min(ln, freq[s[i]])
        return ans
