#######################################################
######Sanmple_sheet_Error_Checking
######Author: Di Wu


#!/usr/bin/python3
import csv
import pandas as pd
import os
import sys
search_phrase = "[Data]"
row_num = 0
with open(sys.argv[1]) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    data = list(readCSV)
    total_row = len(data)
with open(sys.argv[1]) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        row_num += 1
        if search_phrase in row[0]:
            #print(row_num)
            break
if row_num == total_row:
    print("Please check if you have '[Data]' row right above 'Lane, Sample_ID, Sample_Name, Index, Project ...'!")
    print("No blank cells are allowed to the left of '[Data]'! ")
        #break
else:
     # print row_num
    df_header = pd.read_csv(sys.argv[1], header=None, nrows=row_num)  # read the first row_count rows as header_file
        # print(df_header)
    df_data = pd.read_csv(sys.argv[1], skiprows=row_num)  # skip the first row_count rows (i.e. header lines)
        # print(df_data)
     # remove column if blank
     # if Lane is blank, it will be deleted from the dataframe and then no Lane column
    df_data.dropna(how='all', axis=1)
    df = df_data.replace({' ': '', '[^a-zA-Z0-9_-]': '_'}, regex=True) # same as previous two lines
    df.columns = df.columns.str.replace(' ', '', regex=True) #delete space from column names
    df.columns = df.columns.str.replace('[^a-zA-Z0-9_-]', '_', regex=True)  # replace wierd symbols from columne names

if 'Lane' in df:
    if 'Index2' in df:
        duplicateRowsDF = df[df.duplicated(['Lane', 'Index', 'Index2'], False)]
        if duplicateRowsDF.shape[0] > 0:
            print("Duplicate barcode detected! Please modify duplicated barcodes! ")
            #print(duplicateRowsDF)
            #print(duplicateRowsDF[['Lane',"Index"]].to_string(index=False))
            print(duplicateRowsDF.to_string(index=False))
        else:
            df_header.to_csv("header.csv", index=False, header=False)
            df.to_csv("fixed.csv", index=False)
            os.system("cat header.csv fixed.csv > %s" % sys.argv[1])
            os.system("rm header.csv fixed.csv")
            print("Samplesheet looks good. Please download and use %s for demultiplexing!" % sys.argv[1])
    else:
        duplicateRowsDF = df[df.duplicated(['Lane', 'Index'], False)]
        if duplicateRowsDF.shape[0] > 0:
            print("Duplicate barcode detected! Please modify duplicated barcodes! ")
            # print(duplicateRowsDF)
            # print(duplicateRowsDF[['Lane',"Index"]].to_string(index=False))
            print(duplicateRowsDF.to_string(index=False))
        else:
            df_header.to_csv("header.csv", index=False, header=False)
            df.to_csv("fixed.csv", index=False)
            os.system("cat header.csv fixed.csv > %s" % sys.argv[1])
            os.system("rm header.csv fixed.csv")
            print("Samplesheet looks good. Please download and use %s for demultiplexing!" % sys.argv[1])
else:
    if 'Index2' in df:
        duplicateRowsDF = df[df.duplicated(['Index', 'Index2'], False)]
        if duplicateRowsDF.shape[0] > 0:
            print("Duplicate barcode detected! Please modify duplicated barcodes! ")
            # print(duplicateRowsDF)
            # print(duplicateRowsDF[['Lane',"Index"]].to_string(index=False))
            print(duplicateRowsDF.to_string(index=False))
        else:
            df_header.to_csv("header.csv", index=False, header=False)
            df.to_csv("fixed.csv", index=False)
            os.system("cat header.csv fixed.csv > %s" % sys.argv[1])
            os.system("rm header.csv fixed.csv")
            print("Samplesheet looks good. Please download and use %s for demultiplexing!" % sys.argv[1])
    else:
        duplicateRowsDF = df[df.duplicated(['Index'], False)]
        if duplicateRowsDF.shape[0] > 0:
            print("Duplicate barcode detected! Please modify duplicated barcodes!")
            print(duplicateRowsDF.to_string(index=False))
        else:
            df_header.to_csv("header.csv", index=False, header=False)
            df.to_csv("fixed.csv", index=False)
            os.system("cat header.csv fixed.csv > %s" % sys.argv[1])
            os.system("rm header.csv fixed.csv")
            print("Samplesheet looks good. Please download and use %s for demultiplexing!" % sys.argv[1])

