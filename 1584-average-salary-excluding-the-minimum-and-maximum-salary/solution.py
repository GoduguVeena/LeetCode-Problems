class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        res = sum(salary[1:-1]) / (len(salary) - 2)
        return res
