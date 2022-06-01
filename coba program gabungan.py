import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from time import sleep
from cv2 import *
cam_port = 0
cam = VideoCapture(cam_port)
import time, datetime
import telepot
from telepot.loop import MessageLoop
now = datetime.datetime.now()
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dummy=""
scode="190576914082"

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0


disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()


disp.clear()
disp.display()


width = disp.width
height = disp.height
image = Image.new('1', (width, height))


draw = ImageDraw.Draw(image)


shape_width = 20
top = padding
bottom = height-padding

x = padding

x += shape_width+padding

x += shape_width+padding

x += shape_width+padding

font = ImageFont.load_default()


if dummy == scode :
    def action(msg):
        chat_id = msg['chat']['id'] #tambahkan chat_id = hid = library barcode atau di
        command = msg['text'] #command juga bisa

        print ('Received:%i' % command)

        if command == '/8998989300261':
            telegram_bot.sendMessage (chat_id, str("Paket terdeteksi"))
        elif command == '/time':
            telegram_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
        elif command == '/file':
            telegram_bot.sendDocument(chat_id, document=open('/home/pi/Desktop/fire_sms.py'))
        elif command == '/picture':
            telegram_bot.sendDocument(chat_id, document=open('/home/pi/Desktop/OpGL/3d-model.png'))

        telegram_bot = telepot.Bot('5159850257:AAE-1vRaKK9uQIGK1oW853FcCVGqmLP_AEY')

    draw.text((x, top),    'SESUAI',  font=font, fill=255)
    disp.image(image)
    disp.display()