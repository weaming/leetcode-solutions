#!/usr/bin/env python3
import os
import argparse
from importlib import import_module


def import_string(dotted_path):
    """
    Import a dotted module path and return the attribute/class designated by the
    last name in the path. Raise ImportError if the import failed.
    """
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError as err:
        raise ImportError("%s doesn't look like a module path" % dotted_path) from err

    module = import_module(module_path)

    try:
        return getattr(module, class_name)
    except AttributeError as err:
        raise ImportError(
            'Module "%s" does not define a "%s" attribute/class'
            % (module_path, class_name)
        ) from err


def main(directory):
    def get_import_path():
        for root, _, files in os.walk(directory):
            if root == directory:
                continue
            ff = list(filter(lambda x: x.endswith('.py') and x != '__init__.py', files))
            if not ff:
                continue
            for f in ff:
                yield root.replace('/', '.').strip('.') + '.' + f.rsplit('.', 1)[0]

    for x in get_import_path():
        print('=>', x)
        solution = import_string(x + '.Solution')()
        # args = getattr(solution, 'input_args', ())
        # kwargs = getattr(solution, 'input_kwargs', {})
        entry = getattr(
            solution, getattr(solution, 'entry', 'solve')
        )  # default entry method name is 'solve'
        for t in solution.tests:
            input = t['input']
            answer = t['answer']
            result = entry(input)
            arrow = f"'{input}' => {result}"
            assert result == answer, f'{arrow} != {answer}'
            print(arrow)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    args = parser.parse_args()
    main(args.directory)
