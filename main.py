# Python-код для поиска координат ВОТ ЭТОТ СЛАЙД ЮЗАЙ
# контуры, обнаруженные на изображении.
import numpy as np
import cv2 as cv
import os
import sys
import rotate_photo


# Чтение изображения

# font = cv.FONT_HERSHEY_COMPLEX
def cropp_leg_with_cut_image (color_dir, b_w_dir, rotate=None):

    # получаем список файлов в папке
    if rotate == 1:
        rotate_photo.rotate(color_dir+'/')

    list_images = os.listdir(color_dir)
    # переменная и преобразование в серую шкалу.
    for item in list_images:

        img = cv.imread(b_w_dir+'/'+item, cv.IMREAD_GRAYSCALE)

        # Преобразование изображения в двоичное изображение
        # (только черно-белое изображение).
        _, threshold = cv.threshold(img, 110, 255, cv.THRESH_BINARY)

        # Обнаружение контуров в изображении.
        contours, _ = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        img2 = cv.imread(color_dir+'/'+item, cv.IMREAD_COLOR)

        # (1) Crop the bounding rect

        rect = cv.boundingRect(contours[0])
        x, y, w, h = rect
        croped = img2[y:y + h, x:x + w].copy()

        # (2) make mask
        pts = contours[0]
        pts = pts - pts.min(axis=0)
        mask = np.zeros(croped.shape[:2], np.uint8)
        cv.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv.LINE_AA)

        # (3) do bit-op

        dst = cv.bitwise_and(img, croped, mask=mask)

        # (4) add the white background

        bg = np.ones_like(croped, np.uint8) * 255
        cv.bitwise_not(bg, bg, mask=mask)
        dst2 = bg + dst
        if not os.path.exists(color_dir+"_new"):
            os.makedirs(color_dir+'_new')
        # dst_new = cv.resize(dst2,dst2,interpolation=cv.NORM_HAMMING)

        cv.imwrite(color_dir+'_new/'+item, dst)


if __name__ == "__main__":
    params=[ ]
    for param in sys.argv:
        params.append(param)
    if len(params)<3:
        print("Перед началом работы папки с фотографиями необходимо закинуть в папку с проектом\n" +
              "Введите два или три параметра: \n" +
              "Первый паарметр путь до цветных фотографий \n" +
              "Второй параметр путь до черно-белых фотографий \n" +
              "Третий параметр 1: \n 1 - повернуть все фотографии в 1 папке \n" +
              "Пример: main.py название_папки/название_папки_с_цветными_фотографиями название_папки/название_папки_с_черно-белыми_фотографиями\n" +
              "Если после работы программы вы понимаете, что вырезалось некорректно, то скорее всего нужно повернуть фотографии в одной из папок для это нужно\n"+
              "добавить после первых 2 аргументов 1, пример:"+
              "main.py название_папки/название_папки_с_цветными_фотографиями название_папки/название_папки_с_черно-белыми_фотографиями 1\n")
    elif len(params) == 3:
        cropp_leg_with_cut_image(params[1], params[2])
    elif len(params) == 4:
        cropp_leg_with_cut_image(params[1], params[2], params[3])


