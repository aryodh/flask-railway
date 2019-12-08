import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import subprocess
import time # Import the sleep function from the time module


LedPin = 20 
ServoPin = 4 
IRPin = 17
#IR2Pin = 
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ServoPin,  GPIO.OUT)
GPIO.setup(IRPin, GPIO.IN)
#GPIO.setup(IR2Pin, GPIO.IN)

p = GPIO.PWM(ServoPin, 50) # GPIO 17 for PWM with 50Hz
#p.start(3.5) # Initialization
act = None

def main():
  act = p.start(3.5)
  print("zxc")  
  gateIsClose = False
  while True:
  # dapet 1 dari infrared
    if GPIO.input(IRPin) == False and not gateIsClose:
      onLED()
      gateIsClose = closeGate(gateIsClose)
    
    elif GPIO.input(IRPin) == True and gateIsClose:
      offLED()
      gateIsClose = openGate(gateIsClose)
      
    #elif IO.input(IR2Pin) == True and gateIsClose:
      #offLED()
      #openGate()

def onLED():
  #subprocess.call(['./onLED.sh'])
  GPIO.output(LedPin, GPIO.HIGH)

def offLED():
  #subprocess.call(['./offLED.sh'])
  GPIO.output(LedPin, GPIO.LOW)

def closeGate(gateIsClose):
  if gateIsClose == True:
    return gateIsClose

  try:
    if act == None:
      p.start(3.5)
    p.ChangeDutyCycle(6)
    time.sleep(0.5)
    p.ChangeDutyCycle(8.5)
    print("bisa nutup")
    
  except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

  gateIsClose = True
  return gateIsClose

def openGate(gateIsClose):
  if gateIsClose == False:
    return gateIsClose

  try:
    if act == None:
      p.start(3.5) 
    p.start(3.5)
    p.ChangeDutyCycle(6)
    time.sleep(0.5)
    p.ChangeDutyCycle(3.5)
    
  except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

  gateIsClose = False
  return gateIsClose

if __name__ == '__main__':
  main()
  
