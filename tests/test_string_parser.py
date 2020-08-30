import unittest
from unittest import TestCase

from string_parser import string_parser


class TestStringParser(TestCase):
    def setUp(self):
        self.sut = string_parser

    def tearDown(self):
        self.sut = None

    def test_string_parser_empty_should_fail(self):
        # arrange
        data = ''

        # act
        actual = self.sut(data)

        # assert
        self.assertEqual(actual, None)

    def test_string_parser_valid_should_Pass(self):
        # arrange
        data = 'FILESYSTEM OK -/ used space (9.5%) inode (3%) | fs=9% inode=3%'
        expected = {
            'space': '9.5%',
            'inode': '3%',
            'fs': '9%'
        }

        # act
        actual = self.sut(data)

        # assert
        self.assertEqual(actual, expected)
