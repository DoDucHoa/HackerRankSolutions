import unittest
import Strings.sWAP_cASE
from Strings import sWAP_cASE


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = sWAP_cASE.swap_case('a')
        self.assertEqual(result, 'A')


if __name__ == '__main__':
    unittest.main()
