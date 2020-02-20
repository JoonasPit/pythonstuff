import os
from pathlib import Path
import logging
from datetime import datetime
import io
from pathlib import Path
import snowflake.connector as snow


date = datetime.now()
date_string = date.strftime("%d-%m-%Y-%H:%M:%S")
print(date_string)
filename = "log_" + date_string + ".log"
output_path = "C:\snowflake_testing\outfile2.txt"
path_as_string = "C:\snowflake_testing\snowflake_config.txt"

_file = Path(path_as_string)
log_file = "C:\snowflake_testing\pyrunlog.log"
logging.basicConfig()


f = open(password_file, "r")
lines = f.readlines()
file_username = lines[0]
file_password = lines[1]
print(file_username)
print(file_password)

con = snow.connect(

    user = "",
    password = "",
   # password = str(password),
    account = ""
)
snowflake_query= "use ROLE SYSADMIN;USE SNOWFLAKE;SELECT * FROM ACCOUNT_USAGE.QUERY_HISTORYWHERE ERROR_CODE IS NOT NULL;"
use_role ="USE ROLE SYSADMIN"
use_admindb = "USE SNOWFLAKE"
snow_quer="SELECT * FROM ACCOUNT_USAGE.QUERY_HISTORY WHERE ERROR_CODE IS NULL"
cur = con.cursor()
cur.execute(use_admindb)
cur.execute(snow_quer)
one_row = cur.fetchall()
print(one_row)

with io.open(output_path,"w", encoding= "utf-8") as f2:
    f2.write(str(one_row))

#print(one_row, file=open(output_path,"a"))
con.close()



