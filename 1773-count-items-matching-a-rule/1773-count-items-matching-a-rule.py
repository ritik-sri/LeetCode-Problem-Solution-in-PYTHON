Item = collections.namedtuple('Item', ['type', 'color', 'name'])

class Solution:
    def countMatches(self, items: list[list[str]], key: str, value: str) -> int:
        return sum(getattr(Item(*item), key) == value for item in items)