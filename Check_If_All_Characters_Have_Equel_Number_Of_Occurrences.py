class Solution(object):
    def areOccurrencesEqual(self, s):
        mydict = {}

        for letter in s:
            letter = letter.lower()
            mydict[letter] = mydict.get(letter, 0) + 1

        values = list(mydict.values())

        for value in values:
            if value != values[0]:
                return False

        return True
