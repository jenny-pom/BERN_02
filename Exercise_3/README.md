# Assignment 3 - Workflows and FAIR principles
**Course:** Jenny Laberg Nilsson  
**Date:** 8/9/2026  
**Description:**   
This exercise is a practice in creating a reproducible workflow. We are supposed to create a repository that contains descriptive text with a general explanation of the project, including instructions and requirements such as dependencies and setup needed to run the project. Documentation of what was done during the project must also be included. The exercise demands the use of an environment; I will use uv and include a `pyproject.toml` file where I pin necessary package versions. Each pin should have a risk assesmen that will be justified in the README file. In addition, we should work in a notebook where our code and output cells are clearly visible and described.

## Risk Assessment
The dependencies in this workflow are specified using `Major.Minor` lower bounds without exact patch numbers. Overly strict pinning (e.g., locking to an exact patch like `pandas==2.3.3`) can create unnecessary compatibility barriers for future users, while completely unpinned packages risk breaking the workflow if a major update introduces breaking API changes. By pinning dependencies to the `Major.Minor` version level (e.g., `pandas>=2.3`), the workflow remains flexible enough to absorb bug fixes and security patches while preventing automatic upgrades to incompatible future major releases.   
 
I corrected all dependencies by using uv add:    
```bash
uv add "biopython>=1.88" "ipykernel>=7.3" "matplotlib>=3.10" "pandas>=2.3"
```

## Repository structure
```text
├── LICENSE
├── README.md            # Project documentation
├── pyproject.toml       # Dependencies managed via uv
├── data/                # Folder for data storage
└── notebooks/           # Folder for all jupyter notebooks for interactive analysis