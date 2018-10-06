import unittest
from method_parser import CppMethod
from mock_method_generator import *


class TestMockMethodGenerator(unittest.TestCase):
    def test_will_create_simple_method(self):
        expected_output = 'MOCK_METHOD0(methodName, void());'
        method = CppMethod('methodName', 'void', [], True, False)

        self.assertEqual(generate_mock_method(method), expected_output)

    def test_will_create_simple_const_method(self):
        expected_output = 'MOCK_CONST_METHOD0(methodName, void());'
        method = CppMethod('methodName', 'void', [], True, True)

        self.assertEqual(generate_mock_method(method), expected_output)

    def test_will_create_method_with_simple_return_type(self):
        expected_output = 'MOCK_METHOD0(methodName, bool());'
        method = CppMethod('methodName', 'bool', [], True, False)

        self.assertEqual(generate_mock_method(method), expected_output)

    def test_will_create_method_with_reference_return_type(self):
        expected_output = 'MOCK_METHOD0(methodName, QString&());'
        method = CppMethod('methodName', 'QString&', [], True, False)

        self.assertEqual(generate_mock_method(method), expected_output)

    def test_will_create_method_with_const_reference_return_type(self):
        expected_output = 'MOCK_METHOD0(methodName, const QString&());'
        method = CppMethod('methodName', 'const QString&', [], True, False)

        self.assertEqual(generate_mock_method(method), expected_output)

    def test_will_create_const_method_with_const_reference_return_type(self):
        expected_output = 'MOCK_CONST_METHOD0(methodName, const QString&());'
        method = CppMethod('methodName', 'const QString&', [], True, True)

        self.assertEqual(generate_mock_method(method), expected_output)

    def test_will_create_method_with_argument(self):
        expected_output = 'MOCK_METHOD1(methodName, void(QString myString));'
        method = CppMethod('methodName', 'void', [('QString', 'myString',)], True, False)

        self.assertEqual(generate_mock_method(method), expected_output)

    def test_will_create_method_with_multiple_arguments(self):
        expected_output = 'MOCK_METHOD2(methodName, void(QString myString, QVector myVector));'
        method = CppMethod('methodName', 'void', [('QString', 'myString'), ('QVector', 'myVector')], True, False)

        self.assertEqual(generate_mock_method(method), expected_output)
