import clang.cindex


class CppMethod(object):
    """docstring for CppMethod"""

    def __init__(
            self,
            name,
            return_type,
            arguments,
            is_pure_virtual,
            is_const):
        self._name = name
        self._return_type = return_type
        self._arguments = arguments
        self._is_pure_virtual = is_pure_virtual
        self._is_const = is_const

    def __repr__(self):
        template = '{return_type} {name}({arguments}) {const}'
        arguments = ''
        const = ''
        if self._is_const:
            const = 'const'
        for argument in self._arguments:
            arguments += '{} {}'.format(argument[0], argument[1])
        return template.format(
            return_type=self._return_type,
            name=self._name,
            arguments=arguments,
            const=const)

    def name(self):
        return self._name

    def return_type(self):
        return self._return_type

    def arguments(self):
        return self._arguments

    def is_pure_virtual(self):
        return self._is_pure_virtual

    def is_const(self):
        return self._is_const


def method_factory(method_cursor):
    name = method_cursor.spelling
    return_type = method_cursor.result_type.spelling
    is_const = method_cursor.is_const_method()
    is_pure_virtual = method_cursor.is_pure_virtual_method()
    access_specifier = method_cursor.access_specifier
    arguments = []
    for arg in method_cursor.get_arguments():
        arg_type = arg.type.spelling
        arg_name = arg.spelling
        arguments += [(arg_type, arg_name,)]

    return CppMethod(name, return_type, arguments, is_pure_virtual, is_const)
