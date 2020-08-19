import re
import MySQLdb
import os
import urllib
uma123 = 0
#give the path of directory in which required files are place
path = r"C:\Users\Uzair Khan\Desktop\Meta-Data_1"

#path of screenshots
path2 = r"D:\wamp\www\app_recommendation\screenshots"

#connecting with the database
db = MySQLdb.connect("localhost","root","","app_recommendation")

#reading the name of each file in the specifed dirtectory
for filename in os.listdir(path):
    try:
        a = 0
        #reading the file line by line
        file_open = open(os.path.join(path,filename),"r")
        line = file_open.readline()
        while line:
            
            #searching in a file
            if re.search("^[\s]*\"docid\":", line) and a ==0:
                a = re.findall("^[\s]*\"docid\":\"(.*)\"",line)
                counter = 0
                try:
                    
                    #crearting the directory
                    os.makedirs(os.path.join(path2,a[0]))
                except Exception as e:
                    print "\nError: Folder already exits:",os.path.join(path2,a[0]),e
                    
            elif re.search("^[\s]*\"image_url\":", line):
                b = re.findall("^[\s]*\"image_url\":\"(.+)\"", line)
                if not os.path.isfile(os.path.join(path2,a[0],str(counter)+".jpg")):
                    #print os.path.isfile(os.path.join(path2,a[0],str(counter)+".jpg"))
                    resource = urllib.urlopen(b[0])
                    output = open(os.path.join(path2,a[0],str(counter)+".jpg"),"wb+")
                    output.write(resource.read())
                    output.close()
                else:
                    print "\nFile exits:",os.path.join(path2,a[0],str(counter)+".jpg")
                    
                if db:
                    try:
                        cursor = db.cursor()
                        p = os.path.join(path2,a[0],str(counter)+".jpg")
                        counter = counter +1
                        q = "INSERT INTO `app_recommendation`.`screenshots`(`docid`, `path`) VALUES (%s,%s)"
                        cursor.execute(q,(a[0],p))
                        db.commit()
                    except Exception as e:
                        print "\nException",a[0],p,e
                else:
                    print "\nError: Connection not established."
            line = file_open.readline()
    except Exception as e:
        print e
        uma123 = 0
file_open.close()
db.close()
