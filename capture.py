import time
from picamera import PiCamera

def capture_image():
	start = time.time()
	with PiCamera() as camera:
		camera.resolution = (640, 480)
		camera.capture('image.jpg')

	end = time.time()
	print("拍照完成，耗時 {0:.3f} 秒。".format(end - start))

import io
import cv2
import numpy as np

def capture_stream():
	start = time.time()
	stream = io.BytesIO()
	with PiCamera() as camera:
		camera.capture(stream, format='jpeg')

	data = np.fromstring(stream.getvalue(), dtype=np.uint8)
	image = cv2.imdecode(data, 1)
	image = image[:, :, ::-1]
	imgae = np.flipud(np.fliplr(image))

	end = time.time()
	print("拍照完成，耗時 {0:.3f} 秒。".format(end - start))


	from PIL import Image
	img = Image.fromarray(image, 'RGB')
	img.save('test.png')


if __name__ == '__main__':
	capture_stream()
