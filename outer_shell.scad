//Outer Shell
//x = length in x
//y = length in y
//z = length in z
//t_x = thickness x
//t_y = thickness y
//t_z = thickness z
//s_d= screw diameter
//s_l= screw length
//or_rad= o-ring rad

module outer_shell(x, y, z, t_x, t_y, t_z,s_d,s_l,or_rad)
 {
    
     window_l= x-t_x;
     window_w= y-t_y;
    
     //difference(){
     
     difference(){
     difference(){
     difference(){
     difference(){
     difference(){ 
     difference(){
     difference(){
     difference(){
        difference(){
            difference(){
                difference(){
                    difference(){
                        difference(){
                        cube([x,y,z], center=true);
                        rotate([90,0,0])
                        translate([x/4,0,0])   
                        cylinder(r=5,h=(y+1), center=true);}
                    rotate([90,0,0])
                    translate([-x/4,0,0])    
                    cylinder(r=5,h=(y+1), center=true);}
    
                 translate([0,0,t_z])
                 {cube ([window_l,window_w,z], center=true);} }
    
    //electronics windows
    
                    rotate([0,90,0])
                    translate([-5,0,0])    
                    cylinder(r=19,h=(x+1), center=true);}

 //release valve hole
 //rotate([90,0,0])
 //{translate([0,z/5,y/3])
 //cylinder(r=2.5,h=((y/2)+1), center=true);}
 //}
 //screws holes for quartz
 //1
 translate([x/2-6,0,z/2])
 cylinder(r=s_d/2,h=s_l, center=true);
 }
//2
  translate([-(x/2-6),0,z/2])
 cylinder(r=s_d/2,h=s_l, center=true);
}
//3
translate([0,(y/2-6),z/2])
 cylinder(r=s_d/2,h=s_l, center=true);
}
//4
translate([0,-(y/2-6),z/2])
 cylinder(r=s_d/2,h=s_l, center=true);

}
//slot for substrate holder
translate([10,0,0])
cube([40,40,34], center=true);

}
 //o ring holder
    rotate([90,0,0])
    translate([x/2-11,z/2,0])   
    cylinder(r=or_rad,h=(y-20), center=true);
}                  

    rotate([90,0,0])
    translate([-(x/2-11),z/2,0])   
    cylinder(r=or_rad,h=(y-20), center=true);
}   
 
rotate([0,90,0])
    translate([-z/2,y/2-11,0])   
    cylinder(r=or_rad,h=(y-10), center=true);
}
rotate([0,90,0])
    translate([-z/2,-(y/2-11),0])   
    cylinder(r=or_rad,h=(y-10), center=true);

 }
 
 
 }
 //outer_shell(110,100,70,30,30,20,4,20,1.3);
 
