import shutil
import MySQLdb, os, re
import urllib
import numpy as np

path = r"D:\alikhan24"

#establishing connection with MYSQL
def mysql_connect():
    return MySQLdb.connect("localhost","root","","recommender")

def image_extract():
    counter = 0
    f = np.loadtxt("app.txt", delimiter=",",dtype='str')
    for i in range(len(f)):
        try:
            db = mysql_connect()
            cursor = db.cursor()
            query = "SELECT path FROM `recommender`.`screenshot` where `docid`='"+f[i]+"'"
            
            if i == 41:
                exit
            cursor.execute(query)
            row = cursor.fetchone()
            row_counter = 0
            while row is not None:
                if row_counter == 2:
                    resource = urllib.urlopen(row[0])
                    output = open(os.path.join(path,str(counter)+".jpg"),"wb+")
                    output.write(resource.read())
                    output.close()
                row_counter += 1
                row = cursor.fetchone()
                if row_counter == 3:
                    break
            counter += 1
        except Exception as e:
            print "Error occured: ",e
        


if __name__ == "__main__" :
    image_extract()
        
