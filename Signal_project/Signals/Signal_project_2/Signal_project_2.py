from PIL import Image, ImageChops
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
import cv2

def read_raw_bits(file, w, h, ch):
    with open(file, 'rb') as f:
        raw_data = f.read()

    all_pixels = w * h
    pixels = []
    for i in range(0, len(raw_data), ch):
        pixel = tuple(raw_data[i:i+ch])
        pixels.append(pixel)
    pixels = pixels[:all_pixels]
    pixels = np.array(pixels)
 
    return pixels

w = 1024
h = 2048
ch = 1
#all_pixels = w * h

file_name_1 = 'Signal_project/Signals/Signal_project_2/27012025-183000_lines_2048_points_1280.raw'
pixels_1 = read_raw_bits(file_name_1, w, h, ch)
pixels_1 = pixels_1.reshape((h, w))
image_1 = Image.fromarray(pixels_1, 'L')
image_1.save('image_1_project2.png')

file_name_2 = 'Signal_project/Signals/Signal_project_2/27012025-183006_lines_2048_points_1280.raw'
pixels_2 = read_raw_bits(file_name_2, w, h, ch)
pixels_2 = pixels_2.reshape((h, w))
image_2 = Image.fromarray(pixels_2, 'L')
image_2.save('image_2_project2.png')

diff_pixels = abs(pixels_2 - pixels_1)
diff_pixels = diff_pixels.reshape((h, w))
image_diff_pixels = Image.fromarray(diff_pixels, 'L')
image_diff_pixels.save('image_diff_pixels_project2.png')


image_diff_pixels_to_filter = cv2.imread('image_diff_pixels_project2.png', cv2.IMREAD_UNCHANGED)   #прогрузить изображение, чтобы применить функции OpenCV
median_denoise = cv2.medianBlur(image_diff_pixels_to_filter, 5)   #изображение очищается медианным фильтром 
cv2.imwrite('image_median_denoise_project2.png', median_denoise)     #сохранение чистенького изображения
image_median_denoise = Image.open('image_median_denoise_project2.png')   #прогрузка конечного изображения, чтобы отобразить
image_median_denoise.show()

