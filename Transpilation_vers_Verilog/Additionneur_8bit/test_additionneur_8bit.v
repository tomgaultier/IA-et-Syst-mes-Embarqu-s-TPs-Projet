`timescale 1ns / 1ps
`include "additionneur_8bit.v"

module stimulus;
	// Inputs
	reg [7:0] a;
    reg [7:0] b;
	reg rin;
	// Outputs
	wire [7:0] s;
	wire rout;
	// Instantiate the Unit Under Test (UUT)
	additionneur_8bit uut (
		a,
        b,
		rin,
		s,
		rout
	);
 
	initial begin
	$dumpfile("test.vcd");
    $dumpvars(0,stimulus);
	// Initialize Inputs
    a = 0;
	b = 0;
	rin = 0;
    
    #20 a = 8'b11001001;
	#20 b = 8'b00001100;
	#20 b = 8'b01001011;  
	#40 ;
 
	end  
 
	initial begin
	$monitor("t=%3d a=%d,b=%d,s=%d,rout=%d \n",$time,a,b,s,rout, );
	end
 
endmodule