from PIL import Image
import re
import os
path = r'C:\Users\Uzair Khan\vgg16-pretrained-master\data2\validation\GAME_Action'

for file_name in os.listdir(path):
    try:
        old_im = Image.open(os.path.join(path,file_name))
        old_size = old_im.size

        new_size = (512, 512)
        new_im = Image.new("RGB", new_size)   # luckily, this is already black!
        new_im.paste(old_im, ((new_size[0]-old_size[0])/2, (new_size[1]-old_size[1])/2))

        new_im.save(os.path.join(path,file_name))

    except Exception as e:
        print "/error",e
