class Solution(object):
    def countAsterisks(self, s: str = 'l|*e*et|c**o|*de|') -> int:
        """
        :type s: str
        :rtype: int
        """
        return ''.join([char for char in s.split('|')[::2]]).count('*')