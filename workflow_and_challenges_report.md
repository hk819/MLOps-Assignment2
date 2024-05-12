# Workflow and Challenges Report

## Project Overview
This project aims to automate the data extraction, transformation, and storage process using Apache Airflow and Data Version Control (DVC). This README.md file provides a comprehensive overview of the project workflow and discusses the challenges encountered during the implementation phase.

## Workflow Overview
1. **Data Extraction:**
   - Employed web scraping methodologies to extract data from various websites.
   - Specifically targeted dawn.com and BBC.com landing pages to extract links, titles, and descriptions.

2. **Data Transformation:**
   - Conducted preprocessing of the extracted data to ensure cleanliness and appropriate formatting.
   - Implemented text normalization techniques to standardize the data structure.

3. **Data Storage and Version Control:**
   - Stored the processed data securely on Google Drive.
   - Incorporated Data Version Control (DVC) to manage and track versions of the data for reproducibility.

## Challenges Faced
- **Technical Setup:** Encountered difficulties in integrating Airflow with DVC.
- **Data Inconsistencies:** Dealt with inconsistencies and formatting issues during the preprocessing stage.
- **Authentication Problems:** Faced authentication challenges while integrating DVC with GitHub.
  
To overcome these hurdles, robust solutions were devised and implemented, ensuring the smooth execution of the data pipeline.
