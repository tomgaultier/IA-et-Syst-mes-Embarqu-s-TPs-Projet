module multiplieur_8bit (a, b, p);
    input [7:0] a;
    input [7:0] b;
    output [15:0] p;

    // multiplication : addition entre les multiplications de b par chaque bit de a avec un décalage (multiplication par 2 pour décaler)
    assign p = ( (a*b[0]) + (2*a*b[1]) + (4*a*b[2]) + (8*a*b[3]) + (16*a*b[4]) + (32*a*b[5]) + (64*a*b[6]) + (128*a*b[7]) );

endmodule