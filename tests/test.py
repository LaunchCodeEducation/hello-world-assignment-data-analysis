import unittest

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from hello import hello

class TestHelloWorld(unittest.TestCase):

   def test_student_solution(self):
      self.assertEqual(hello(), 'Hello world!');

if __name__ == '__main__':
    unittest.main()
