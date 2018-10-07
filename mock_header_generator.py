# Copyright (c) Mac Clayton. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for details.

from mock_method_generator import generate_mock_method
from utils import mock_class_name
TEMPLATE = '''#pragma once

#include <{INTERFACE_NAME}.h>
{HEADERS}

class {MOCK_CLASS_NAME} : public QObject, public {INTERFACE_NAME}
{{
    Q_OBJECT

public:
    explicit {MOCK_CLASS_NAME}();
    virtual ~{MOCK_CLASS_NAME}();

{METHODS}
{SIGNALS}
}};
'''

SIGNALS_TEMPLATE = '''
    {SIGNAL_HELPERS}
signals:
    {SIGNALS}
'''

DEFAULT_HEADERS = [
    '#include <QObject>',
    '#include <gtest/gmock.h>'
]


def _signal_helper_name(signal_name):
    return 'emit{}'.format(signal_name[0].upper() + signal_name[1:])

def _format_arguments(arguments):
    if len(arguments) is 0: return ''
    TEMPLATE = '{TYPE} value{COUNT}, '
    output = ''
    count = 0
    for argument in arguments:
        output += TEMPLATE.format(
            TYPE=argument[0],
            COUNT=count)
        count += 1
    output_with_trailing_comma_and_space_removed = output[:-2]
    return output_with_trailing_comma_and_space_removed

def _method_string(methods):
    mock_methods = [generate_mock_method(m) for m in methods]
    return '    ' + '\n    '.join(mock_methods)


def _signal_helpers(signals):
    TEMPLATE='void {SIGNAL_NAME}({ARGUMENTS});\n    '
    output = ''
    for signal in signals:
        output += TEMPLATE.format(
            SIGNAL_NAME=_signal_helper_name(signal.name()),
            ARGUMENTS=_format_arguments(signal.arguments()))
    return output


def _signals_string(signals):
    if len(signals) is 0: return ''
    return SIGNALS_TEMPLATE.format(
        SIGNAL_HELPERS=_signal_helpers(signals),
        SIGNALS='\n    '.join([str(s) for s in signals]))


def generate_mock_header(interface_name, methods = [], signals = []):
    headers = '\n'.join(DEFAULT_HEADERS)

    return TEMPLATE.format(
        HEADERS=headers,
        MOCK_CLASS_NAME=mock_class_name(interface_name),
        INTERFACE_NAME=interface_name,
        METHODS=_method_string(methods),
        SIGNALS=_signals_string(signals))
