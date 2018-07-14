import time
from picamera import PiCamera
from argparse import ArgumentParser

def args_parser(parser):
	parser.add_argument("start", help="開始的 FLAG", type=int)
	parser.add_argument("end", help="結束的 FLAG", type=int)
	args = parser.parse_args()
	return args

def take_off():
	# 起飛
	pass

def landing():
	# 降落
	pass

def follow_line(color):
	pass

def capture_image(camera):
	start = time.time()
	camera.resolution = (640, 480)
	camera.capture('image.jpg')

	end = time.time()
	print("拍照完成，耗時 {0:.3f} 秒。".format(end - start))

import io
import cv2
import numpy as np

def capture_stream(camera):
	start = time.time()
	stream = io.BytesIO()
	camera.capture(stream, format='jpeg', quality=5)

	data = np.fromstring(stream.getvalue(), dtype=np.uint8)
	image = cv2.imdecode(data, 1)
	image = image[:, :, ::-1]
	image = np.flipud(np.fliplr(image))

	end = time.time()
	print("拍照完成，耗時 {0:.3f} 秒。".format(end - start))


	from PIL import Image
	img = Image.fromarray(image, 'RGB')
	img.save('{}.jpg'.format(time.strftime("%Y%m%d-%H%M%S")))


if __name__ == '__main__':
	parser = ArgumentParser()
	args = args_parser(parser)

	FLAG = args.start
	FLAG_END = args.end

	camera = PiCamera()
	camera.start_preview()
	capture_stream(camera)
	camera.stop_preview()
	# camera.close()

	# FLAG = 0
	# (起飛) 沿著黑線 直到 辨識燈號 (紅/綠)

	# 辨識綠燈 FLAG 0 -> 1

	# FLAG = 1
	# 沿著黑線 直到 轉彎

	# 轉彎 FLAG 1 -> 2

	# FLAG = 2
	# 沿著黑色辨識白色 停下計算距離 (準備投擲沙包)

	# 計算距離 往前飛行 (修正/不修正?)
	# 投擲沙包 FLAG 2 -> 3

	# FLAG = 3 同 FLAG 1
	# 沿著黑線 直到 轉彎

	# 轉彎 FLAG 3 -> 4

	# FLAG = 4
	# 沿著黑線 直到 偵測不到黑線 停下

	# 偵測不到黑線 停下 FLAG 4 -> 5

	# FLAG = 5
	# 辨識牆壁 左右

	# 辨識成功 往 左或右移動 FLAG 5 -> 6

	# FLAG = 6
	# 向前走 直到 看到黑線 沿著黑線 直到 黑線消失

	# 辨識不到黑線 降落 FLAG 6 -> 7
