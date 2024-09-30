# Prodigy-Task-4

## Overview

This project involves sentiment analysis of Twitter data to determine public opinions about various brands. It includes preprocessing, sentiment analysis using TextBlob, visualization of sentiment distributions, sentiment trends across brands, and generating word clouds for positive, negative, and neutral sentiments.

---

## Requirements

The project uses the following Python libraries:

- `pandas`: For data manipulation.
- `numpy`: For numerical operations.
- `seaborn`: For statistical data visualization.
- `matplotlib`: For plotting and visualizations.
- `textblob`: For sentiment analysis.
- `wordcloud`: For creating word clouds.

To install the required libraries, run:

```bash
pip install pandas numpy seaborn matplotlib textblob wordcloud
```

---

## Dataset

The dataset used for this analysis is a **Twitter training dataset**. It contains columns with Twitter data including brand names, tweet status, and customer responses. After initial preprocessing, the dataset has the following columns:

- **ID**: Unique identifier for each tweet.
- **Brand Name**: Name of the brand mentioned in the tweet.
- **Status**: The content of the tweet or the tweet status.
- **Response**: The customer response associated with the tweet.

The dataset is preprocessed to remove duplicates and clean up the headers.

---

## Key Steps

### 1. **Loading and Cleaning Data**
   - The dataset is loaded using `pandas`, and initial exploration such as checking for missing values and inspecting column data types is performed.
   - The first row of the dataset is used as the header and the column names are updated to reflect the structure: `ID`, `Brand Name`, `Status`, and `Response`.
   - Duplicate entries are removed from the dataset.

### 2. **Sentiment Analysis**
   - The sentiment of each tweet's status is analyzed using **TextBlob**. The sentiment is classified as:
     - **Positive**: Polarity > 0
     - **Neutral**: Polarity == 0
     - **Negative**: Polarity < 0
   - A new column, `calculated_sentiment`, is added to the dataset to store the sentiment for each tweet.
   - A distribution of sentiments is displayed using a count plot.

### 3. **Sentiment Trends**
   - Sentiment trends across different brands are analyzed using the `groupby` function to count the sentiment categories for each brand.
   - A line plot is used to visualize sentiment trends for brands over time.

### 4. **Word Clouds**
   - Word clouds are generated to display the most frequent words in customer responses, grouped by sentiment (positive, negative, and neutral).
   - The word clouds provide a visual summary of common terms associated with different sentiments.

---

## Visualizations

1. **Sentiment Distribution**: A count plot showing the frequency of positive, neutral, and negative sentiments.
2. **Sentiment Trend Over Brands**: A line plot showing the trend of sentiment for each brand.
3. **Word Clouds**: Three separate word clouds are generated for positive, negative, and neutral customer responses.

---

## How to Run

1. Clone or download the repository containing this notebook and the dataset.
2. Ensure the dataset (`twitter_training.csv`) is placed in the same directory as the notebook.
3. Install the necessary Python libraries as mentioned in the "Requirements" section.
4. Open the notebook in Jupyter, Google Colab, or any other notebook environment.
5. Run each code block sequentially to process the data, perform sentiment analysis, visualize trends, and generate word clouds.

---

## Contact

For any questions or issues regarding this project, please contact dhanushree2607@gmail.com.
