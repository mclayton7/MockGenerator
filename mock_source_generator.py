
TEMPLATE = '''#include <{MOCK_CLASS_NAME}.h>
#include <{MOCK_CLASS_NAME}.moc>

{MOCK_CLASS_NAME}::{MOCK_CLASS_NAME}()
{{
}}

{MOCK_CLASS_NAME}::~{MOCK_CLASS_NAME}()
{{
}}
'''

SIGNAL_HELPER_TEMPLATE='''
void {MOCK_CLASS_NAME}::{HELPER_NAME}({ARGUMENTS})
{{
    void emit {{SIGNAL}}({ARGUMENTS});
}}
'''

def _class_name(interface_name):
    return interface_name[2:]

def _method_string(methods):
    return '    ' + '\n    '.join(methods)

def _signal_string(class_name, signal):
    output = SIGNAL_HELPER_TEMPLATE.format(
        MOCK_CLASS_NAME=class_name)


def generate_mock_source(interface_name, methods = [], signals = []):
    mock_class_name = 'Mock{}'.format(_class_name(interface_name))
    output = TEMPLATE.format(
        MOCK_CLASS_NAME=mock_class_name)
    for signal in signals:
        output+= _signal_string(signal)
