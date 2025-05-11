import os
from pathlib import Path
import logging

# logging.basicConfig(
#     level=logging.info,
#     format='%(asctime)s %(message)s'
# )
project_name="datascienceproject"

list_of_files=[
 ".github/workflows/.gitkeep",
 f"src/{project_name}/__init__.py",
 f"src/{project_name}/components/__init__.py",
 f"src/{project_name}/utils/__init__.py",
 f"src/{project_name}/utils/common.py",
 f"src/{project_name}/config/configuration.py",
 f"src/{project_name}/pipeline/__init__.py",
 f"src/{project_name}/entity/__init__.py",
 f"src/{project_name}/entity/config_entity.py",
 f"src/{project_name}/constants/__init__.py",
 "config/config.yaml",
 "params.yaml",
 "schema.yaml",
 "main.yaml",
 "dockerfile",
 "setup.py",
 "research/research.ipynb",
 "templates/index.html"


]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename= os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        # logging.info(f"creating dir {filedir} for the file name {filename}")
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            # logging.info(f"Creating empty file: {filepath}")

    else:
            # logging.info(f"Already exists: {filename}")
        pass