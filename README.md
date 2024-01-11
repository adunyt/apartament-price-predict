# Apartment Price Prediction

This repository contains Python code for building and comparing regression models to predict the price per square meter (`price_per_m2`) for apartments. The aim is to provide insights into the factors influencing apartment prices and to develop accurate predictive models.

## Dataset

The dataset is loaded from the file `clear_all_data.csv` using the `pandas` library. 

The target variable `y` is defined as the `price_per_m2`, representing the cost per square meter for each apartment. 

The input features `X` are derived from other relevant columns in the dataset:

1. **city**: The city in which the apartment is located (categorical).
2. **floor**: The floor on which the apartment is situated (integer).
3. **floors_count**: The total number of floors in the building (integer).
4. **rooms_count**: The number of rooms in the apartment (integer).
5. **total_meters**: The total area of the apartment in square meters (float).
6. **year_of_construction**: The year in which the building was constructed (integer).
7. **living_meters**: The area dedicated to living spaces within the apartment (float).
8. **kitchen_meters**: The area dedicated to the kitchen within the apartment (float).
9. **district**: The district in which the apartment is located (categorical).

## Data Encoding

Categorical features (`city` and `district`) are encoded using the `CatBoostEncoder` from the `category_encoders` library to prepare the data for regression model training.

## Model Training

The following regression models are trained and added to a list for comparison:

1. **Lasso Regression**: L1 regularized linear regression model trained using cross-validation.
2. **Linear Regression**: Traditional linear regression model.
3. **ElasticNET Regression**: Linear regression with a combination of L1 and L2 regularization.
4. **Ridge Regression**: Linear regression with L2 regularization.
5. **Gradient Boosting Regression**: Ensemble model based on decision trees.
6. **CatBoost Regressor** (most recent): Gradient boosting algorithm specifically designed for categorical features, with hyperparameters set to `depth=5`, `learning_rate=0.1`, `iterations=5000`, `loss_function="MAE"`, `od_type="Iter"`, `od_wait=350`.

## Prediction

The trained models are used to make predictions on a test set, and the results are stored in a list (`predict_list`). This enables a comparison of how well each model predicts the apartment prices.

## Results Visualization

A line plot is generated using `matplotlib` and `seaborn` to visually compare the predicted values against the actual values. The black line represents the actual prices, while each colored line represents the predictions from a different regression model.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/adunyt/apartament-price-predict.git
   cd apartament-price-predict
   ```

2. Install Jupyter:

   ```bash
   pip install jupyter
   ```

3. Run the `catboost.ipynb` notebook to use CatBoost regressor **(recommended)**:

   ```bash
   jupyter notebook catboost.ipynb
   ```

4. Run the `main.ipynb` notebook to use sklearn models:

   ```bash
   jupyter notebook main.ipynb
   ```
