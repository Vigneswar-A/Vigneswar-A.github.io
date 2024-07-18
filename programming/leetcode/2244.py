class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        prev = 0
        res = 0

        for s in bank:
            count = s.count('1')
            if not count:
                continue
            
            res += prev*count
            prev = count

        return res
        