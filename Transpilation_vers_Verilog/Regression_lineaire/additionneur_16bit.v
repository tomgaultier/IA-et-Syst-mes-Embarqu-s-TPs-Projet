`include "additionneur_8bit.v"

module additionneur_16bit (a, b, rin, s, rout);


    // Inputs
    input [15:0] a;
    input [15:0] b;
    input rin;
    // Outputs
    output [15:0] s;
    output rout;

    wire r0, r1;

    additionneur_8bit add_1(a[7:0], b[7:0], rin, s[7:0], r0);
    additionneur_8bit add_2(a[15:8], b[15:8], r0, s[15:8], r1);

    assign rout = r1;

endmodule