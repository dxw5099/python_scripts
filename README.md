# python_scripts
```bash
$ python Samplesheet_error_checking_v3.py samplesheet.csv
```
The first argument is to tell what samplesheet to check.  
  

Samplesheet_error_checking_v3.py detects:
  if duplicated row by 'Lane', 'Index', 'Index2' or by 'Index', 'Index2' 
  delete all space
  replace "+" by "-P-"
  replace special charaters by "-" except "_", "-", "+" and " "
  Overwrite input file using corrected file




```bash
$ python Samplesheet_error_checking_v2.py samplesheet.csv
```
The first argument is to tell what samplesheet to check.  
  

Samplesheet_error_checking_v2.py detects:
  if any column is blank, then delete empty columns
  if duplicated row by 'Lane', 'Index', 'Index2' or by 'Index', 'Index2' 
  delete all space
  replace special charaters by "_" except "-" and " "
  Overwrite input file using corrected file



```bash
$ python Samplesheet_error_checking_v1.py samplesheet.csv 2
```
The first argument is to tell what samplesheet to check.  
The second argument is to tell how many projects within in the samplesheet.  

Samplesheet_error_checking_v1.py detects:
  if number of projects == your input
  if duplicated row by 'Lane', 'Index' or by 'Index' 
  delete all space
  replace special charaters by "_" except "-" and " "
  Overwrite input file using corrected file
