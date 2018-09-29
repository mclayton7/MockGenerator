import unittest
from method_parser import CppMethod
from mock_method_generator import *


class TestMockMethodGenerator(unittest.TestCase):
    def test_will_create_simple_method(self):
        expected_output = 'MOCK_METHOD0(voidMethod, void());'
        method = CppMethod('voidMethod', 'void', [], True, False)

        actual_output = generate_mock_method(method)

        self.assertEqual(actual_output, expected_output)

    def test_will_create_simple_const_method(self):
        expected_output = 'MOCK_CONST_METHOD0(voidMethod, void());'
        method = CppMethod('voidMethod', 'void', [], True, True)

        actual_output = generate_mock_method(method)

        self.assertEqual(actual_output, expected_output)

    def test_will_create(self):
        self.assertEqual(1, 1)
