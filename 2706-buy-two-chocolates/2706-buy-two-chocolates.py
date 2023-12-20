class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        sumi=sum(prices)
        a=prices[0]+prices[1]
        if a<=money:
            return abs(money-a)
        else:
            return money