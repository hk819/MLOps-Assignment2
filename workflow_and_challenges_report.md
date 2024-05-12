# Workflow and Challenges Report

## Project Overview:
Our project aims to automate the data extraction, transformation, and storage process using Apache Airflow and Data Version Control (DVC). This report provides an overview of the project workflow and highlights the challenges encountered during implementation.

## Workflow Description:
1. **Data Extraction:**
   - Utilized web scraping techniques to extract data from websites.
   - Extracted links, titles, and descriptions from the landing pages of dawn.com and BBC.com.

2. **Data Transformation:**
   - Preprocessed the extracted data to clean and format it appropriately for further analysis.
   - Implemented text normalization techniques to standardize the data format.

3. **Data Storage and Version Control:**
   - Stored the processed data on Google Drive.
   - Implemented Data Version Control (DVC) to track versions of the data and ensure reproducibility.

## Challenges Encountered:
- Technical issues with setting up Airflow and DVC integration.
- Data inconsistencies and formatting challenges during preprocessing.
- Authentication issues with GitHub integration for DVC.
- Robust solutions were implemented to address these challenges and ensure the successful execution of the data pipeline.
