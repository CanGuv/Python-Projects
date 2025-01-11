# Football Scouting Network

## Overview

The `FootballScoutingNetworkSoftware.ipynb` notebook is designed to analyse and visualise football scouting data, utilising advanced data processing and visualisation techniques. This notebook processes a dataset of football players and focuses on extracting insights, such as transfer values and player attributes, to aid in scouting and decision-making. The inspiration for this was the success that Bright Football Club has achieved through its exciting scouting network - to replicate it in a data science project we made sure the players were young and cheap with huge potential - the users are able to view the players in a dashboard.

The data used in this project can be downloaded from here: https://www.kaggle.com/datasets/furkanuluta/football-manager-22-complete-player-dataset?resource=download 

## Features

1. Data Loading and Processing:

    - Reads a CSV file containing football player data.

    - Filters and processes the dataset to include only relevant columns and clean data for analysis.

2. Transfer Value Conversion:

    - Extracts and converts transfer values (in ranges) into numeric data for better analytical use.

3. Data Visualization:

    - Utilises the bokeh library to create interactive visualisations, such as scatter plots with color mappings based on player attributes.

3. Customisable Analysis:

    - Designed to allow users to adapt filtering criteria and visualisations according to specific scouting needs.

## Requirements

The notebook requires the following Python libraries:

  - pandas
  - bokeh

Ensure these libraries are installed using the following command:
```bash
pip install pandas bokeh
```

## Usage Instructions

1. Setup:

    - Place the dataset in the appropriate path (modify the dataset path in the code if needed).

    - Open the notebook in Jupyter Notebook or JupyterLab.

2. Run the Notebook:

    - Execute the cells sequentially.

    - The notebook will load, process, and visualize the data step by step.

3. Data Preparation:

    - The dataset is filtered to exclude irrelevant columns and cleaned for missing or inconsistent values.

4. Visualization:

    - Generates interactive visualisations using bokeh. Users can customise these visualisations by modifying the relevant code sections.

## Key Steps

1. Data Loading

    - Loads the dataset using pandas.

2. Data Cleaning

    - Filters columns and processes the Transfer Value column to extract minimum and maximum values for numeric operations.

3. Visualisation

    - Creates interactive visualisations using bokeh, such as scatter plots with color-coded attributes.
