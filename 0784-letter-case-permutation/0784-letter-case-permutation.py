class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def generate_permutations(s, index, current, result):
            if index == len(s):
                result.append(current)
                return
            char = s[index]
            if char.isalpha():
                generate_permutations(s, index + 1, current + char.lower(), result)
                generate_permutations(s, index + 1, current + char.upper(), result)
            else:
                generate_permutations(s, index + 1, current + char, result)

        result = []
        generate_permutations(s, 0, "", result)
        return result
