import os
import path
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name="text summerizer"

list_of_files= [
   ".github/workflows/.gitkeep",
   f"src/{project_name}/init.py",
   f"src/{project_name}/components/init.py",
   f"src/{project_name}/utils_init_.py",
   f"src/{project_name}/utils/common.py",
   f"src/{project_name}/logging//init.py",
   f"src/{project_name}/config_init_.py",
   f"src/{project_name}/config/configuration.py",
   f"src/{project_name}/pipeline/configuration.py",
   f"src/{project_name}/entity/init.py",
   f"src/{project_name}/constants/init.py",
   "config/config.yaml",
   "params.yaml",
   "app.py",
   "main.py",
   "Dockerfiles",
   "requirements.txt",
   "setup.py","research/trials.ipynb"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:(filedir) for the file (filename)")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exist")