"""
2000. Reverse Prefix of Word
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at 
index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch 
does not exist in word, do nothing.
"""

def reversePrefix(word, ch):
    if ch in word:
        prefix = word[:word.index(ch) + 1][::-1]
        res = prefix + word[len(prefix):]

        return res
    return word

print(reversePrefix(word='xyxzxe', ch='z'))
