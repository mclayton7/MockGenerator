from method_parser import CppMethod


def generate_mock_method(CppMethod):
    template = '{mock_macro}{num_args}({method_name}, {return_type}());'
    num_args = len(CppMethod.arguments())
    mock_macro = 'MOCK_METHOD'
    method_name = CppMethod.name()
    return_type = CppMethod.return_type()
    if CppMethod.is_const():
        mock_macro = 'MOCK_CONST_METHOD'

    return template.format(
        mock_macro=mock_macro,
        num_args=num_args,
        method_name=method_name,
        return_type=return_type,
    )
