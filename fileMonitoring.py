import re
import sys
import time

while True:
    with open("file1.txt", "r") as logfile1,open("file2.txt", "r+") as logfile2:
        countCDSfile1 = sum(len(re.findall("CDS", word, re.M|re.I)) for word in logfile1)
        countCDSfile2 = sum(len(re.findall("CDS", word, re.M|re.I)) for word in logfile2)
        log = open("search_results.log", "a")
        sys.stdout = log
        print("file1.txt - {}".format(countCDSfile1),end = " ")
        print("file2.txt - {}".format(countCDSfile2),end = "\n")
        time.sleep(8)



