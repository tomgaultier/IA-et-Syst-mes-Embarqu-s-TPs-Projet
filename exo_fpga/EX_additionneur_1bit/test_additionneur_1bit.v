`timescale 1ns / 1ps
`include "additionneur_1bit.v"

module stimulus;
	// Inputs
	reg a;
    reg b;
	reg rin;
	// Outputs
	wire s;
	wire rout;
	// Instantiate the Unit Under Test (UUT)
	additionneur_1bit uut (
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
    
    #20 a = 1;
	#20 b = 1;
	#20 rin = 1;
	#20 b = 0;	  
	#40 ;
 
	end  
 
	initial begin
	$monitor("t=%3d a=%d,b=%d,rin=%d,s=%d,rout=%d \n",$time,a,b,rin,s,rout, );
	end
 
endmodule