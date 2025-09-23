import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "ufo_mlops"

list_of_files = [
    # GitHub workflows
    ".github/workflows/.gitkeep",

    # Source code
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/etl/__init__.py",
    f"src/{project_name}/etl/clean_data.py",
    f"src/{project_name}/features/__init__.py",
    f"src/{project_name}/features/build_features.py",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/models/train.py",
    f"src/{project_name}/models/predict.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",

    # Configs
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",

    # Root scripts
    "main.py",
    "Dockerfile",
    "setup.py",

    # Data directories
    "data/raw/.gitkeep",
    "data/interim/.gitkeep",
    "data/processed/.gitkeep",

    # Research notebooks
    "research/eda.ipynb",

    # API & dashboard
    "api/main.py",
    "dashboards/app.py",

    # Templates (for future HTML/Streamlit dashboards)
    "templates/index.html",

    # Tests
    "tests/__init__.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
