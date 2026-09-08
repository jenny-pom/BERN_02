# Assignment 3 - Workflows and FAIR principles
**Course:** Jenny Laberg Nilsson
**Date:** 8/9/2026
**Description:** 
This excersice is a pracetice of how to create a reproducible workflow. 
We are suppose to create a repository that contains descriptive text with a general explination of the project. 
Including instructions and requirments such as dependencies and setups needed to run the project. 
Documentation of what was done during the project must be included. 
The exercise also demands the usage of an envirolment. I will use uv and include pyproject.toml file where I pin necessary versions.
In addition we should work in a nortebook where our code and output cells are clearly visible and described. 

## Repository structure
```text
├── LICENSE
├── README.md            # Project documentation
├── pyproject.toml       # Dependencies managed via uv
├── data/                # Folder for data storage, split into raw and processed data
│   ├── processed_data/
│   └── raw_data/
├── notebooks/           # Folder for all jupyter notebooks for interactive analysis
├── results/             # Folder for results (incase there are any)
└── scripts/             # Folder for .py scripts

## FAIR Principle
the FAIR principle is a process decribing how to make your work reproducible. It is an abrivation that stands for:
F - Findable
A - Accessible
I - Interoperable
R - Reusable
We want to work by FAIR in order to make our research transparent and to reduce barriers for re-usage. A few example inlcude the usage of digit object identifier (DOI), standardised communication protocols, ex. http, documneting clear workflows and having data files that are easy to read and use. We should describe the data through metadata files and use licens to increase accessibility. 