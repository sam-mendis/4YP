//Quartz Window model
module window(x, y, z, t_y,s_d,t){
    difference(){
        difference(){
            difference(){
                difference(){
                    cube([x,y,t],center=true);
                    
//screws holes for quartz
 //1
 translate([x/2-6,0,0])
 cylinder(r=s_d/2,h=t+1, center=true);
 }
//2
  translate([-(x/2-6),0,0])
 cylinder(r=s_d/2,h=t+1, center=true);
}
//3
translate([0,(y/2-6),0])
 cylinder(r=s_d/2,h=t+1, center=true);
}
//4
translate([0,-(y/2-6),0])
 cylinder(r=s_d/2,h=t+1, center=true);

}
}
window(110,100,30,30,5,5);