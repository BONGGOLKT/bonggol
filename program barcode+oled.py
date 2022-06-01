import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

scode="12145678"

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


if scode == scode :
draw.text((x, top),    'SESUAI',  font=font, fill=255)


# Display image.
disp.image(image)
disp.display()