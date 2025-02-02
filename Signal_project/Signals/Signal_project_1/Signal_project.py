from PIL import Image, ImageChops
import numpy as np
#import matplotlib.pyplot as plt
import cv2

w = 1280
h = 2048
w0 = 1024
#all_pixels = w0 * h

def read_raw_image(file, w, h):
    with open(file, 'rb') as f:
        raw_data = f.read()

    pixels = np.frombuffer(raw_data, dtype=np.uint8)
    pixels = pixels.reshape((h, w))
    image_pixels = Image.fromarray(pixels, 'L')

    return image_pixels

file_name_1 = 'C:/Signals/27012025-183000_lines_2048_points_1280.raw'
image_1 = read_raw_image(file_name_1, w, h)
#image_1.show()
image_1.save('image_1_project1.png')

file_name_2 = 'C:/Signals/27012025-183006_lines_2048_points_1280.raw'
image_2 = read_raw_image(file_name_2, w, h)
#image_2.show()
image_2.save('image_2_project1.png')

diff = ImageChops.difference(image_1, image_2)      #разница изображений
diff_array = np.array(diff)     #перевод разницы между изображениями в массив, чтобы отобразить
image_diff = Image.fromarray(diff_array, 'L')       #создание изображения
image_diff.save('image_diff_project1.png')
#image_res.show()


image_diff_to_filter = cv2.imread('image_diff_project1.png', cv2.IMREAD_UNCHANGED)   #прогрузить изображение, чтобы применить функции OpenCV
median_denoise = cv2.medianBlur(image_diff_to_filter, 5)   #изображение очищается медианным фильтром 
cv2.imwrite('image_median_denoise_project1.png', median_denoise)     #сохранение чистенького изображения
image_median_denoise = Image.open('image_median_denoise_project1.png')   #прогрузка конечного изображения, чтобы отобразить
image_median_denoise.show()

'''gauss_denoise = cv2.GaussianBlur(image_diff_to_filter, (5,5),0)
cv2.imwrite('image_gauss_denoise_project1.png', gauss_denoise)
image_gauss_denoise = Image.open('image_gauss_denoise_project1.png')
image_gauss_denoise.show()'''






