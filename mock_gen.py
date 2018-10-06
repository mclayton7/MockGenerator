#!/usr/bin/env python

import argparse

from header_parser import HeaderParser
from mock_header_generator import generate_mock_header
from mock_method_generator import generate_mock_method

def main():
    parser = argparse.ArgumentParser(description='Short sample app')
    parser.add_argument('interface_path', help='path/to/interface.h')
    args = parser.parse_args()

    header = HeaderParser(args.interface_path)

    classes = header.classes()

    first_class = classes[0]
    interface_name = first_class.name()
    methods = first_class.methods()
    signals = first_class.signals()

    mock_methods = [generate_mock_method(m) for m in methods]
    signals = [str(s) for s in signals]

    output = generate_mock_header(interface_name, mock_methods, signals)

    print(output)

if __name__ == '__main__':
    main()
