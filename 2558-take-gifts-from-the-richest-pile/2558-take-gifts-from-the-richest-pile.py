class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k>0:
            a=max(gifts)
            b=gifts.index(a)
            gifts[b]=math.floor(sqrt(a))
            k-=1
        return sum(gifts)