`timescale 1ns / 1ps
`include "regression_lineaire.v"

module stimulus;
	// Inputs
	reg [15:0] x;
	// Outputs
	wire [31:0] y;
	// Instantiate the Unit Under Test (UUT)
	regression_lineaire uut (
		x,
        y
	);
 
	initial begin
	$dumpfile("test.vcd");
    $dumpvars(0,stimulus);
	// Initialize Inputs
    x = 0;
    
    #20 x = 16'b0000000010000100;
	#20 x = 16'b0000000010111010;
	#40 ;
 
	end  
 
	initial begin
	$monitor("t=%3d x=%d,y=%d \n",$time,x,y, );
	end
 
endmodule