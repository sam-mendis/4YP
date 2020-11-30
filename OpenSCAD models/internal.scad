//internal layout


module internal(){
    
    include<substrate_holder1.1.scad>
    
    include<substrate-outline.scad>
    translate([0,0,15])
    substrate();
    
    
    include<bracket.scad>
    translate([0,0,17])
    casing(40,40,3,1,2);
    
    
    
    
    
    
    
}

//internal();