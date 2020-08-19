import shutil
import MySQLdb, os, re

#establishing connection with MYSQL
def mysql_connect():
    return MySQLdb.connect("localhost","root","","app_recommendation")

def image_extract():
    counter = 0
    category = raw_input("Enter category: ")
    try:
        os.mkdir(os.path.join("D:\\",category))
    except Exception as e:
        print e
    db = mysql_connect()
    cursor = db.cursor()
    query = 'SELECT path FROM `screenshots` where `docid` IN (SELECT docid FROM `playstore` where `category` Like "'+category+'%")'
    cursor.execute(query)
    for row in cursor.fetchall():
        try:
            a = re.findall('(\d+.jpg)', row[0])
            shutil.copy(row[0], os.path.join("D:\\",category))
            os.rename(os.path.join("D:\\",category,a[0]), os.path.join("D:\\",category,category+"_"+str(counter)+".jpg"))
            counter += 1
        except Exception as e:
            print e
        if counter == 1220:
            break

if __name__ == "__main__" :
    image_extract()
