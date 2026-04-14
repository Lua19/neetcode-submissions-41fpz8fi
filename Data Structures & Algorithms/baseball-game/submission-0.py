class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for x in operations:
            if x == '+':
                record.append(record[-1]+record[-2])
                continue
            if x == 'D':
                record.append(record[-1]*2)
                continue
            if x == 'C':
                record.pop()
                continue
            record.append(int(x))
        return sum(record)