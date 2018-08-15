from sense_hat import SenseHat
from PIL import Image
import sys

hat = SenseHat()


def display_pixels(start_x, start_y):
    for x in range(8):
        for y in range(8):
            hat.set_pixel(x, y, pix[start_x + x, start_y + y])    

img = Image.open('/home/pi/Desktop/{}.jpg'.format(sys.argv[1])).convert('RGB')
w, h = img.size
if min(w, h) > 64:
    scale = max(w // 64, h // 64)
    print(scale)
    print(img.size)
    img = img.resize((w//scale, h//scale))
    w, h = img.size
pix = img.load()
curr_x, curr_y = 0, 0
display_pixels(0,0)
while True:
    event = hat.stick.wait_for_event()
    if event.action != 'released':
        if event.direction == 'right':
            curr_x = min(w - 8, curr_x + 1)
        elif event.direction == 'left':
            curr_x = max(0, curr_x - 1)
        elif event.direction == 'down':
            curr_y = min(h - 8, curr_y + 1)
        elif event.direction == 'up':
            curr_y = max(0, curr_y - 1)
        else:
            hat.clear()
            sys.exit(0)
        display_pixels(curr_x, curr_y)

        
