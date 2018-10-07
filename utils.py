# Copyright (c) Mac Clayton. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for details.

def class_name_from_interface(interface_name):
    return interface_name[2:]


def mock_class_name(class_name):
    if 'I_' in class_name or 'A_' in class_name:
        class_name = class_name_from_interface(class_name)
    return  'Mock{}'.format(class_name)
