# m2vcl

![CI Tests status badge](https://github.com/rubyroobs/m2vcl/workflows/CI%20Tests/badge.svg)

Experimental extension of [m2cgen](https://github.com/BayesWitnesses/m2cgen) to export statistical models to [Varnish Configuration Language](https://varnish-cache.org/docs/trunk/users-guide/vcl.html), for use in the Varnish cache. Right now only Fastly-flavored VCL is the only target supported, though this could theoretically partially target core Varnish in the future.

## Examples

For code examples and their generated VCL outputs, see the [example_outputs](https://github.com/rubyroobs/m2vcl/tree/master/example_outputs) directory. 

## Usage

Use `export_to_fastly_vcl` to export to Fastly-flavored VCL. The `export_to_fasty_vcl` function takes arguemnts `indent` (defaults to 4, indent size in the generated VCL) and `sub_name` (defaults to `score`, the prefix for the generated subroutine and input/output header names). Inputs for the subroutine can be set on the headers `req.http.<prefix>_input_<index>` and outputs will be set on the header `req.http.<prefix>_output_<index>`. 

A working demo is available in [this Fastly fiddle](https://fiddle.fastlydemo.net/fiddle/754b1898), with the source provided below:

### Generating Python code

```
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

import m2vcl

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=0)

clf = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
clf.fit(X_train, y_train)
print(m2vcl.export_to_vcl(clf))
```

### Output VCL

```
sub score {
    declare local var.input_3 FLOAT;
    set var.input_3 = std.atof(req.http.score_input_3);

    declare local var.input_2 FLOAT;
    set var.input_2 = std.atof(req.http.score_input_2);

    declare local var.var0_0 FLOAT;
    declare local var.var0_1 FLOAT;
    declare local var.var0_2 FLOAT;
    if (var.input_3 <= 0.800000011920929) {
        set var.var0_0 = 1.0;
        set var.var0_1 = 0.0;
        set var.var0_2 = 0.0;
    } else {
        if (var.input_2 <= 4.950000047683716) {
            set var.var0_0 = 0.0;
            set var.var0_1 = 0.9166666666666666;
            set var.var0_2 = 0.08333333333333333;
        } else {
            set var.var0_0 = 0.0;
            set var.var0_1 = 0.02564102564102564;
            set var.var0_2 = 0.9743589743589743;
        }
    }
    set req.http.score_output_0 = var.var0_0;
    set req.http.score_output_1 = var.var0_1;
    set req.http.score_output_2 = var.var0_2;
    return;
}
```

### VCL Usage

```
# VCL_DELIVER
set req.http.score_input_2 = "1.23456789";
set req.http.score_input_3 = "9.87654321";
call score;
set resp.http.Score-Result-0 = req.http.score_output_0;
set resp.http.Score-Result-1 = req.http.score_output_1;
set resp.http.Score-Result-2 = req.http.score_output_2;
```

## Known limitations

* Precision is limited due to limitations of Fastly, and will be lost for each subroutine the AST is broken down into due to the required float -> string -> float conversion.
* Only tested with a small subset of models i.e. highly experimental - make sure to sanity check outputs

## Todo

* Improve test coverage by performing end to end testing on Fastly
* Create tests for more models
* Support core Varnish (may require a VMOD to provide equivalent functionality of [Fastly's math trig](https://developer.fastly.com/reference/vcl/functions/math-trig/))