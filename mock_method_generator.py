from method_parser import CppMethod


def _generate_arguments(arguments):
    output = []
    for argument in arguments:
        output += ['{type} {name}'.format(type=argument[0], name=argument[1])]
    return ', '.join(output)


def generate_mock_method(CppMethod):
    num_args = len(CppMethod.arguments())
    method_name = CppMethod.name()
    return_type = CppMethod.return_type()
    arguments = _generate_arguments(CppMethod.arguments())
    mock_macro = 'MOCK_METHOD'
    if CppMethod.is_const():
        mock_macro = 'MOCK_CONST_METHOD'

    template = '{mock_macro}{num_args}({method_name}, {return_type}({arguments}));'
    return template.format(
        mock_macro=mock_macro,
        num_args=num_args,
        method_name=method_name,
        return_type=return_type,
        arguments=arguments
    )
