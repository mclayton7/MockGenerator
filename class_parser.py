import clang.cindex
from method_parser import method_factory


class CppClass(object):
    """docstring for CppClass"""

    def __init__(self, name, methods, signals):
        self._name = name
        self._methods = methods
        self._signals = signals

    def __repr__(self):
        template = '''
Class Name: {name}
{methods}
'''
        methods_str = ''
        for method in self._methods:
            methods_str += str(method)
        return template.format(
            name=self.self._name,
            methods=methods_str)

    def name(self):
        return self._name

    def methods(self):
        return self._methods

    def signals(self):
        return self._signals

def find_signals_line(cursor):
    for x in cursor.get_tokens():
        if x.kind is clang.cindex.TokenKind.COMMENT:
            if 'signals' in x.spelling:
                return x.location.line
    return None


def is_a_signal(cursor, signals_line = False):
    if not signals_line:
        return False
    is_protected = cursor.access_specifier is clang.cindex.AccessSpecifier.PROTECTED
    is_below_signals_comment = cursor.location.line > signals_line
    return is_protected and is_below_signals_comment


def class_factory(class_cursor):
    name = class_cursor.spelling
    methods = []
    signals = []

    signals_line = find_signals_line(class_cursor)

    for child in class_cursor.get_children():
        if child.kind is clang.cindex.CursorKind.CXX_METHOD:
            if  is_a_signal(child, signals_line):
                signals.append(method_factory(child))
            else:
                methods.append(method_factory(child))

    return CppClass(name, methods, signals)
