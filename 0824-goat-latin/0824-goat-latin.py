class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split(' ')
        out = ""
        count = 1
        ma = "ma"
        p = "aeiouAEIOU"
        for i in sentence:
            a = i[0]
            if a in p:
                out += i + ma
            else:
                k = i[0]
                out += i[1:] + k
                out += ma
            out += 'a' * count + ' '
            count += 1
        return out.strip()
