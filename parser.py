

# parser.py

import re

def parse_psr_code(code):
    lines = code.split('\n')
    parsed_code = []

    for line in lines:
        line = line.strip()

        if line.startswith('screentext'):
            text = re.search(r'screentext"(.+)"', line).group(1)
            parsed_code.append(f'print("{text}")')
        elif line.startswith('If'):
            condition = re.search(r'If\s+(.*)\s+{', line).group(1)
            parsed_code.append(f'if {condition}:')
        elif line.startswith('Elif'):
            condition = re.search(r'Elif\s+(.*)\s+{', line).group(1)
            parsed_code.append(f'elif {condition}:')
        elif line.startswith('Else'):
            parsed_code.append('else:')
        elif line.startswith('loop.ve'):
            count = re.search(r'loop\.ve(\d+)\s*{', line).group(1)
            parsed_code.append(f'for i in range({count}):')
        elif line.startswith('import'):
            module = re.search(r'import"(.+)"', line).group(1)
            parsed_code.append(f'# Importar módulo {module}')
        elif line.startswith('function'):
            func_name = re.search(r'function\s+(\w+)', line).group(1)
            parsed_code.append(f'def {func_name}():')
        elif line.startswith('tryto'):
            script = re.search(r'tryto"(.+)"', line).group(1)
            parsed_code.append(f'try:')
        elif line.startswith('error'):
            error_msg = re.search(r'error"(.+)"', line).group(1)
            parsed_code.append(f'except {error_msg}:')
        elif line.startswith('with'):
            script = re.search(r'with"(.+)" response (\w+) on {', line).group(1)
            response_var = re.search(r'with"(.+)" response (\w+) on {', line).group(2)
            parsed_code.append(f'try:')
            parsed_code.append(f'    response = {script}')
            parsed_code.append(f'{response_var} = response')
        elif re.match(r'var \w+ = \d+', line):
            var_name, value = re.findall(r'var (\w+) = (\d+)', line)[0]
            parsed_code.append(f'{var_name} = {value}')
        elif re.match(r'var \w+ = \{.+\}', line):
            var_name, content = re.findall(r'var (\w+) = \{(.+)\}', line)[0]
            parsed_code.append(f'{var_name} = {{{content}}}')
        elif re.match(r'var \w+ = \[.+\]', line):
            var_name, content = re.findall(r'var (\w+) = \[(.+)\]', line)[0]
            parsed_code.append(f'{var_name} = [{content}]')

    return '\n'.join(parsed_code)

if __name__ == "__main__":
    with open('mp.psr', 'r') as file:
        code = file.read()
    parsed_code = parse_psr_code(code)
    print(parsed_code)
