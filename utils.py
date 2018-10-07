# Copyright (c) Mac Clayton. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for details.

def class_name_from_interface(interface_name):
    return interface_name[2:]


def mock_class_name(class_name):
    if 'I_' in class_name or 'A_' in class_name:
        class_name = class_name_from_interface(class_name)
    return  'Mock{}'.format(class_name)

def signal_helper_name(signal):
    return 'emit{}'.format(signal.name()[0].upper() + signal.name()[1:])

def format_method_arguments(method):
    if len(method.arguments()) is 0: return ''
    TEMPLATE = '{TYPE} value{COUNT}, '
    output = ''
    count = 0
    for argument in method.arguments():
        output += TEMPLATE.format(
            TYPE=argument[0],
            COUNT=count)
        count += 1
    output_with_trailing_comma_and_space_removed = output[:-2]
    return output_with_trailing_comma_and_space_removed
