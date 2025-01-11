# PDF Extraction

## Overview
The PDFextraction.ipynb notebook is designed to extract data from PDF files and process it using Python. It provides functionality for selecting folders, querying PDF contents, and leveraging external tools like OpenAI for analysis. The notebook is modular, allowing users to integrate and expand its capabilities for specific PDF extraction and processing tasks.

## Features

1. **PDF Extraction**:

    - Uses libraries like `pdfplumber` and `PyPDF2` to extract text and metadata from PDFs.

2. **File Selection**:

    - Includes a GUI-based file dialog for folder selection using `tkinter`.

3. **OpenAI Integration**:

    - Designed to interact with the OpenAI API for advanced querying and processing of extracted content.

4. **Customizable Variables**:

    - API key, common terms, and folder paths can be easily configured for specific use cases.

## Requirements:

The notebook requires the following Python libraries:

 - `openai`

 - `pdfplumber`

 - `PyPDF2`

 - `tkinter`

 - `pandas`

Ensure that these libraries are installed before running the notebook. Use the command:
```bash
pip install openai pdfplumber PyPDF2 pandas
```
Note: tkinter is typically included with Python installations.

## Usage Functionc

1. **Setup**:

      - Open the notebook in Jupyter Notebook or JupyterLab.

      - Install required libraries if not already installed.

2. **Configuration**:

      - Set your OpenAI API key in the `api_key` variable.

      - Define any common terms for querying in the `common_terms` list.

3. **Run the Notebook**:

      - Execute cells sequentially.

      - When prompted, select the folder containing PDF files using the GUI dialog.

      - The script will process the selected PDFs and perform analysis based on the configured options.

## Key Functions

1. **`get_folder_path()`**

      - Description: Opens a file dialog for selecting a folder.

      - Returns: The file path of the selected folder.

2. **`extract_and_query(pdf_folder, api_key, common_terms)`**

     - Description: Processes the PDFs in the specified folder and performs analysis using OpenAI.

     - Parameters:

        - pdf_folder: Path to the folder containing PDFs.

        - api_key: Your OpenAI API key.

        - common_terms: List of terms to query within the PDFs.

     python PDFextraction.ipynb
     ```


