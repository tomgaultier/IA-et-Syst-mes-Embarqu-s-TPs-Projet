module additionneur_1bit (a, b, rin, s, rout);
    input a;
    input b;
    input rin;
    output s;
    output rout;

    assign s = (a ^ b) ^ rin;
    assign rout = (a & b) | (a & rin) | (b & rin);

endmodule