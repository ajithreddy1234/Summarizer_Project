import os
from pathlib import Path
import logging 
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')
project_name = "Summarizer"
list_of_files = [
    ".github/workflows/.gitkeep"
    f"src/summarizer/__init__.py",
    f"src/summarizer/components/__init__.py",
    f"src/summarizer/utils/__init__.py",
    f"src/summarizer/utils/common.py",
    f"src/summarizer/logging//__init__.py",
    f"src/summarizer/config/__init__.py",
    f"src/summarizer/config/configuration.py",
    f"src/summarizer/pipeline/__init__.py",
    f"src/summarizer/entity/__init__.py",
    f"src/summarizer/constat/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating file: {filename} at {filedir}")
    else:
        logging.info(f"File already exists: {filename} at {filedir}")
