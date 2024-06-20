import sys
import os
import markdown

# validator
if(len(sys.argv) != 4):
    print('Incorrext number of argument. Type markdown, inputfile and outputfile')
    sys.exit()

function = sys.argv[1]
inputfile = sys.argv[2]
outputfile = sys.argv[3]

if(function != 'markdown'):
    print(function + ' is invalid function. Please type markdown to run the code')
    sys.exit()

if not (os.path.exists(inputfile)):
    print(inputfile + ' does not exsists. Type valid file path')
    sys.exit()

# function
with open(inputfile) as f:
    html= markdown.markdown(f.read())
with open(outputfile, 'w') as f:
    f.write(html)
print(inputfile + ' is sucessfully converted to html file')