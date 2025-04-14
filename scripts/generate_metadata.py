import os
import json

current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(current_path)
print(parent_path)

books_dir_path = os.path.join(parent_path,"books")
files = os.listdir(books_dir_path)



university_metadata = {}


for file in files:
    if file.endswith(".pdf"):

        """ Stripping University Name and Data

        E.g. Stored as -- NUST-PROSPECTUS.pdf
        Final Result --   NUST,PROSPECTUS ("-" acts as a delimiter)
        
        """

        fileData = file.split("-")
        universityName = fileData[0] if len(fileData) > 0  else "unknown"
        universityDocType = fileData[1] if len(fileData) > 1 else "unknown"



        metadata = {
            "filename" : file.replace(".pdf",""),
            "type"     : universityDocType,
            "path"     : os.path.join(books_dir_path,file)
        }
        
        if universityName not in university_metadata:
            university_metadata[universityName] = []
        
        university_metadata[universityName].append(metadata)
    


with open("university_metadata.json","w") as file:
    json.dump(university_metadata,file,indent = 4)













