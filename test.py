import os

from our_ast import if_variable_unused
from collections import defaultdict

function_length_list = []
problems = {}
problems_per_file = defaultdict(list)
file_name = ''

def open_dir(dir_path):
    function_length_list = []
    problems["too long function"] = 0
    problems["too long file"] = 0
    problems["missing docstring"] = 0
    problems["variables unused"] = 0
    if os.path.isfile(dir_path):
        call_functions(dir_path)
        return
    files = os.listdir(dir_path)
    for file_name in files:
        file_path = os.path.join(dir_path, file_name)
        if os.path.isfile(file_path):
            if file_name.endswith('.py'):
                print(file_path)
                call_functions(file_path)
        elif os.path.isdir(file_path):
            open_dir(file_path)

def call_functions(file_path):
    request_func_len = function_length(file_path)
    request_file_len = file_length(file_path)
    request_missing_docstrings = missing_docstrings(file_path)
    request_variable_unused = variable_unused(file_path)

    if request_func_len:
        function_length_list.append(request_func_len)
        problems[request_func_len] = problems[request_func_len] + 1
        problems_per_file[file_name].append(request_func_len)
    if request_file_len:
        problems[request_file_len] = problems[request_file_len] + 1
        problems_per_file[file_name].append(request_file_len)
    if request_variable_unused:
        problems[request_variable_unused] = problems[request_variable_unused] + 1
        problems_per_file[file_name].append(request_variable_unused)
    if request_missing_docstrings:
        problems[request_missing_docstrings] = problems[request_missing_docstrings] + 1
        problems_per_file[file_name].append(request_missing_docstrings)

def get_functions_length(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        spaces = 0
        current_spaces = 0
        length = 0
        for line in file:
            if line.startswith('def '):
                function_length_list.append(length)
                print(length)
                length = 0
                spaces = len(line) - len(line.lstrip())
            else:
                current_spaces = len(line) - len(line.lstrip())
                if current_spaces > spaces:
                    length += 1
        if length > 0:
            function_length_list.append(length)
    return function_length_list

def function_length(file_path):
    list_length = get_functions_length(file_path)
    for leng in list_length:
        if leng > 20:
            return "too long function"
    return False

def get_file_length(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        line_number = 0
        for line in enumerate(file, start=1):
            line_number += 1
        return line_number

def file_length(file_path):
    this_file_length = get_file_length(file_path)
    if this_file_length > 200:
        return "too long file"
    return False


def variable_unused(file_path):
    if if_variable_unused(file_path):
        return "variables unused"
    return False

def missing_docstrings(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        inside_function = False
        function_indent = 0
        missing_docstring = False
        for line in file:
            stripped_line = line.strip()
            current_indent = len(line) - len(stripped_line)

            if 'def' in stripped_line:
                inside_function = True
                function_indent = current_indent
                continue

            if inside_function and current_indent <= function_indent:
                if not missing_docstring:
                    return  "missing docstring"
                missing_docstring = False
                inside_function = False

            if stripped_line.startswith('"""'):
                if inside_function:
                    missing_docstring = True
                    continue
    return False

