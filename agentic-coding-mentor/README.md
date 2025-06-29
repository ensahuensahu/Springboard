# Step 5: Data Wrangling - Agentic Coding Mentor

This step involves cleaning the dataset, handling missing values and outliers, and preparing the data for analysis in the Agentic Coding Mentor capstone project.

## Key Steps

- **Data Inspection:** Loaded and inspected raw data for missing values and structure.
- **Cleaning:**
  - Removed rows with missing or empty code fields.
  - Trimmed whitespace from code strings.
  - Removed duplicate rows.
- **Outlier Handling:** 
  - Calculated code length.
  - Removed examples with unusually long code (>1000 tokens).
- **Subsampling:** Sampled 10,000 rows for efficient prototyping if the dataset is large.
- **Optional EDA:** Visualized error type distributions to guide downstream modeling decisions.

## Folder Structure

```
agentic-coding-mentor/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── 05_data_wrangling.ipynb
└── README.md
```
