    module attempt1()
    {
        color("red")
        linear_extrude(height = 1.1, center = true, convexity = 1)
        import (file = "transistor_adapter.dxf");
        
   
        }
        //attempt1();
        
            module attempt2()
    {
        color("red")
        linear_extrude(height = 1.1, center = true, convexity = 1)
        import (file  = "single_cell_full_layout.dxf");
        
   
        }
        //translate([0,0,5])
        //attempt2();
        
                
            module attempt3()
    {
        color("blue")
        linear_extrude(height = 1.1, center = true, convexity = 1)
        import (file  = "single_cell_full_layout-2.dxf");
        
   
        }
        
          translate([0,0,10])
        attempt3();
               
        
        module attempt4()
    {
        color("blue")
        linear_extrude(height = 1.1, center = true, convexity = 1)
        import (file  = "layout.dxf");
        
   
        }
        
          //translate([0,0,15])
        //attempt4();
        
        
         module attempt5()
    {
       
        linear_extrude(height = 1.1, center = true, convexity = 1)
        import (file  = "substrate-layout.dxf");
        
   
        }
        
          translate([0,0,30])
        attempt5();
        