class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            d[size] += [i]
        print(d)
        result = []
        for key, value in d.items():
            print(key,value)
            i, len_value = 0, len(value)
            while key <= len_value:
                result.append(value[i: i + key])
                i = key
                len_value -= key
        return result