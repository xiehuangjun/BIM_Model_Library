import pymysql, json, configparser, os, datetime

path = os.path.abspath('.')
cfgpath = path.split('BIM_API')[0] + 'BIM_API/config.ini'

config = configparser.ConfigParser()
config.read(cfgpath)


mysql = pymysql.connect(user = config['MYSQL']["user"], password = config['MYSQL']["password"], port = int(config["MYSQL"]["port"]), host = config['MYSQL']["host"])
cur = mysql.cursor()
cur.execute('''CREATE DATABASE BIM;''')

cur.execute('''CREATE TABLE IF NOT EXISTS BIM.account (
                 User_accountID CHAR(100) NOT NULL PRIMARY KEY, 
                 User_account_name TEXT NOT NULL,
                 User_group TEXT NOT NULL,
                 User_password TEXT NOT NULL,
                 User_createTime DATETIME NOT NULL,
                 User_status TEXT NOT NULL,
                 User_status_change DATETIME NOT NULL)ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;''')
mysql.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS BIM.Object_Information(
    User_accountID VARCHAR(100),
    Object_Name VARCHAR(100),
    Object_ID VARCHAR(100),
    Object_parameter text, 
    Object_json_path VARCHAR(500), 
    Object_json_size VARCHAR(100),
    Object_png_path VARCHAR(500),
    Object_png_size VARCHAR(100),
    Object_gh_path VARCHAR(500),
    Object_gh_size VARCHAR(100),
    Object_3dm_path VARCHAR(500),
    Object_3dm_size VARCHAR(100),
    Project_jpg_path VARCHAR(500),
    Project_jpg_size VARCHAR(100),
    Object_pdf_path VARCHAR(500),
    Object_pdf_size VARCHAR(100),
    Object_version VARCHAR(50),
    Object_update_times VARCHAR(50),
    Object_download_times VARCHAR(50),
    Object_hashcode VARCHAR(150),
    Object_bc_time VARCHAR(1000),
    Object_db_time VARCHAR(1000),
    Object_total_time VARCHAR(1000),
    Object_json_time VARCHAR(1000),
    Object_png_time VARCHAR(1000),
    Object_gh_time VARCHAR(1000),
    Object_3dm_time VARCHAR(1000),
    Project_jpg_time VARCHAR(1000),
    Object_pdf_time VARCHAR(1000),
    Finshed_upload_time VARCHAR(1000),
    Id_co_times VARCHAR(100),
    Id_ch_time VARCHAR(100),
    Id_so_time VARCHAR(100),
    Id_to_time VARCHAR(100),
    Object_ghuser_path VARCHAR(500),
    Object_ghuser_size VARCHAR(100),
    Object_ghuser_time VARCHAR(1000)
    )ENGINE = InnoDB DEFAULT CHARSET = utf8 COLLATE = utf8_unicode_ci;''')

mysql.commit()



cur.close()




