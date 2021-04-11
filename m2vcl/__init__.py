
from m2cgen.exporters import _export
from .vcl.interpreter import FastlyVCLInterpreter


def export_to_vcl(model, indent=4, sub_name="score"):
    """
    Generates a VCL code representation of the given model.
    Parameters
    ----------
    model : object
        The model object that should be transpiled into code.
    indent : int, optional
        The size of indents in the generated code.
    sub_name : string, optional
        Name of the subroutine in the generated code.
    Returns
    -------
    code : string
    """
    interpreter = FastlyVCLInterpreter(
        indent=indent,
        sub_name=sub_name
    )
    return _export(model, interpreter)
