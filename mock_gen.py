#!/usr/bin/env python
# Copyright (c) Mac Clayton. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for details.

import argparse
import os

from header_parser import HeaderParser
from mock_header_generator import generate_mock_header
from mock_source_generator import generate_mock_source
from utils import mock_class_name

def main():
    args = parse_args()
    header = HeaderParser(args.interface_path)

    classes = header.classes()

    first_class = classes[0]
    interface_name = first_class.name()
    methods = first_class.methods()
    signals = first_class.signals()

    header_string = generate_mock_header(interface_name, methods, signals)
    source_string = generate_mock_source(interface_name, methods, signals)

    class_name = mock_class_name(interface_name)

    write_file(args.interface_path, '{}.h'.format(class_name), header_string)
    write_file(args.interface_path, '{}.cc'.format(class_name), source_string)

def parse_args():
    parser = argparse.ArgumentParser(description='Short sample app')
    parser.add_argument('interface_path', help='path/to/interface.h')
    return parser.parse_args()


def write_file(interface_path, mock_filename, data):
    file_path = os.path.join(os.path.dirname(interface_path), mock_filename)
    print(file_path)
    with open(file_path, 'w') as f:
        f.write(data)


if __name__ == '__main__':
    main()
