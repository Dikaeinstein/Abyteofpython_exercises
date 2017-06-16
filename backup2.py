import os
import time
from mywalk import directory
from zipfile import ZipFile

# Files and directories to be backed up
source = ["/storage/sdcard1/python/mit"]

# Main backup directory
target_dir = "/storage/sdcard1/python/Backup"

# The current day is the name of the subdirectory in the main
today = target_dir + os.sep + time.strftime("%Y%m%d")

# Creates subdirectory if it doesn't already exist
if not os.path.exists(today):
    # make directory
    os.mkdir(today)    
    print("Successfully created directory", today)

# The current time is the name of the zip archilve    
now = time.strftime("%H%M%S")

# Take a comment from the user and create the name of the zip file
comment = input("Enter a comment --> ")
if len(comment) == 0:
    target = today + os.sep + now + ".zip"
else:    
    target = today + os.sep + now + "_" + comment.replace(" ", "_") + ".zip"
  
# Create zip archive  
with ZipFile(target, "w") as myzip:
    sources = directory(source[0])
    for f in sources:
        myzip.write(f)
        
