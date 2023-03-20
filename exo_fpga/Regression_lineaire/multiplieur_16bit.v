module multiplieur_16bit (a, b, p);
    input [15:0] a;
    input [15:0] b;
    output [31:0] p;

    // multiplication : addition entre les multiplications de b par chaque bit de a avec un décalage (multiplication par 2 pour décaler)
    assign p = ( (a*b[0]) + (2*a*b[1]) + (4*a*b[2]) + (8*a*b[3]) + (16*a*b[4]) + (32*a*b[5]) + (64*a*b[6]) + (128*a*b[7]) + (256*a*b[8]) + (512*a*b[9]) + (1024*a*b[10]) + (2048*a*b[11]) + (4096*a*b[12]) + (8192*a*b[13]) + (16384*a*b[14]) + (32768*a*b[15]));

endmodule