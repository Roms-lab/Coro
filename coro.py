from lark import Lark, Transformer, Tree, Token

coro_file = "test.co"
file_name_w = "Coro_Output.cpp"
content_to_write = ""

# --- Read the grammar from the file ---
try:
    with open("syntax.lark", "r") as f:
        coro_syntax = f.read()
except FileNotFoundError:
    print("Error: 'syntax.lark' not found. Please create the file with the grammar definition.")
    exit(1)

class CoroToCpp(Transformer):
    def __init__(self):
        super().__init__()
        self.cpp_includes = set()

    def start(self, statements):
        main_body = "\n".join(statements)
        includes_str = "\n".join(sorted(list(self.cpp_includes)))
        
        return f"""\
{includes_str}

int main() {{
{main_body}
    return 0;
}}
"""

    def io_import_iostream(self, _):
        self.cpp_includes.add("#include <iostream>")
        return ""

    def io_import_clib(self, _):
        self.cpp_includes.add("#include <cstdlib>")
        return ""
    
    def io_import_time(self, _):
        self.cpp_includes.add("#include <chrono>")
        self.cpp_includes.add("#include <thread>")
        return ""

    def io_print_statement(self, items):
        """
        Transforms a coro print statement with multiple chained items.
        `items` will be a list of transformed print_item children.
        """
        output_parts = []
        for item in items:
            if isinstance(item, Tree) and item.data == 'io_endl':
                output_parts.append('endl')
            else:
                # Handle both string values and Tree objects
                if isinstance(item, Token):
                    output_parts.append(item.value)
                else:
                    output_parts.append(str(item))
        
        cpp_expression = " << ".join(output_parts)
        
        return f"    cout << {cpp_expression};"
    
    def io_endl(self, _):
        # Return a special Tree object so we can distinguish it in io_print_statement.
        return Tree('io_endl', [])
    
    def io_readln_statement(self, children):
        # 'children' is a list containing the CNAME token
        # The CNAME will be a Token object, so we access its value
        variable_name = children[0].value
        return f"    string {variable_name}; cin >> {variable_name};"

    def ESCAPED_STRING(self, s):
        # This is a terminal; we just return its value.
        return s.value
        
    def CNAME(self, c):
        # This is a terminal; we just return its value.
        return c.value

    def statement(self, children):
        # children is a list containing the single transformed statement
        return children[0] if children else ""

    def io_newline(self, _):
        # This rule is not part of a statement that needs to generate code, so we ignore it.
        return ""

try:
    with open(coro_file, "r") as f:
        coro_code = f.read()
except FileNotFoundError:
    print("Error: <file>.co not found. Please create a .co file and try re-compiling.")
    exit(1)
except:
    print("Unknown Error During Compilation.")
    exit(1)

if __name__ == '__main__':
    parser = Lark(coro_syntax, parser='lalr', start='start')

    try:
        # Parse the code
        tree = parser.parse(coro_code)
        
        # Transform the parse tree into C++ code
        cpp_code_output = CoroToCpp().transform(tree)
        
        # Print the generated C++ code
        print("--- Generated C++ Code ---")
        print(cpp_code_output)
    except Exception as e:
        print(f"An error occurred: {e}")

# Set content to write to cpp code output
content_to_write = cpp_code_output

with open(file_name_w, 'w') as file_object:
    file_object.write(content_to_write)

print(f"Content written to '{file_name_w}' in write mode.")

# Append to an existing file (or create if not exists)
file_name_a = "Coro_Output.cpp"