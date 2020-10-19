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
 translate([10,0,-5])
 Substrate_holder(40,40,30);

 // outer shell
 include <outer_shell.scad>
outer_shell(110,100,70,30,30,20,5,10,1);

//substrate layout
include <substratelayout.scad>
translate([-5,-15,10])
{
    substratelayout();
    }
    
    //cell connections window
    include <cell_contacts.scad>
    translate([48,0,5])
    rotate([90,0,90])
    cell_contacts(1);
    
    //cell connections window
    include <elec_contacts.scad>
    translate([-48,0,5])
    rotate([90,0,90])
    elec_contacts(1);