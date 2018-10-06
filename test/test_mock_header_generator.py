import unittest
import os
from mock_header_generator import generate_mock_header


class TestMockHeaderGenerator(unittest.TestCase):
    def test_will_define_class_that_inherits_from_qobject_and_interface(self):
        expected_output = 'class MockMyClass : public QObject, public I_MyClass'

        self.assertIn(expected_output, generate_mock_header('I_MyClass', []))

    def test_will_have_qobject_header(self):
        self.assertIn('#include <QObject>', generate_mock_header('I_MyClass', []))

    def test_will_have_gmock_header(self):
        self.assertIn('#include <gtest/gmock.h>', generate_mock_header('I_MyClass', []))
