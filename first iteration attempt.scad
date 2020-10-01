//first attempted iteration of design

// all values of length in mm unless specified
 d_max = 150; //max diameter of glovebox 
 
 //dimensions
 
<<<<<<< Updated upstream
 shell_l = 200;
 shell_w = 100;
 shell_h = 100;
 thickness_l = 50;
 thickness_w = 25;
 thichness_h = 25;
=======
 include <Substrate_holder.scad>
>>>>>>> Stashed changes
 
 // outer shell
 module outer_shell(shell_l, shell_w, shell_h, thickness_l, thickness_w, thickness_h)
 {
     window_l= shell_l-thickness_l;
     window_w= shell_w-thickness_w;
     difference(){
         difference(){
     difference()
  {
    difference(){
        difference(){
        cube([shell_l,shell_w,shell_h], center=true);
     rotate([90,0,0])
    translate([shell_l/4,0,0])    
    cylinder(r=5,h=(shell_w+1), center=true);}
    rotate([90,0,0])
    translate([-shell_l/4,0,0])    
    cylinder(r=5,h=(shell_w+1), center=true);}
    
        translate([0,0,thickness_h])
    {    
    cube ([window_l,window_w,shell_h], center=true); 
    }
     }
 translate([-shell_l/2,0,(shell_h-thickness_h)/4])
 cube([thickness_l+1,25,25],center=true);
 
 }
 translate([shell_l/2,0,0])
 cube([thickness_l+1,25,25],center=true);
 }
 }
 //substrate holder

 
 outer_shell(70,70,70,20,20,20);
 {
     Substrate_holder(40,40,30);
 }
 
 //importing and translating substrate layout
 translate([-15,-15,15])
 {linear_extrude(height=1.1, center=true, convexity=10)
import(file = "substrate-layout.dxf");
}
 
 
 
 