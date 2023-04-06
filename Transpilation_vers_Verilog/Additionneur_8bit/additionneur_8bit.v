`include "additionneur_1bit.v"

module additionneur_8bit (a, b, rin, s, rout);
    input [7:0] a;
    input [7:0] b;
    input rin;

    output [7:0] s;
    output rout;

    wire r0, r1, r2, r3, r4, r5, r6, r7;

    additionneur_1bit add_1(a[0], b[0], rin, s[0], r0);
    additionneur_1bit add_2(a[1], b[1], r0, s[1], r1);
    additionneur_1bit add_3(a[2], b[2], r1, s[2], r2);
    additionneur_1bit add_4(a[3], b[3], r2, s[3], r3);
    additionneur_1bit add_5(a[4], b[4], r3, s[4], r4);
    additionneur_1bit add_6(a[5], b[5], r4, s[5], r5);
    additionneur_1bit add_7(a[6], b[6], r5, s[6], r6);
    additionneur_1bit add_8(a[7], b[7], r6, s[7], r7);

    assign rout = r7;

endmodule