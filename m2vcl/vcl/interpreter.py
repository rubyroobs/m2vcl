from m2cgen.interpreters import mixins
from m2cgen.interpreters.interpreter import ImperativeToCodeInterpreter
from .code_generator import FastlyVCLCodeGenerator
from .mixins import VCLSubroutinesMixin


class FastlyVCLInterpreter(ImperativeToCodeInterpreter,
                           mixins.LinearAlgebraMixin,
                           mixins.BinExpressionDepthTrackingMixin,
                           VCLSubroutinesMixin):

    # VCL does not allow x = y * z style operations
    bin_depth_threshold = 1

    ast_size_check_frequency = 2
    ast_size_per_subroutine_threshold = 200

    abs_function_name = "math.trunc"
    atan_function_name = "math.atan"
    exponent_function_name = "math.exp"
    exp2_function_name = "math.exp2"
    logarithm_function_name = "math.log"
    log1p_function_name = "math.log1p"
    sqrt_function_name = "math.sqrt"
    tanh_function_name = "math.tanh"

    def __init__(self, indent=4, sub_name="score",
                 *args, **kwargs):
        self.indent = indent
        self.sub_name = sub_name

        super().__init__(None, *args, **kwargs)

    def interpret(self, expr):
        top_cg = self.create_code_generator()

        self.enqueue_subroutine(self.sub_name, expr)
        self.process_subroutine_queue(top_cg)

        return top_cg.finalize_and_get_generated_code()

    def create_code_generator(self):
        return FastlyVCLCodeGenerator(
            indent=self.indent,
            id_prefix=self.sub_name,
        )

    def interpret_pow_expr(self, expr, **kwargs):
        # Fastly VCL doesn't have a math.pow, so hack around this
        base_result = self._do_interpret(expr.base_expr, **kwargs)
        exp_result = self._do_interpret(expr.exp_expr, **kwargs)

        if exp_result == "2.0":
            return self._cg.function_invocation(
                self.exp2_function_name, exp_result)

        var_name = self._cg.add_var_declaration(1)
        self._cg.add_var_assignment(
            var_name,
            self._cg.function_invocation(
                self.logarithm_function_name,
                exp_result
            ),
            1
        )
        self._cg.add_code_line(
            f"set {var_name} *= {base_result};"
        )
        self._cg.add_var_assignment(
            var_name,
            self._cg.function_invocation(
                self.exponent_function_name,
                var_name
            ),
            1
        )
        return var_name
