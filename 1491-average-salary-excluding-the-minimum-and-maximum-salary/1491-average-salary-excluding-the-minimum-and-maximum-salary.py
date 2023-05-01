class Solution:
    def average(self, salary: List[int]) -> float:
        if len(salary)==1:
            return salary[0]
        if len(salary)>2:
            salary.remove(max(salary))
            salary.remove(min(salary))
            return sum(salary)/len(salary)