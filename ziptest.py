import cwd
from zipfile import ZipFile

with ZipFile("test.zip", "r") as myzip:
    myzip.printdir()
    
