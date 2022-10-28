import unittest
from rock_paper_scissors import who_wins

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("You Win!", who_wins(1,3))  # add assertion here


if __name__ == '__main__':
    unittest.main()
