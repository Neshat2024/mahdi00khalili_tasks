"""
Write a Python code that takes a Python file as input 
and adds a print before each instruction to show what is being executed.
"""


def add_print_statements(input_file):
    with open(input_file, 'r') as file:
        code = file.readlines()

    modified_code = []
    for line in code:
        # Skip empty lines and lines with only whitespace
        if line.strip():
            modified_code.append(f"print('Executing: {line.strip()}')\n")
        modified_code.append(line)

    output_file = input_file.replace('.py', '_with_prints.py')
    with open(output_file, 'w') as file:
        file.writelines(modified_code)

    print(f"Print statements added. Modified code saved in '{output_file}'.")

if __name__ == "__main__":
    input_file = input("Enter the Python file name: ")
    add_print_statements(input_file)
