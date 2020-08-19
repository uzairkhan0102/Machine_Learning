from PIL import Image
import os



def max_size():
    path = r'D:\wamp\www\app_recommendation\screenshots'
    height_max, width_max = 0,0
    for dir_name in os.listdir(path):
        for file_name in os.listdir(os.path.join(path,dir_name)):
            try:
                old_im = Image.open(os.path.join(path,dir_name,file_name))
                old_size = old_im.size
                height_max = max(height_max, old_size[1])
                width_max = max(width_max, old_size[0])
            except Exception as e:
                print e
    fd = open('max_size.txt','a')
    fd.write("Height: "+str(height_max)+"\n")
    fd.write("Width: "+str(width_max)+"\n")

if __name__ == '__main__':
    max_size()
