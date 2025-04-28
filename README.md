# Machine Learning Engineering & AI Capstone Project: Data Collection

This repository contains the **Data Collection step** for my capstone project.

## Datasets Explored

1. **Lending Club Loan Data (Finance)**  
   - Source: [Kaggle Lending Club Dataset](https://www.kaggle.com/datasets/wordsforthewise/lending-club)  
   - Use case: Loan default prediction (credit risk modeling).

2. **Amazon Customer Reviews (NLP)**  
   - Source: [AWS Open Data Registry](https://registry.opendata.aws/amazon-reviews/)  
   - Use case: Sentiment analysis, star rating prediction, fake review detection.

3. **MovieLens 20M Dataset (Recommendation Systems)**  
   - Source: [MovieLens 20M Dataset](https://grouplens.org/datasets/movielens/20m/)  
   - Use case: Movie recommendation systems using collaborative filtering.

## Chosen Dataset

- **Amazon Customer Reviews (Electronics category)** has been selected due to:
  - Rich textual data for advanced **NLP modeling**.
  - Real-world applications in **product insights**, **review quality**, and **sentiment analysis**.

- Data is collected via a **Python script** in [`chosen_dataset/amazon_reviews_download.py`](chosen_dataset/amazon_reviews_download.py).  
- A **sample of 1000 reviews** is provided in [`chosen_dataset/amazon_reviews_sample.csv`](chosen_dataset/amazon_reviews_sample.csv) for quick exploration.

---