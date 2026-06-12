# Netflix Recommendation System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-Surprise](https://img.shields.io/badge/Library-Scikit--Surprise-orange.svg)
![Machine Learning](https://img.shields.io/badge/Domain-Machine_Learning-success.svg)

## Overview
This project develops a highly personalized movie recommendation engine utilizing the legendary **Netflix Prize Dataset**. The objective is to intelligently learn user preferences from historical movie ratings, overcome extreme matrix sparsity, and generate highly relevant Top-K recommendations for unseen content.

## Project Deliverables
- **`Untitled.ipynb`**: The core Jupyter Notebook containing all Exploratory Data Analysis (EDA), model training, data visualizations, and evaluation code.
- **`Netflix_Recommendation_Presentation.pdf`**: A professional, detailed 8-slide executive presentation outlining the motivation, methodology, and key results.
- **`Netflix Recommendation System for Personalized Content Discovery.docx`**: A comprehensive technical report detailing the dataset architecture, model design choices, and deeper insights.

## The Challenge
Recommendation systems power modern digital streaming products by driving user engagement and retention. The core challenge addressed in this project is **extreme matrix sparsity (98.4%)**—because each of the 480K users rates only a tiny fraction of the 17.7K available movies, traditional item-to-item correlation often fails to accurately map users to niche, unrated titles.

## Methodology

Two distinct paradigms were engineered and evaluated:
1. **Item-Based Collaborative Filtering**: Computes similarity between items based on historical overlap. Highly interpretable but computationally expensive at scale and vulnerable to the sparsity problem.
2. **Singular Value Decomposition (SVD)**: A powerful Matrix Factorization technique that reduces matrix dimensionality to uncover hidden *latent factors*. These factors mathematically represent underlying movie traits and user tastes.

## Key Results

The models were evaluated using a strict 80/20 train-test split, focusing on **Root Mean Squared Error (RMSE)** for absolute prediction accuracy and **MAP@10** for ranking quality (with a relevance threshold of >= 3.5).

| Model | RMSE | Status |
|---|---|---|
| Item-Based Collaborative Filtering | 1.0723 | Baseline |
| **Singular Value Decomposition (SVD)** | **0.9889** | **Selected** |

The SVD architecture vastly outperformed traditional Collaborative Filtering. It successfully minimized prediction error by extracting meaningful latent structures from the highly sparse dataset, generating accurate Top-10 personalized recommendations even for niche sub-genres.

## Setup & Execution

### 1. Environment Setup
Navigate to the project directory and set up a virtual environment:
```bash
python -m venv venv

# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Core dependencies include: `pandas`, `numpy`, `matplotlib`, `seaborn`, and `scikit-surprise`)*

### 3. Data Preparation
Ensure the Netflix Prize Dataset is extracted into a `data/` folder in the root directory. The script expects files like `combined_data_1.txt` and `movie_titles.csv` to be present.

### 4. Running the Code
1. Open `Untitled.ipynb` in your IDE (e.g., VS Code).
2. Ensure your notebook kernel is set to the Python interpreter inside your newly created `venv`.
3. Run all cells to reproduce the data visualizations, train the models, and generate the final recommendations.

## Future Roadmap
- **Hybrid Models**: Incorporate Movie Metadata (genres, cast, release year) alongside explicit ratings to build a context-aware engine and solve the "Cold-Start" problem for new users.
- **Neural Collaborative Filtering**: Integrate Deep Learning to capture highly non-linear user-item relationships that standard matrix factorization might miss.
