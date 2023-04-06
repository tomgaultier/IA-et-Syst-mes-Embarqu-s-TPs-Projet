`include "multiplieur_16bit.v"
`include "additionneur_32bit.v"

module regression_lineaire (x, y);

	// Inputs
	input [15:0] x;
	// Outputs
	output [31:0] y;

	wire [31:0] p;
	wire rin;
	wire rout;



	multiplieur_16bit mult(16'b0010011100010000, x, p);

	additionneur_32bit add(32'b00000000000000000010011100010000 , p, 1'b0, y, rout);
	
endmodule