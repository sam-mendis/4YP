//first attempted iteration of design

// all values of length in mm unless specified
 d_max = 150; //max diameter of glovebox 
 
 //dimensions

 shell_l = 200;
 shell_w = 100;
 shell_h = 100;
 thickness_l = 50;
 thickness_w = 25;
 thichness_h = 25;
//  s_d= screw diameter
//  s_l= screw length
 include <Substrate_holder.scad>

 // outer shell
 include <outer_shell.scad>

 {
     Substrate_holder(40,40,30);
 }
 
 //importing and translating substrate layout
 translate([-15,-15,15])
 {
linear_extrude(height=1.1, center=true, convexity=10)
import(file = "substrate-layout.dxf");
}
 
 
 
 