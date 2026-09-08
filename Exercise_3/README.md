# Assignment 3 - Workflows and FAIR principles
**Course:** Jenny Laberg Nilsson
**Date:** 8/9/2026
**Description:** 
This exercise is a practice in creating a reproducible workflow. We are supposed to create a repository that contains descriptive text with a general explanation of the project, including instructions and requirements such as dependencies and setup needed to run the project. Documentation of what was done during the project must also be included. The exercise demands the use of an environment; I will use uv and include a `pyproject.toml` file where I pin necessary package versions. In addition, we should work in a notebook where our code and output cells are clearly visible and described.

## Repository structure
```text
├── LICENSE
├── README.md            # Project documentation
├── pyproject.toml       # Dependencies managed via uv
├── data/                # Folder for data storage
└── notebooks/           # Folder for all jupyter notebooks for interactive analysis
 