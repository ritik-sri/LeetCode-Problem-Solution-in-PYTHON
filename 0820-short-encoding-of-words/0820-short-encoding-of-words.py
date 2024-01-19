from typing import List

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        word_set = set(words)
        word_list = list(word_set)
        dup_list = set()
        for i in range(len(word_list)):
            for j in range(len(word_list)):
                if i != j:
                    if word_list[i].endswith(word_list[j]):
                        dup_list.add(word_list[j])

        count = 0
        for word in word_list:
            if word not in dup_list:
                count += len(word) + 1

        return count
