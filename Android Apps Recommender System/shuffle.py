import os
import random
import sys

path = r'D:\BUSINESS'
music_files=[]
 
if len(sys.argv) != 2:
  print "Usage:", path[0], "/path/directory"
else:
  dir_name=path[1]
  if os.path.isdir(dir_name):
    for file_name in os.listdir(dir_name):
      music_files.append(file_name)
  else:
    print "Directory", dir_name, "does not exist"
    sys.exit(1)
# shuffle list
random.shuffle(music_files)
for item in music_files:
  print os.path.join(dir_name,item)
