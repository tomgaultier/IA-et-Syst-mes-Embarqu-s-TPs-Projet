`include "additionneur_16bit.v"

module additionneur_32bit (a, b, rin, s, rout);


    // Inputs
    input [31:0] a;
    input [31:0] b;
    input rin;
    // Outputs
    output [31:0] s;
    output rout;

    wire r0, r1;

    additionneur_16bit add_1(a[15:0], b[15:0], rin, s[15:0], r0);
    additionneur_16bit add_2(a[31:16], b[31:16], r0, s[31:16], r1);

    assign rout = r1;

endmodule