import numpy as np
import pandas as pd
import os 
import glob
import sys
import ntpath
from subprocess import call

def cutter(filePath):
    fileList = [filePath]
    allRows = []
    for file in fileList:
        pdf = pd.read_csv(file, header=None)
        rows = list(pdf.itertuples(index=False, name=None))
        allRows.extend(rows)
    for i in range (len(allRows)):
        fullFileName = str(allRows[i][0])
        ss = allRows[i][1].replace(" ", "")
        to = str(allRows[i][2]).replace(" ", "")
        fileName, fileExt = os.path.splitext(ntpath.basename(fullFileName))
        call(["ffmpeg", "-y", "-ss", ss, "-t", to,"-i", fullFileName, fileName + '-' + str(i)+"-"+ss.replace(":","_")+"-"+str(to)+fileExt])

cutter("C:/Users/psundareson/TOOLS/cutterinput.txt")  