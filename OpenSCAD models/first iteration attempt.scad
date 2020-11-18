////first attempted iteration of design
//// Anything blue is Aluminium
/// Anything yellow is ABS
/// ANything red is Acrylic
///black is imported components
// all values of length in mm unless specified
 d_max = 150; //max diameter of glovebox 
 
 //dimensions
// length = 110 mm
//width   = 100 mm
//height  = 70 mm


//  s_d= screw diameter
//  s_l= screw length
 include <Substrate_holder.scad>
 translate([5,0,-5])
 Substrate_holder(40,40,30);

 // outer shell
 include <outer_shell.scad>
outer_shell(110,100,70,30,30,20,4,10,1.3);

//substrate layout
include <substratelayout.scad>
translate([-5,-15,10])
    {
    substratelayout();
    }
    
    //cell connections window
    include <cell_contacts.scad>
    translate([47.5,0,5])
    rotate([90,0,90])
    cell_contacts(1);
    
    
    //elec connections window
    include <elec_contacts.scad>
    translate([-47.5,0,5])
    rotate([90,0,90])
    elec_contacts(1);
    
    
    //quartz plate
    include<quartz_window.scad>
    translate([0,0,37])
    %window(110,100,3);
    
    //metal lide
    include<metal_lid.scad>
    translate([0,0,40])
    rotate([180,0,0])
    metal_lid(110,100,4,1.3);