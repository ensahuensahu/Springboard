# Amazon Customer Reviews (Electronics Category)

**Source**: [AWS Open Data Registry - Amazon Reviews](https://registry.opendata.aws/amazon-reviews/)

## Dataset Description

This dataset contains millions of **customer reviews** from the **Electronics category** on Amazon, including:
- Review text (`review_body`)
- Star ratings (`star_rating`)
- Product metadata (product titles, IDs, categories)

The dataset is provided in **TSV (Tab-Separated Values)** format and includes rich textual data for Natural Language Processing (NLP) tasks.

## Why This Dataset?

- **Rich textual data** allows the exploration of advanced NLP models.
- Provides both **unstructured text** (reviews) and **structured labels** (ratings, categories).
- Real-world dataset for analyzing **customer sentiment**, **product feedback**, and **rating prediction**.

## Prediction Potential

- **Sentiment analysis**: Classify reviews as positive, negative, or neutral.
- **Star rating prediction**: Predict numeric ratings based on review text.
- **Fake review detection**: Identify potentially fraudulent or biased reviews.
- **Topic modeling**: Discover common themes across products or reviews.

## Data Collection Method

The dataset is downloaded from AWS Open Data using the provided **Python script**:  
[`amazon_reviews_download.py`](amazon_reviews_download.py)

This script:
- Downloads the **Electronics category subset** in compressed `.tsv.gz` format.
- Extracts it to a usable **TSV file**.

---

## File Structure
