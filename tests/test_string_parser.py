import unittest

from string_parser import string_parser

class TestStringParser(unittest.TestCase):
    def setUp(self):
        self.sut = string_parser

    def test_null_should_fail(self):
        # arrange
        data = ''

        # act
        actual = self.sut(data)

        # assert
        self.assertEqual(actual, None)

    def test_valid_should_Pass(self):
        # arrange
        data = 'FILESYSTEM OK -/ used space (9%) inode (3%) | fs=9% inode=3%'
        expected = {
            'space': '9%',
            'inode': '3%',
            'fs': '9%'
        }

        # act
        actual = self.sut(data)

        # assert
        self.assertEqual(actual, expected)