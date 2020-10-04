import os 
import yaml
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

### Login in ###
cred = credentials.Certificate(r"cred.json")      # Add credential downloaded from firestore
firebase_admin.initialize_app(cred,{"databaseURL":"https://apollo-bb64b.firebaseio.com/user/Tutorial/"})  # Point to credentials and page 

### Setting Database References ###
db_ref_1 = db.reference("user/Tutorial")  # Create a pointer inside database


## Get Values ##
data = db_ref_1.get()  # Get value of Reference 3
print("Succesful Transaction!")


path = os.getcwd()                # Get current path
parent = Path(path).parent        # Get parent node
os.chdir(parent)                  # Change to parent node
os.chdir("docs")                  # Change to docs
title = data["title"].rstrip()    # get the title ands strip /n
title2 = title.replace(" ","_")   # Change the spaces for underscore
text =  data["text"]              # Get  text

### Write file ###
with open(title2 + ".md","wb") as handler:  # Create md file
    title = "# " + title                    # Set title to md title
    handler.write(title.encode("UTF-8"))    # Write title tothe md file
    handler.write("\n".encode("UTF-8"))     # Write space
    handler.write("\n".encode("UTF-8"))     # Write space
    handler.write(text.encode("UTF-8"))     # Write text

os.chdir(parent)                            # Go pack to parent directory
with open("mkdocs.yml","r") as handler:                                 # Open yml file in wirte mode
    cur_yaml = yaml.safe_load(handler)                                  # Safe Load information
    # cur_yaml["nav"][1].keys()                                         # Verify  Keys
    cur_yaml["nav"][1]["Tutorials"].append( {title2: title2 + ".md"})   # Upload md to yml

if cur_yaml:                                                            # if file exists
    with open("mkdocs.yml",'w') as handler:                             # open it again in write mode
        yaml.safe_dump(cur_yaml, handler)                               # Safe dump     

os.chdir(path)

print("Succesful Interaction!")