from PIL import Image
import os
def rotate (dir_photos):
    tmp = os.listdir(dir_photos)
    for item in tmp:
        im = Image.open(dir_photos + item   )
        os.remove(dir_photos + item )
        im.transpose(Image.ROTATE_270).save(dir_photos+item)

