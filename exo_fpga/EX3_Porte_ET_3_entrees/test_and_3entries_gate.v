`timescale 1ns / 1ps
`include "and_3entries_gate.v"

module stimulus;
	// Inputs
	reg w;
    reg x;
	reg y;
	// Outputs
	wire z;
	// Instantiate the Unit Under Test (UUT)
	and_3entries_gate uut (
		w,
        x, 
		y, 
		z
	);
 
	initial begin
	$dumpfile("test.vcd");
    $dumpvars(0,stimulus);
	// Initialize Inputs
    w = 0;
	x = 0;
	y = 0;
    
    #20 w = 1;
	#20 x = 1;
	#20 y = 1;
	#20 y = 0;	
	#20 x = 0;	  
	#40 ;
 
	end  
 
	initial begin
	$monitor("t=%3d w=%d,x=%d,y=%d,z=%d \n",$time,w,x,y,z, );
	end
 
endmodule