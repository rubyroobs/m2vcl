sub score {
    declare local var.input_0 FLOAT;
    set var.input_0 = std.atof(req.http.score_input_0);

    declare local var.input_1 FLOAT;
    set var.input_1 = std.atof(req.http.score_input_1);

    declare local var.input_2 FLOAT;
    set var.input_2 = std.atof(req.http.score_input_2);

    declare local var.input_3 FLOAT;
    set var.input_3 = std.atof(req.http.score_input_3);

    declare local var.input_4 FLOAT;
    set var.input_4 = std.atof(req.http.score_input_4);

    declare local var.input_5 FLOAT;
    set var.input_5 = std.atof(req.http.score_input_5);

    declare local var.input_6 FLOAT;
    set var.input_6 = std.atof(req.http.score_input_6);

    declare local var.input_7 FLOAT;
    set var.input_7 = std.atof(req.http.score_input_7);

    declare local var.input_8 FLOAT;
    set var.input_8 = std.atof(req.http.score_input_8);

    declare local var.input_9 FLOAT;
    set var.input_9 = std.atof(req.http.score_input_9);

    declare local var.input_10 FLOAT;
    set var.input_10 = std.atof(req.http.score_input_10);

    declare local var.input_11 FLOAT;
    set var.input_11 = std.atof(req.http.score_input_11);

    declare local var.input_12 FLOAT;
    set var.input_12 = std.atof(req.http.score_input_12);

    declare local var.var0_0 FLOAT;
    set var.var0_0 = var.input_0;
    set var.var0_0 *= -0.10801135783679545;
    declare local var.var1_0 FLOAT;
    set var.var1_0 = var.var0_0;
    declare local var.var2_0 FLOAT;
    set var.var2_0 = 36.459488385090125;
    set var.var2_0 += var.var1_0;
    declare local var.var3_0 FLOAT;
    set var.var3_0 = var.var2_0;
    declare local var.var4_0 FLOAT;
    set var.var4_0 = var.input_1;
    set var.var4_0 *= 0.04642045836688176;
    declare local var.var5_0 FLOAT;
    set var.var5_0 = var.var4_0;
    declare local var.var6_0 FLOAT;
    set var.var6_0 = var.var3_0;
    set var.var6_0 += var.var5_0;
    declare local var.var7_0 FLOAT;
    set var.var7_0 = var.var6_0;
    declare local var.var8_0 FLOAT;
    set var.var8_0 = var.input_2;
    set var.var8_0 *= 0.02055862636707862;
    declare local var.var9_0 FLOAT;
    set var.var9_0 = var.var8_0;
    declare local var.var10_0 FLOAT;
    set var.var10_0 = var.var7_0;
    set var.var10_0 += var.var9_0;
    declare local var.var11_0 FLOAT;
    set var.var11_0 = var.var10_0;
    declare local var.var12_0 FLOAT;
    set var.var12_0 = var.input_3;
    set var.var12_0 *= 2.6867338193448966;
    declare local var.var13_0 FLOAT;
    set var.var13_0 = var.var12_0;
    declare local var.var14_0 FLOAT;
    set var.var14_0 = var.var11_0;
    set var.var14_0 += var.var13_0;
    declare local var.var15_0 FLOAT;
    set var.var15_0 = var.var14_0;
    declare local var.var16_0 FLOAT;
    set var.var16_0 = var.input_4;
    set var.var16_0 *= -17.766611228300167;
    declare local var.var17_0 FLOAT;
    set var.var17_0 = var.var16_0;
    declare local var.var18_0 FLOAT;
    set var.var18_0 = var.var15_0;
    set var.var18_0 += var.var17_0;
    declare local var.var19_0 FLOAT;
    set var.var19_0 = var.var18_0;
    declare local var.var20_0 FLOAT;
    set var.var20_0 = var.input_5;
    set var.var20_0 *= 3.809865206809212;
    declare local var.var21_0 FLOAT;
    set var.var21_0 = var.var20_0;
    declare local var.var22_0 FLOAT;
    set var.var22_0 = var.var19_0;
    set var.var22_0 += var.var21_0;
    declare local var.var23_0 FLOAT;
    set var.var23_0 = var.var22_0;
    declare local var.var24_0 FLOAT;
    set var.var24_0 = var.input_6;
    set var.var24_0 *= 0.0006922246403425021;
    declare local var.var25_0 FLOAT;
    set var.var25_0 = var.var24_0;
    declare local var.var26_0 FLOAT;
    set var.var26_0 = var.var23_0;
    set var.var26_0 += var.var25_0;
    declare local var.var27_0 FLOAT;
    set var.var27_0 = var.var26_0;
    declare local var.var28_0 FLOAT;
    set var.var28_0 = var.input_7;
    set var.var28_0 *= -1.475566845600255;
    declare local var.var29_0 FLOAT;
    set var.var29_0 = var.var28_0;
    declare local var.var30_0 FLOAT;
    set var.var30_0 = var.var27_0;
    set var.var30_0 += var.var29_0;
    declare local var.var31_0 FLOAT;
    set var.var31_0 = var.var30_0;
    declare local var.var32_0 FLOAT;
    set var.var32_0 = var.input_8;
    set var.var32_0 *= 0.30604947898517226;
    declare local var.var33_0 FLOAT;
    set var.var33_0 = var.var32_0;
    declare local var.var34_0 FLOAT;
    set var.var34_0 = var.var31_0;
    set var.var34_0 += var.var33_0;
    declare local var.var35_0 FLOAT;
    set var.var35_0 = var.var34_0;
    declare local var.var36_0 FLOAT;
    set var.var36_0 = var.input_9;
    set var.var36_0 *= -0.01233459391657437;
    declare local var.var37_0 FLOAT;
    set var.var37_0 = var.var36_0;
    declare local var.var38_0 FLOAT;
    set var.var38_0 = var.var35_0;
    set var.var38_0 += var.var37_0;
    declare local var.var39_0 FLOAT;
    set var.var39_0 = var.var38_0;
    declare local var.var40_0 FLOAT;
    set var.var40_0 = var.input_10;
    set var.var40_0 *= -0.9527472317072923;
    declare local var.var41_0 FLOAT;
    set var.var41_0 = var.var40_0;
    declare local var.var42_0 FLOAT;
    set var.var42_0 = var.var39_0;
    set var.var42_0 += var.var41_0;
    declare local var.var43_0 FLOAT;
    set var.var43_0 = var.var42_0;
    declare local var.var44_0 FLOAT;
    set var.var44_0 = var.input_11;
    set var.var44_0 *= 0.009311683273793711;
    declare local var.var45_0 FLOAT;
    set var.var45_0 = var.var44_0;
    declare local var.var46_0 FLOAT;
    set var.var46_0 = var.var43_0;
    set var.var46_0 += var.var45_0;
    declare local var.var47_0 FLOAT;
    set var.var47_0 = var.var46_0;
    declare local var.var48_0 FLOAT;
    set var.var48_0 = var.input_12;
    set var.var48_0 *= -0.5247583778554923;
    declare local var.var49_0 FLOAT;
    set var.var49_0 = var.var48_0;
    declare local var.var50_0 FLOAT;
    set var.var50_0 = var.var47_0;
    set var.var50_0 += var.var49_0;
    set req.http.score_output_0 = var.var50_0;
    return;
}