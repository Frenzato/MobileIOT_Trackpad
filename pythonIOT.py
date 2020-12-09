import mouse, sys
import time 
import serial

mouse.FAILSAFE=False
ArduinoSerial=serial.Serial('com8',9600)  
time.sleep(1)                             

while 1:
   data=str(ArduinoSerial.readline().decode('ascii'))
   (x,y,z)=data.split(":")  
   (x,y)=(int(x),int(y))   
   mouse.move(x,y)         
   if '1' in z:                       
      mouse.click(button="left") 
   elif '2' in z:
      mouse.click(button="right")
   elif '3' in z:
      mouse.wheel(delta=-1)      
   elif '4' in z:
      mouse.wheel(delta=1)       
    
     
