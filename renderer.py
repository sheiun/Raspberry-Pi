import picamera
import io
import time
import numpy as np
import cv2

cam = picamera.PiCamera()
ren = picamera.PiRenderer(cam, vflip = True, hflip = True)
stream = io.BytesIO()
cam.capture(stream, format='jpeg', quality=4)
data = np.fromstring(stream.getvalue(), dtype=np.uint8)
image = cv2.imdecode(data, 1)
image = image[:, :, ::-1]

from PIL import Image
img = Image.fromarray(image, 'RGB')
img.save('{}.jpg'.format(time.strftime("%Y%m%d-%H%M%S")))

