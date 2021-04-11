from m2cgen import ast
from m2cgen.interpreters.interpreter import BaseToCodeInterpreter
from m2cgen.interpreters.mixins import SubroutinesMixin


class VCLSubroutinesMixin(SubroutinesMixin):

    def _pre_interpret_hook(self, expr, ast_size_check_counter=0, **kwargs):
        if isinstance(expr, ast.BinExpr) and not expr.to_reuse:
            frequency = self._adjust_ast_check_frequency(expr)
            self.ast_size_check_frequency = min(
                frequency, self.ast_size_check_frequency)

            ast_size_check_counter += 1
            if ast_size_check_counter >= self.ast_size_check_frequency:
                ast_size_check_counter = 0
                ast_size = ast.count_exprs(expr)
                if ast_size > self.ast_size_per_subroutine_threshold:
                    sub_name = self._get_subroutine_name()
                    self.enqueue_subroutine(sub_name, expr)
                    return self._cg.sub_invocation(
                        sub_name
                    ), kwargs

            kwargs['ast_size_check_counter'] = ast_size_check_counter

        return BaseToCodeInterpreter._pre_interpret_hook(self, expr, **kwargs)
