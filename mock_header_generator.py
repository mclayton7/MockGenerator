
TEMPLATE = '''
#pragma once

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
signals:
    {SIGNALS}
'''

DEFAULT_HEADERS = [
    '#include <QObject>',
    '#include <gtest/gmock.h>'
]

def _class_name(interface_name):
    return interface_name[2:]

def _method_string(methods):
    return '    ' + '\n    '.join(methods)

def _signals_string(signals):
    if len(signals) is 0: return ''
    return SIGNALS_TEMPLATE.format(SIGNALS='\n    '.join(signals))


def generate_mock_header(interface_name, methods = [], signals = []):
    headers = '\n'.join(DEFAULT_HEADERS)
    mock_class_name = 'Mock{}'.format(_class_name(interface_name))
    return TEMPLATE.format(
        HEADERS=headers,
        MOCK_CLASS_NAME=mock_class_name,
        INTERFACE_NAME=interface_name,
        METHODS=_method_string(methods),
        SIGNALS=_signals_string(signals))
