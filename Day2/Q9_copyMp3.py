#9. program to copy a .mp3 audio file to another file.

import shutil

sfname=input("Enter the source file name: ")

if sfname.endswith('.mp3'):
    dfname=input("Enter the destination file name: ")
    with open(sfname) as f:
        with open(dfname,'w') as f1:
            shutil.copy(sfname,dfname)      #copies directly from one file to another
else:
    print("Not an mp3 file")
        
