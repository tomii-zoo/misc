from machine import Pin, SPI
import st7789
import time

RESET_PIN = 11 # 11 = SPI TX = XIAO D6
DC_PIN = 12    # 12 = SPI RX = XIAO D9? free?
CS_PIN = 13    # 13 = SPI CSn = XIAO D7
CLK_PIN = 14   # 14 = SPI SCK = XIAO D8
DIN_PIN = 15   # 15 = SPI TX/SDA = MOSI? => XIAO D10?
# lower left corner
# backlight unuse

spi = SPI(1, baudrate=31250000, sck=Pin(CLK_PIN), mosi=Pin(DIN_PIN))
tft = st7789.ST7789(spi, 240, 240,
    reset=Pin(RESET_PIN, Pin.OUT),
    cs=Pin(CS_PIN, Pin.OUT),
    dc=Pin(DC_PIN, Pin.OUT),
    #backlight=Pin(BACKLIGHT_PIN, Pin.OUT),
    rotation=0)
tft.init()

# 描画する
#tft.draw(vector_font, str_md_c,50, 30, st7789.color565(0,0,0), 1.4)
#tft.fill(st7789.color565(128,128,0))
def clear():
    tft.fill(st7789.BLACK) 


while True:
    clear()
    tft.png("friren.png", 0, 0)
    time.sleep(10)
    
    clear()
    tft.png("icon.png", 0, 0)
    time.sleep(10)

    clear()
    tft.png("samus.png", 0, 0)
    time.sleep(10)

# テキストをベクターフォントで描画
#import romand as vector_font
#tft.draw(vector_font, "I'm HOME",20, 100, st7789.color565(255,255,255), 1.4)
