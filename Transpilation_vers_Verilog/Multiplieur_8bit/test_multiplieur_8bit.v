`timescale 1ns / 1ps
`include "multiplieur_8bit.v"

module stimulus;
	// Inputs
	reg [7:0] a;
    reg [7:0] b;
	// Outputs
	wire [15:0] p;
	// Instantiate the Unit Under Test (UUT)
	multiplieur_8bit uut (
		a,
        b,
		p
	);
 
	initial begin
	$dumpfile("test.vcd");
    $dumpvars(0,stimulus);
	// Initialize Inputs
    a = 0;
	b = 0;
    
    #20 a = 8'b11001001;
	#20 b = 8'b00001100;
	#20 b = 8'b01001011; 
	#40 ;
 
	end  
 
	initial begin
	$monitor("t=%3d a=%d,b=%d,p=%d \n",$time,a,b,p, );
	end
 
endmodule