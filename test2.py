from our_ast import if_variable_unused

def get_functions_length(file_path):
    function_length_list = []
    with open(file_path, 'r') as file:
        spaces = 0
        current_spaces = 0
        length = 0
        for line_number, line in enumerate(file, start=1):
            if 'def' in line:
                function_length_list.append(length)
                print(length)
                length = 0
                spaces = len(line) - len(line.lstrip())
            else:
                current_spaces = len(line) - len(line.lstrip())
                if current_spaces > spaces:
                    length += 1
    return function_length_list

def function_length(file_path):
    list_length = get_functions_length(file_path)
    for leng in list_length:
        if leng > 20:
            return False
    return True

def get_file_length(file_path):
    with open(file_path, 'r') as file:
        line_number = 0
        for line in enumerate(file, start=1):
            line_number += 1
        if line_number < 200:
            return True
    return False

def file_length(file_path):
    this_file_length = get_file_length(file_path)


def variable_unused(file_path):
    return if_variable_unused(file_path)
    # with open(file_path, 'r') as file:
    #     variable_outside_func = {}
    #     inside_function = False
    #     function_indent = 0
    #     variables = {}
    #     for line in file:
    #         stripped_line = line.strip()
    #         current_indent = len(line) - len(stripped_line)
    #
    #         if 'def' in stripped_line:
    #             if any(value is False for value in variables.values()):
    #                 return False
    #             variables = {}
    #             inside_function = True
    #             function_indent = current_indent
    #             continue
    #
    #         if inside_function and current_indent <= function_indent:
    #             inside_function = False
    #
    #         if '=' in stripped_line:
    #             word = line.split('=')[0].strip()
    #             if inside_function:
    #                 if word not in variables:
    #                     if word in variable_outside_func:
    #                         variable_outside_func[word] = True
    #                     else:
    #                         variables[word] = False
    #                 else:
    #                     variables[word] = True
    #             else:
    #                 if word not in variable_outside_func:
    #                     variable_outside_func[word] = False
    #                 else:
    #                     variable_outside_func[word] = True
    #
    # if any(value is False for value in variables.values()) or any(
    #         value is False for value in variable_outside_func.values()):
    #     return False
    # return True


def missing_docstrings(file_path):
    with open(file_path, 'r') as file:
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
                    return  False
                missing_docstring = False
                inside_function = False

            if stripped_line.startswith('"""'):
                if inside_function:
                    missing_docstring = True
                    continue
    return True

