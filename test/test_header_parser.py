# Copyright (c) Mac Clayton. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for details.

import unittest
import os
from header_parser import HeaderParser

directory = os.path.dirname(os.path.abspath(__file__))


class TestParser(unittest.TestCase):
    def test_will_return(self):
        patient = HeaderParser(os.path.join(directory, 'I_SimpleInterface.h'))

        self.assertEqual(patient.classes()[0].name(), 'I_SimpleInterface')


    def test_will_find_methods(self):
        expected_count = 15

        patient = HeaderParser(os.path.join(directory, 'I_SimpleInterface.h'))

        self.assertEqual(len(patient.classes()[0].methods()), expected_count)

    def test_will_find_signals(self):
        expected_count = 4

        patient = HeaderParser(os.path.join(directory, 'I_SimpleInterface.h'))

        actual_count = len(patient.classes()[0].signals())
        self.assertEqual(actual_count, expected_count)

