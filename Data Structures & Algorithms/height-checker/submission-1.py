class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        e = sorted(heights)
        m = 0
        for i in range(len(heights)):
            if heights[i] != e[i]:
                m += 1
        return m