"""Test code for palindrome.py.

Author: Allen B. Downey
"""

"""import unittest
import palindrome
class Tests(unittest.TestCase):
	def test_is_palindrome(self):
		self.assertTrue(palindrome.is_palindrome('abbs'))"""

from palindrome import is_palindrome

def main():
	for line in open('words.txt'):
		#remove whitespace from the beginning and end
		word = line.strip()
		#only print palindromes
		if is_palindrome(word):
			print word

if __name__ == '__main__':
		#unittest.main()
		print main()