module and_3entries_gate (e1, e2, e3, s);
    input e1;
    input e2;
    input e3;
    output s;


    assign s = e1 & e2 & e3;

endmodule