from lark import Lark, Transformer, Tree, Token, v_args

coro_file = "test.co"
file_name_w = "Coro_Output.cpp"
content_to_write = ""

# --- Read the syntax from the file ---
try:
    with open("syntax.lark", "r") as f:
        coro_syntax = f.read()
except FileNotFoundError:
    print("Error: 'syntax.lark' not found. Please create the file with the grammar definition.")
    exit(1)

@v_args(inline=True)
class CoroToCpp(Transformer):
    def __init__(self):
        super().__init__()
        self.cpp_includes = set()

    def start(self, *statements):
        main_body = "\n".join(statements)
        includes_str = "\n".join(sorted(list(self.cpp_includes)))
        
        return f"""\
{includes_str}

int main() {{
{main_body}
    return 0;
}}
"""
    
    def statement(self, child):
        return child

    def io_import_iostream(self):
        self.cpp_includes.add("#include <iostream>")
        return ""

    def io_import_clib(self):
        self.cpp_includes.add("#include <cstdlib>")
        return ""
    
    def io_import_time(self):
        self.cpp_includes.add("#include <chrono>")
        self.cpp_includes.add("#include <thread>")
        return ""

    def io_print_statement(self, *items):
        output_parts = [str(item) for item in items]
        cpp_expression = " << ".join(output_parts)
        
        return f"    std::cout << {cpp_expression};"

    def print_item(self, child):
        return child
    
    def io_endl(self):
        return "std::endl"
    
    def io_readln_statement(self, var_name):
        self.cpp_includes.add("#include <string>")
        return f"    std::string {var_name}; std::cin >> {var_name};"

    def io_wait_seconds(self, wait_time):
        self.cpp_includes.add("#include <chrono>")
        self.cpp_includes.add("#include <thread>")
        return f"    std::this_thread::sleep_for(std::chrono::seconds({wait_time}));"

    def ESCAPED_STRING(self, s):
        return s.value
        
    def CNAME(self, c):
        return c.value

    def NUMBER(self, n):
        return n.value

try:
    with open(coro_file, "r") as f:
        coro_code = f.read()
except FileNotFoundError:
    print(f"Error: '{coro_file}' not found. Please create a .co file and try re-compiling.")
    exit(1)
except Exception:
    print("Unknown Error During Compilation.")
    exit(1)

if __name__ == '__main__':
    parser = Lark(coro_syntax, parser='lalr', start='start')

    try:
        tree = parser.parse(coro_code)
        cpp_code_output = CoroToCpp().transform(tree)
        
        print("--- Generated C++ Code ---")
        print(cpp_code_output)
    except Exception as e:
        print(f"An error occurred: {e}")
        cpp_code_output = ""

    content_to_write = cpp_code_output

    with open(file_name_w, 'w') as file_object:
        file_object.write(content_to_write)

    if cpp_code_output:
        print(f"\nContent written to '{file_name_w}'.")
    else:
        print(f"\nNo content written to '{file_name_w}' due to an error.")
