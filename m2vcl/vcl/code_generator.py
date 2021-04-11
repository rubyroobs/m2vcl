import contextlib

from m2cgen.interpreters.code_generator import CLikeCodeGenerator
from m2cgen.interpreters.code_generator import CodeTemplate


class FastlyVCLCodeGenerator(CLikeCodeGenerator):

    tpl_var_declaration = CodeTemplate(
        "declare local {var_name} FLOAT;")
    tpl_var_assignment = CodeTemplate("set {var_name} = {value};")
    tpl_array_index_access = CodeTemplate("{array_name}_{index}")
    tpl_infix_expression = CodeTemplate("{left} {op} {right}")

    def __init__(self, indent=4,
                 id_prefix="score"):
        self.id_prefix = self.header_var(id_prefix)
        super().__init__(indent)

    def header_var(self, name):
        return f"req.http.{name}"

    def reset_state(self):
        super().reset_state()
        self._sub_prefix = self.id_prefix
        self._sub_start_pos = 0
        self._output_size = 1
        self._input_idxs = {}
        self._var_sizes = {}

    def get_var_name(self):
        var_name = f"var.var{self._var_idx}"
        self._var_idx += 1
        return var_name

    def add_var_declaration(self, size):
        var_name = self.get_var_name()

        self._var_sizes[var_name] = size
        for i in range(size):
            self.add_code_line(
                self.tpl_var_declaration(var_name=f"{var_name}_{i}")
            )

        if size == 1:
            return var_name + "_0"

        return var_name

    def add_return_statement(self, value):
        if value in self._var_sizes:
            # this wont work if an array is passed directly to value
            # todo: check if that is a possibility
            self._output_size = self._var_sizes[value]

        if self._output_size > 1:
            for i in range(self._output_size):
                self.add_code_line(
                    self.tpl_var_assignment(
                        var_name=f"{self._sub_prefix}_output_{i}",
                        value=f"{value}_{i}"
                    )
                )
        else:
            self.add_code_line(self.tpl_var_assignment(
                var_name=f"{self._sub_prefix}_output_0", value=f"{value}"))

        self.add_code_line("return;")

    def add_var_assignment(self, var_name, value, value_size):
        for i in range(value_size):
            if var_name in self._var_sizes:
                var = f"{var_name}_{i}"
            else:
                var = var_name
            self.add_code_line(
                self.tpl_var_assignment(
                    var_name=var,
                    value=(value[i] if value_size > 1 else value)
                )
            )

    def add_function_def(self, name, args, is_vector_output):
        if args != [(True, "input")]:
            print(args)
            raise "Unexpected args given from FastlyVCLInterpreter"

        self.add_code_line(f"sub {name} {{")
        self._sub_start_pos = self._code_buf.tell()
        self.increase_indent()

    @contextlib.contextmanager
    def function_definition(self, name, args, is_vector_output):
        if self._sub_prefix != self.header_var(name):
            self._sub_prefix = f"{self._sub_prefix}_{name}"

        self.add_function_def(name, args, is_vector_output)
        yield
        self.add_block_termination()

        self._code_buf.seek(0)
        content = self._code_buf.read(self._sub_start_pos)
        for index, var_name in self._input_idxs.items():
            content += str(self._indent * " ") + \
                self.tpl_var_declaration(var_name=var_name) + "\n"
            content += str(self._indent * " ")
            content += self.tpl_var_assignment(
                var_name=f"{var_name}",
                value=f"std.atof({self.id_prefix}_input_{index})"
            )
            content += "\n\n"

        content += self._code_buf.read()
        self._code_buf.seek(0)
        self._code_buf.write(content)

    def infix_expression(self, left, right, op):
        if op == "=":
            raise "Assignment should be done with add_var_assignment"
        elif op in ["+", "-", "*", "/", "%", "|", "&", "^", "<<", ">>", "rol"]:
            # this could be optimized
            var_name = self.add_var_declaration(1)
            self.add_var_assignment(var_name, left, 1)
            self.add_code_line(f"set {var_name} {op}= {right};")
            return var_name

        return self.tpl_infix_expression(left=left, right=right, op=op)

    def sub_invocation(self, sub_name):
        self.add_code_line(f"call {sub_name};")
        var_name = self.add_var_declaration(1)
        self.add_var_assignment(
            var_name,
            f"std.atof({self.id_prefix}_{sub_name}_output_0)",
            1
        )
        return var_name

    def array_index_access(self, array_name, index):
        if array_name == "input":
            var_name = f"var.input_{index}"
            self._input_idxs[index] = var_name
            return var_name

        return super().array_index_access(array_name, index)

    def vector_init(self, values):
        # vectors must be assigned value by value
        # this is done in add_var_assignment
        return values
