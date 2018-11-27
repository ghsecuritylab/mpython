
from machine import Pin, ADC, PWM, I2C,TouchPad,SPI,Timer,UART
from mpython import *
import machine
import time,ubinascii,framebuf,network


# wifi参数 
SSID="yourSSID"            #wifi名称
PASSWORD="yourPASSWORD"         #密码

# 本函数实现wifi连接 
def connectWifi(ssid,passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(ssid,passwd)
  print('connecting to network...')
  
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep_ms(500)
    print('.',end="")
  print('WiFi Connection Successful,Network Config:%s' %str(wlan.ifconfig()))


#connectWifi(SSID,PASSWORD)


logo = bytearray([\
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X07,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X0F,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X1F,0X06,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X3E,0X0E,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X7C,0X1F,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0XF8,0X3E,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X06,0X01,0XF0,0X7C,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X0F,0X03,0XE0,0XF8,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X1F,0X07,0XC1,0XF0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X3E,0X0F,0X83,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X7C,0X1F,0X07,0XC1,0XC0,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0XF8,0X3E,0X0F,0X83,0XC0,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X01,0XF0,0X7C,0X1F,0X07,0XC0,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X03,0XE0,0XF8,0X3E,0X0F,0X80,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X07,0XC0,0XF0,0X7C,0X1F,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X0F,0X81,0XE0,0XF8,0X3E,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X1F,0X01,0XE1,0XF0,0X7C,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X3E,0X01,0XE3,0XE0,0XF8,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X3C,0X01,0XE3,0XC1,0XF0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X78,0X01,0XE1,0X83,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X78,0XC1,0XE0,0X07,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0XF0,0XE0,0XF0,0X0F,0X83,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0XF0,0XE0,0XF8,0X1F,0X07,0X80,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XE7,0XF8,0X7C,0X1E,0X0F,0X80,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XE7,0XFC,0X3E,0X0C,0X1F,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XE7,0XF8,0X1F,0X00,0X3E,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XE0,0XE0,0X0F,0X80,0X7C,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XC0,0XE0,0X07,0XC0,0XF8,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XE0,0XC0,0X03,0XC1,0XF0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XE0,0X00,0X01,0XE3,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X01,0XE0,0X00,0X01,0XE7,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0XE0,0X00,0X00,0XFF,0X80,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0XF0,0XC0,0X18,0XFF,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0XF0,0XF0,0X38,0XFE,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X78,0XFF,0XF8,0XFC,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X7C,0X7F,0XF1,0XF8,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X3E,0X0F,0X81,0XF0,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X1F,0X00,0X07,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X0F,0XC0,0X1F,0XC0,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X07,0XFF,0XFF,0X80,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X03,0XFF,0XFE,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0XFF,0XF8,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X1F,0XE0,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,
])

# analog 
ext   = ADC(Pin(34))
P2   = ADC(Pin(35))
P1   = ADC(Pin(32))
P0   = ADC(Pin(33))

# Pin test

pwm_P8=PWM(Pin(26), freq = 20,duty = 512) 
pwm_P9=PWM(Pin(25), freq = 20,duty = 512)   
pwm_P13=PWM(Pin(18),freq = 20, duty = 512) 
pwm_P16=PWM(Pin(5), freq = 20,duty = 512)   
pwm_P14=PWM(Pin(19),freq = 20, duty = 512)   
pwm_P15=PWM(Pin(21),freq = 20, duty = 512)


# touchPad
touchPad_P = TouchPad(Pin(27))
touchPad_Y = TouchPad(Pin(14))
touchPad_T = TouchPad(Pin(12))
touchPad_H = TouchPad(Pin(13))
touchPad_O = TouchPad(Pin(15))
touchPad_N = TouchPad(Pin(4))

# MAC id
machine_id = ubinascii.hexlify(machine.unique_id()).decode().upper()

def btn_A_irq(_):
  if button_a.value() == 0:
    buzz.on()
  else:
    buzz.pwm.freq(20)
    buzz.off()

def btn_B_irq(_):
  if button_b.value() == 0:
    buzz.on()
  else:
    buzz.pwm.freq(20)
    buzz.off()
    
	
def testoled():
  
  logo_ = framebuf.FrameBuffer(logo,128,64, framebuf.MONO_HLSB)
  #display.invert(1)
  display.blit(logo_,0,0)
  display.show()
  time.sleep_ms(1000)
  display.fill(0)
  time.sleep_ms(200)
  display.fill(1)
  display.show()

          

button_a.irq(btn_A_irq)
button_b.irq(btn_B_irq)


tim1 = Timer(1)

# pixles
color_index = 0
color = ((32, 0, 0), (0, 32, 0), (0, 0, 32))

def Rgb_Neopixel():
  global color_index,color
  for i in range(0, 3):
    rgb[i] = color[color_index]
  rgb.write()
  color_index = color_index + 1
  color_index = color_index % 3
  
  
def Print_Serial_num():
  u = UART(2, baudrate=115200, bits=8, parity=None, stop=1, rx=26, tx=25,timeout=200)
  display.fill(1)
  display.show()
  while True:
    
    if u.readline()=='COM:Give me string'.encode():
      
      time.sleep_ms(10)
      u.write(machine_id[:6]+'\n')
      u.write(machine_id[6:]+'\n\r')
      u.write(machine_id[:6]+'\n')
      u.write(machine_id[6:]+'\n\r')
      
 
 # pixles timer
tim1.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:Rgb_Neopixel()) 

#oled full pixel test
testoled()
time.sleep_ms(1000)
display.fill(0)
display.show()


while True:

  print('P:%d,Y:%d, T:%d, H:%d, O:%d, N:%d' % (touchPad_P.read(),touchPad_Y.read(),touchPad_T.read(),touchPad_H.read(),touchPad_O.read(),touchPad_N.read()))
  print('P0:%d, P1:%d ,P2:%d, P3/ext:%d' % (P0.read(),P1.read(),P2.read(),ext.read()))
  print('light:%d,Sound:%d' % (light.read(),sound.read()))
  print('x = %.2f, y = %0.2f, z = %.2f ' % (accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()))
  display.rect(0,0,128,64,1)
  display.DispChar('声音:%d,光线:%d' % (sound.read(),light.read()), 3, 3)
  display.DispChar('加速度:%.1f,%.1f,%.1f' %(accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()),3,16)
  display.DispChar('id:%s' %machine_id,3,42)
  display.show()
  display.fill(0) 
  if ext.read()==0 and P2.read()==4095:
    Print_Serial_num()
    


















































