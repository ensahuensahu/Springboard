 MovieLens 20M Dataset

**Source**: [MovieLens 20M Dataset](https://grouplens.org/datasets/movielens/20m/)

## Dataset Description

The **MovieLens 20M dataset** contains:
- **20 million user ratings** (from 138,000 users) for **27,000 movies**.
- Includes additional metadata:
  - Movie titles
  - Genres
  - User-generated tags

The dataset is provided in **CSV format** and is commonly used for recommender system research and development.

## Why This Dataset?

- A **benchmark dataset** for building and evaluating **recommendation systems**.
- Rich in **collaborative filtering data** (user-item interactions).
- Includes **metadata** like genres and tags for potential **content-based filtering**.

## Prediction Potential

- **Rating prediction**: Predict how a user will rate a movie.
- **Movie recommendation**: Suggest movies based on a user's past ratings.
- Explore **cold-start problems** (new user or new item scenarios).
- Develop **hybrid recommenders** (collaborative + content-based filtering).

## Data Collection Method

The dataset is downloaded directly from the GroupLens project using the provided **Python script**:  
[`movielens_download.py`](movielens_download.py)

This script:
- Downloads the dataset ZIP file.
- Extracts it to the **CSV format** for further analysis.

---

## File Structure