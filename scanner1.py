from MyQR import myqr
import os
  
version, level, qr_name = myqr.run (
  words="https://www.genio2k22.com/",     

  version=1,               
  level='H',               
  picture="itachi.gif", 
          
  colorized=True,    
  brightness=1.0,            
  save_name="final_v1.gif",     
  save_dir=os.getcwd() 
)
