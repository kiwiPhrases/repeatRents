import os, re
import codecs

# set data path
data_path = 'C:/Users/SpiffyApple/Documents/USC/OwnResearch/proposal/PostFolder'
old_path = 'programs_orig'
new_path = 'programs'

# get list of files
fileList = [f for f in os.listdir("/".join([data_path, old_path])) if ".do" in f]

# read in file
file = fileList[2]
txt = codecs.open("/".join([data_path, old_path,file]), 'r', 'cp1257').read()

# set items to change
pathFndr = "([\:\-\w_\\\]+);"
toChange = ['local datapath ', 'local path ']

# set what to change to
pathNew = ["/".join([data_path, 'Data'])+';',data_path+';' ]

# iterate over all files
for f in fileList:
    with open("/".join([data_path, old_path, f]),'r') as file:
        txt = file.read()
    #txt = codecs.open("/".join([data_path, 'Programs',f]), 'rb', 'cp1257').read()
    for i in range(len(toChange)):
        txt = re.sub(toChange[i]+pathFndr, toChange[i] + pathNew[i], txt)
        
    with open("/".join([data_path, new_path,f]),'w+') as f:
        f.write(txt)
      
