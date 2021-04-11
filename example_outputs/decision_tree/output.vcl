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