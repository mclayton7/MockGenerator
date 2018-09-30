import clang.cindex
import pprint

from class_parser import class_factory


class HeaderParser(object):
    def __init__(self, file_name):
        self._file_name = file_name
        self._forward_declares = []
        self._classes = []

        index = clang.cindex.Index.create()
        tu = index.parse(file_name, args=['-x', 'c++'])
        self.visit_node(tu.cursor)


    def __repr__(self):
        template = 'Interface name: {interface_name}'
        return template.format(interface_name=self._interface_name)

    def classes(self):
        return self._classes

    def visit_node(self, cursor):
        if cursor.kind == clang.cindex.CursorKind.CLASS_DECL:
            if cursor.is_definition():
                self._classes.append(class_factory(cursor))
            else:
                self._forward_declares += [cursor.spelling]
        for child in cursor.get_children():
            self.visit_node(child)
