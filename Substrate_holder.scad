 
 use <MCAD/boxes.scad>
 
 

 module Substrate_holder(x,y,z)
 {
     difference(){
     difference(){
   cube([x,y,z],center=true);
         {translate([0,0,15+0.001])
    cube([31,34,1.11],center=true); }
         
     }
     
      rotate([0,0,0]) 
    { roundedBox(size=[x+1,y-20,z-20],radius=4,center=true);
    }
 
 }
     }
 
 Substrate_holder(40,40,30);